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

# Generated("e26cd07b352785778a5fef831a6f7ac8")

# hex: 0x050B00
REQUEST_MESSAGE_TYPE = 330496
# hex: 0x050B01
RESPONSE_MESSAGE_TYPE = 330497
REQUEST_INCLUDE_VALUE_FIELD_OFFSET = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
REQUEST_LOCAL_ONLY_FIELD_OFFSET = REQUEST_INCLUDE_VALUE_FIELD_OFFSET + Bits.BOOLEAN_SIZE_IN_BYTES
REQUEST_INITIAL_FRAME_SIZE = REQUEST_LOCAL_ONLY_FIELD_OFFSET + Bits.BOOLEAN_SIZE_IN_BYTES
RESPONSE_RESPONSE_FIELD_OFFSET = RESPONSE_BACKUP_ACKS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES

RESPONSE_INITIAL_FRAME_SIZE = RESPONSE_RESPONSE_FIELD_OFFSET + Bits.UUID_SIZE_IN_BYTES
EVENT_ITEM_UUID_FIELD_OFFSET = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
EVENT_ITEM_EVENT_TYPE_FIELD_OFFSET = EVENT_ITEM_UUID_FIELD_OFFSET + Bits.UUID_SIZE_IN_BYTES
EVENT_ITEM_INITIAL_FRAME_SIZE = EVENT_ITEM_EVENT_TYPE_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
    #hex: 0x050B02
EVENT_ITEM_MESSAGE_TYPE = 330498


def encode_request(name, include_value, local_only):
    client_message = ClientMessage.create_for_encode()
    client_message.retryable = False
    client_message.operation_name = "List.AddListener"
    initial_frame = ClientMessage.Frame(bytearray(REQUEST_INITIAL_FRAME_SIZE), UNFRAGMENTED_MESSAGE)
    FixedSizeTypesCodec.encode_int(initial_frame.content, TYPE_FIELD_OFFSET, REQUEST_MESSAGE_TYPE)
    FixedSizeTypesCodec.encode_boolean(initial_frame.content, REQUEST_INCLUDE_VALUE_FIELD_OFFSET, include_value)
    FixedSizeTypesCodec.encode_boolean(initial_frame.content, REQUEST_LOCAL_ONLY_FIELD_OFFSET, local_only)
    client_message.add(initial_frame)
    StringCodec.encode(client_message, name)
    return client_message


def decode_response(client_message):
    iterator = client_message.frame_iterator()
    response = dict(response=None)
    initial_frame = iterator.next()
    response["response"] = FixedSizeTypesCodec.decode_uuid(initial_frame.content, RESPONSE_RESPONSE_FIELD_OFFSET)
    return response


def handle(client_message, handle_item_event=None):
    message_type = client_message.message_type()
    iterator = client_message.frame_iterator()
    if message_type == EVENT_ITEM_MESSAGE_TYPE and handle_item_event is not None:
        initial_frame = iterator.next()
        uuid = FixedSizeTypesCodec.decode_uuid(initial_frame.content, EVENT_ITEM_UUID_FIELD_OFFSET)
        event_type = FixedSizeTypesCodec.decode_int(initial_frame.content, EVENT_ITEM_EVENT_TYPE_FIELD_OFFSET)
        item = CodecUtil.decode_nullable(iterator, DataCodec.decode)
        handle_item_event(item, uuid, event_type)
