from hazelcast.protocol.client_message import ClientMessage, IS_FINAL_FLAG, SIZE_OF_FRAME_LENGTH_AND_FLAGS
from hazelcast.protocol.bits import FMT_LE_INT, FMT_LE_UINT16, INT_SIZE_IN_BYTES, SHORT_SIZE_IN_BYTES

import struct


class ClientMessageWriter:
    def __init__(self, connection):
        self.current_frame = None
        self.connection = connection
        self.write_offset = -1

    def write_to(self, client_message):
        if self.current_frame is None:
            self.current_frame = client_message.start_frame

        while True:
            is_last_frame = self.current_frame.next is None
            if self.write_frame(self.current_frame, is_last_frame):
                self.write_offset = -1
                if is_last_frame:
                    self.current_frame = None
                    return True
                self.current_frame = self.current_frame.next
            else:
                return False

    def write_frame(self, frame, is_last_frame):
        frame_content_length = 0 if frame.content is None else len(frame.content)
        #if self.write_offset == -1:
        data = bytearray(frame_content_length + SIZE_OF_FRAME_LENGTH_AND_FLAGS)
        #self.connection.write(struct.pack(FMT_LE_INT, frame_content_length + SIZE_OF_FRAME_LENGTH_AND_FLAGS))
        #self.write_offset += INT_SIZE_IN_BYTES
        struct.pack_into(FMT_LE_INT, data, 0, frame_content_length + SIZE_OF_FRAME_LENGTH_AND_FLAGS)


        if is_last_frame:
            struct.pack_into(FMT_LE_UINT16, data, INT_SIZE_IN_BYTES, frame.flags | IS_FINAL_FLAG)
        else:
            struct.pack_into(FMT_LE_UINT16, data, INT_SIZE_IN_BYTES, frame.flags)

        #self.write_offset += SHORT_SIZE_IN_BYTES
        #self.write_offset = 0

        #bytes_writable = len(dst) - self.write_offset
        #done = False
        """
        if bytes_writable >= bytes_needed:
            bytes_write = bytes_needed
            done = True
        else:
            bytes_write = bytes_writable
            done = False

        """
        #print(frame.content)
        data[SIZE_OF_FRAME_LENGTH_AND_FLAGS:] = frame.content[:]
        self.connection.write(data)

        return True
