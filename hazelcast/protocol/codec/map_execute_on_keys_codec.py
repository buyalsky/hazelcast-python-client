from hazelcast.protocol.client_message import ClientMessage, PARTITION_ID_FIELD_OFFSET, RESPONSE_BACKUP_ACKS_FIELD_OFFSET, UNFRAGMENTED_MESSAGE, TYPE_FIELD_OFFSET
import hazelcast.protocol.bits as Bits
from hazelcast.protocol.codec.builtin import *
from hazelcast.protocol.codec.custom import *

"""
 * This file is auto-generated by the Hazelcast Client Protocol Code Generator.
 * To change this file, edit the templates or the protocol
 * definitions on the https://github.com/hazelcast/hazelcast-client-protocol
 * and regenerate it.
"""

# Generated("a7b51075e5385cbaf4e10fdaccb5a477")

# hex: 0x013200
REQUEST_MESSAGE_TYPE = 78336
# hex: 0x013201
RESPONSE_MESSAGE_TYPE = 78337
REQUEST_INITIAL_FRAME_SIZE = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
RESPONSE_INITIAL_FRAME_SIZE = RESPONSE_BACKUP_ACKS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES


def encode_request(name, entry_processor, keys):
    client_message = ClientMessage.create_for_encode()
    client_message.retryable = False
    client_message.operation_name = "Map.ExecuteOnKeys"
    initial_frame = ClientMessage.Frame(bytearray(REQUEST_INITIAL_FRAME_SIZE), UNFRAGMENTED_MESSAGE)
    FixedSizeTypesCodec.encode_int(initial_frame.content, TYPE_FIELD_OFFSET, REQUEST_MESSAGE_TYPE)
    client_message.add(initial_frame)
    StringCodec.encode(client_message, name)
    DataCodec.encode(client_message, entry_processor)
    ListMultiFrameCodec.encode(client_message, keys, DataCodec.encode)
    return client_message


def decode_response(client_message):
    iterator = client_message.frame_iterator()
    response = dict(response=None)
    #empty initial frame
    iterator.next()
    response["response"] = EntryListCodec.decode(iterator, DataCodec.decode, DataCodec.decode)
    return response


