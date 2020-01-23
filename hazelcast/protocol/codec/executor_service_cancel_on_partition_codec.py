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

# Generated("cf62e223096542335ed28db05557d341")

# hex: 0x080300
REQUEST_MESSAGE_TYPE = 525056
# hex: 0x080301
RESPONSE_MESSAGE_TYPE = 525057
REQUEST_UUID_FIELD_OFFSET = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
REQUEST_INTERRUPT_FIELD_OFFSET = REQUEST_UUID_FIELD_OFFSET + Bits.UUID_SIZE_IN_BYTES
REQUEST_INITIAL_FRAME_SIZE = REQUEST_INTERRUPT_FIELD_OFFSET + Bits.BOOLEAN_SIZE_IN_BYTES
RESPONSE_RESPONSE_FIELD_OFFSET = RESPONSE_BACKUP_ACKS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES

RESPONSE_INITIAL_FRAME_SIZE = RESPONSE_RESPONSE_FIELD_OFFSET + Bits.BOOLEAN_SIZE_IN_BYTES


def encode_request(uuid, interrupt):
    client_message = ClientMessage.create_for_encode()
    client_message.retryable = False
    client_message.operation_name = "ExecutorService.CancelOnPartition"
    initial_frame = ClientMessage.Frame(bytearray(REQUEST_INITIAL_FRAME_SIZE), UNFRAGMENTED_MESSAGE)
    FixedSizeTypesCodec.encode_int(initial_frame.content, TYPE_FIELD_OFFSET, REQUEST_MESSAGE_TYPE)
    FixedSizeTypesCodec.encode_uuid(initial_frame.content, REQUEST_UUID_FIELD_OFFSET, uuid)
    FixedSizeTypesCodec.encode_boolean(initial_frame.content, REQUEST_INTERRUPT_FIELD_OFFSET, interrupt)
    client_message.add(initial_frame)
    return client_message


def decode_response(client_message):
    iterator = client_message.frame_iterator()
    response = dict(response=None)
    initial_frame = iterator.next()
    response["response"] = FixedSizeTypesCodec.decode_boolean(initial_frame.content, RESPONSE_RESPONSE_FIELD_OFFSET)
    return response


