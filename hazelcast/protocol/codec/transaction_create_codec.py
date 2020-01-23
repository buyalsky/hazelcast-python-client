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

# Generated("53dbc4b8ad328aaced80dea4c7a1fe8f")

# hex: 0x150200
REQUEST_MESSAGE_TYPE = 1376768
# hex: 0x150201
RESPONSE_MESSAGE_TYPE = 1376769
REQUEST_TIMEOUT_FIELD_OFFSET = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
REQUEST_DURABILITY_FIELD_OFFSET = REQUEST_TIMEOUT_FIELD_OFFSET + Bits.LONG_SIZE_IN_BYTES
REQUEST_TRANSACTION_TYPE_FIELD_OFFSET = REQUEST_DURABILITY_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
REQUEST_THREAD_ID_FIELD_OFFSET = REQUEST_TRANSACTION_TYPE_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
REQUEST_INITIAL_FRAME_SIZE = REQUEST_THREAD_ID_FIELD_OFFSET + Bits.LONG_SIZE_IN_BYTES
RESPONSE_RESPONSE_FIELD_OFFSET = RESPONSE_BACKUP_ACKS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES

RESPONSE_INITIAL_FRAME_SIZE = RESPONSE_RESPONSE_FIELD_OFFSET + Bits.UUID_SIZE_IN_BYTES


def encode_request(timeout, durability, transaction_type, thread_id):
    client_message = ClientMessage.create_for_encode()
    client_message.retryable = False
    client_message.operation_name = "Transaction.Create"
    initial_frame = ClientMessage.Frame(bytearray(REQUEST_INITIAL_FRAME_SIZE), UNFRAGMENTED_MESSAGE)
    FixedSizeTypesCodec.encode_int(initial_frame.content, TYPE_FIELD_OFFSET, REQUEST_MESSAGE_TYPE)
    FixedSizeTypesCodec.encode_long(initial_frame.content, REQUEST_TIMEOUT_FIELD_OFFSET, timeout)
    FixedSizeTypesCodec.encode_int(initial_frame.content, REQUEST_DURABILITY_FIELD_OFFSET, durability)
    FixedSizeTypesCodec.encode_int(initial_frame.content, REQUEST_TRANSACTION_TYPE_FIELD_OFFSET, transaction_type)
    FixedSizeTypesCodec.encode_long(initial_frame.content, REQUEST_THREAD_ID_FIELD_OFFSET, thread_id)
    client_message.add(initial_frame)
    return client_message


def decode_response(client_message):
    iterator = client_message.frame_iterator()
    response = dict(response=None)
    initial_frame = iterator.next()
    response["response"] = FixedSizeTypesCodec.decode_uuid(initial_frame.content, RESPONSE_RESPONSE_FIELD_OFFSET)
    return response


