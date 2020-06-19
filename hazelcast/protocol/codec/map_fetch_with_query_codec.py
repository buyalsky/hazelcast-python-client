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

# Generated("d769b398646d466d9850b7ad9273dbc0")

# hex: 0x014000
REQUEST_MESSAGE_TYPE = 81920
# hex: 0x014001
RESPONSE_MESSAGE_TYPE = 81921
REQUEST_BATCH_FIELD_OFFSET = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
REQUEST_INITIAL_FRAME_SIZE = REQUEST_BATCH_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
RESPONSE_INITIAL_FRAME_SIZE = RESPONSE_BACKUP_ACKS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES


def encode_request(name, iteration_pointers, batch, projection, predicate):
    client_message = ClientMessage.create_for_encode()
    client_message.retryable = True
    client_message.operation_name = "Map.FetchWithQuery"
    initial_frame = ClientMessage.Frame(bytearray(REQUEST_INITIAL_FRAME_SIZE), UNFRAGMENTED_MESSAGE)
    fixed_size_types_codec.encode_int(initial_frame.content, TYPE_FIELD_OFFSET, REQUEST_MESSAGE_TYPE)
    fixed_size_types_codec.encode_int(initial_frame.content, PARTITION_ID_FIELD_OFFSET, -1)
    fixed_size_types_codec.encode_int(initial_frame.content, REQUEST_BATCH_FIELD_OFFSET, batch)
    client_message.add(initial_frame)
    string_codec.encode(client_message, name)
    entry_list_integer_integer_codec.encode(client_message, iteration_pointers)
    data_codec.encode(client_message, projection)
    data_codec.encode(client_message, predicate)
    return client_message


def decode_response(client_message, to_object=None):
    iterator = client_message.frame_iterator()
    response = dict(results=None, iterationPointers=None)
    # empty initial frame
    iterator.next()
    response["results"] = list_multi_frame_codec.decode_contains_nullable(iterator, data_codec.decode)
    response["iterationPointers"] = entry_list_integer_integer_codec.decode(iterator)
    return response


