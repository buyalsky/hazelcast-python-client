from hazelcast.protocol.client_message import ClientMessage, PARTITION_ID_FIELD_OFFSET, RESPONSE_BACKUP_ACKS_FIELD_OFFSET, UNFRAGMENTED_MESSAGE, TYPE_FIELD_OFFSET
import hazelcast.protocol.bits as Bits
from hazelcast.protocol.codec.builtin import *
from hazelcast.protocol.codec.custom import *
from hazelcast.util import ImmutableLazyDataList

"""
 * This file is auto-generated by the Hazelcast Client Protocol Code Generator.
 * To change this file, edit the templates or the protocol
 * definitions on the https://github.com/hazelcast/hazelcast-client-protocol
 * and regenerate it.
"""

# Generated("b7e4fb3662fe0fdc3275e061c96de954")

# hex: 0x010800
REQUEST_MESSAGE_TYPE = 67584
# hex: 0x010801
RESPONSE_MESSAGE_TYPE = 67585
REQUEST_THREAD_ID_FIELD_OFFSET = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
REQUEST_INITIAL_FRAME_SIZE = REQUEST_THREAD_ID_FIELD_OFFSET + Bits.LONG_SIZE_IN_BYTES
RESPONSE_RESPONSE_FIELD_OFFSET = RESPONSE_BACKUP_ACKS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES

RESPONSE_INITIAL_FRAME_SIZE = RESPONSE_RESPONSE_FIELD_OFFSET + Bits.BOOLEAN_SIZE_IN_BYTES


def encode_request(name, key, value, thread_id):
    client_message = ClientMessage.create_for_encode()
    client_message.retryable = False
    client_message.operation_name = "Map.RemoveIfSame"
    initial_frame = ClientMessage.Frame(bytearray(REQUEST_INITIAL_FRAME_SIZE), UNFRAGMENTED_MESSAGE)
    fixed_size_types_codec.encode_int(initial_frame.content, TYPE_FIELD_OFFSET, REQUEST_MESSAGE_TYPE)
    fixed_size_types_codec.encode_int(initial_frame.content, PARTITION_ID_FIELD_OFFSET, -1)
    fixed_size_types_codec.encode_long(initial_frame.content, REQUEST_THREAD_ID_FIELD_OFFSET, thread_id)
    client_message.add(initial_frame)
    string_codec.encode(client_message, name)
    data_codec.encode(client_message, key)
    data_codec.encode(client_message, value)
    return client_message


def decode_response(client_message, to_object=None):
    iterator = client_message.frame_iterator()
    response = dict(response=None)
    initial_frame = iterator.next()
    response["response"] = fixed_size_types_codec.decode_boolean(initial_frame.content, RESPONSE_RESPONSE_FIELD_OFFSET)
    return response


