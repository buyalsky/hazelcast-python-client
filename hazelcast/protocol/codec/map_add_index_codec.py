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

# Generated("e3ba824f416bbe642ab597cedea4e3e1")

# hex: 0x012900
REQUEST_MESSAGE_TYPE = 76032
# hex: 0x012901
RESPONSE_MESSAGE_TYPE = 76033
REQUEST_INITIAL_FRAME_SIZE = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
RESPONSE_INITIAL_FRAME_SIZE = RESPONSE_BACKUP_ACKS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES


def encode_request(name, index_config):
    client_message = ClientMessage.create_for_encode()
    client_message.retryable = False
    client_message.operation_name = "Map.AddIndex"
    initial_frame = ClientMessage.Frame(bytearray(REQUEST_INITIAL_FRAME_SIZE), UNFRAGMENTED_MESSAGE)
    fixed_size_types_codec.encode_int(initial_frame.content, TYPE_FIELD_OFFSET, REQUEST_MESSAGE_TYPE)
    fixed_size_types_codec.encode_int(initial_frame.content, PARTITION_ID_FIELD_OFFSET, -1)
    client_message.add(initial_frame)
    string_codec.encode(client_message, name)
    index_config_codec.encode(client_message, index_config)
    return client_message


def decode_response(client_message, to_object=None):
    iterator = client_message.frame_iterator()
    response = dict()
    # empty initial frame
    iterator.next()
    return response


