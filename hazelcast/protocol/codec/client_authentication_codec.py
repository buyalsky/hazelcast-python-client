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

# Generated("a9505ba5284de525aa628da0e0c991b4")

# hex: 0x000100
REQUEST_MESSAGE_TYPE = 256
# hex: 0x000101
RESPONSE_MESSAGE_TYPE = 257
REQUEST_UUID_FIELD_OFFSET = PARTITION_ID_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
REQUEST_SERIALIZATION_VERSION_FIELD_OFFSET = REQUEST_UUID_FIELD_OFFSET + Bits.UUID_SIZE_IN_BYTES
REQUEST_INITIAL_FRAME_SIZE = REQUEST_SERIALIZATION_VERSION_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES
RESPONSE_STATUS_FIELD_OFFSET = RESPONSE_BACKUP_ACKS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES
RESPONSE_MEMBER_UUID_FIELD_OFFSET = RESPONSE_STATUS_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES
RESPONSE_SERIALIZATION_VERSION_FIELD_OFFSET = RESPONSE_MEMBER_UUID_FIELD_OFFSET + Bits.UUID_SIZE_IN_BYTES
RESPONSE_PARTITION_COUNT_FIELD_OFFSET = RESPONSE_SERIALIZATION_VERSION_FIELD_OFFSET + Bits.BYTE_SIZE_IN_BYTES
RESPONSE_CLUSTER_ID_FIELD_OFFSET = RESPONSE_PARTITION_COUNT_FIELD_OFFSET + Bits.INT_SIZE_IN_BYTES
RESPONSE_FAILOVER_SUPPORTED_FIELD_OFFSET = RESPONSE_CLUSTER_ID_FIELD_OFFSET + Bits.UUID_SIZE_IN_BYTES

RESPONSE_INITIAL_FRAME_SIZE = RESPONSE_FAILOVER_SUPPORTED_FIELD_OFFSET + Bits.BOOLEAN_SIZE_IN_BYTES


def encode_request(cluster_name, username, password, uuid, client_type, serialization_version, client_hazelcast_version, client_name, labels):
    client_message = ClientMessage.create_for_encode()
    client_message.retryable = True
    client_message.operation_name = "Client.Authentication"
    initial_frame = ClientMessage.Frame(bytearray(REQUEST_INITIAL_FRAME_SIZE), UNFRAGMENTED_MESSAGE)
    FixedSizeTypesCodec.encode_int(initial_frame.content, TYPE_FIELD_OFFSET, REQUEST_MESSAGE_TYPE)
    FixedSizeTypesCodec.encode_uuid(initial_frame.content, REQUEST_UUID_FIELD_OFFSET, uuid)
    FixedSizeTypesCodec.encode_byte(initial_frame.content, REQUEST_SERIALIZATION_VERSION_FIELD_OFFSET, serialization_version)
    client_message.add(initial_frame)
    StringCodec.encode(client_message, cluster_name)
    CodecUtil.encode_nullable(client_message, username, StringCodec.encode)
    CodecUtil.encode_nullable(client_message, password, StringCodec.encode)
    StringCodec.encode(client_message, client_type)
    StringCodec.encode(client_message, client_hazelcast_version)
    StringCodec.encode(client_message, client_name)
    ListMultiFrameCodec.encode(client_message, labels, StringCodec.encode)
    return client_message


def decode_response(client_message):
    iterator = client_message.frame_iterator()
    response = dict(status=None, address=None, memberUuid=None, serializationVersion=None, serverHazelcastVersion=None, partitionCount=None, clusterId=None, failoverSupported=None)
    initial_frame = iterator.next()
    response["status"] = FixedSizeTypesCodec.decode_byte(initial_frame.content, RESPONSE_STATUS_FIELD_OFFSET)
    response["memberUuid"] = FixedSizeTypesCodec.decode_uuid(initial_frame.content, RESPONSE_MEMBER_UUID_FIELD_OFFSET)
    response["serializationVersion"] = FixedSizeTypesCodec.decode_byte(initial_frame.content, RESPONSE_SERIALIZATION_VERSION_FIELD_OFFSET)
    response["partitionCount"] = FixedSizeTypesCodec.decode_int(initial_frame.content, RESPONSE_PARTITION_COUNT_FIELD_OFFSET)
    response["clusterId"] = FixedSizeTypesCodec.decode_uuid(initial_frame.content, RESPONSE_CLUSTER_ID_FIELD_OFFSET)
    response["failoverSupported"] = FixedSizeTypesCodec.decode_boolean(initial_frame.content, RESPONSE_FAILOVER_SUPPORTED_FIELD_OFFSET)
    response["address"] = CodecUtil.decode_nullable(iterator, AddressCodec.decode)
    response["serverHazelcastVersion"] = StringCodec.decode(iterator)
    return response


