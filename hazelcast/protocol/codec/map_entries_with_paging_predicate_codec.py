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

# Generated("9ada09a6b38de56850198f76a332899a")

# hex: 0x013600
REQUEST_MESSAGE_TYPE = 79360
# hex: 0x013601
RESPONSE_MESSAGE_TYPE = 79361
REQUEST_INITIAL_FRAME_SIZE = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
RESPONSE_INITIAL_FRAME_SIZE = RESPONSE_BACKUP_ACKS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES


def encode_request(name, predicate):
    client_message = ClientMessage.create_for_encode()
    client_message.retryable = True
    client_message.operation_name = "Map.EntriesWithPagingPredicate"
    initial_frame = ClientMessage.Frame(bytearray(REQUEST_INITIAL_FRAME_SIZE), UNFRAGMENTED_MESSAGE)
    FixedSizeTypesCodec.encode_int(initial_frame.content, TYPE_FIELD_OFFSET, REQUEST_MESSAGE_TYPE)
    client_message.add(initial_frame)
    StringCodec.encode(client_message, name)
    PagingPredicateHolderCodec.encode(client_message, predicate)
    return client_message


def decode_response(client_message):
    iterator = client_message.frame_iterator()
    response = dict(response=None, anchorDataList=None)
    #empty initial frame
    iterator.next()
    response["response"] = EntryListCodec.decode(iterator, DataCodec.decode, DataCodec.decode)
    response["anchorDataList"] = AnchorDataListHolderCodec.decode(iterator)
    return response


