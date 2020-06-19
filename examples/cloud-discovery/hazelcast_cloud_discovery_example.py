import hazelcast

if __name__ == "__main__":
    config = hazelcast.ClientConfig()

    # Set up cluster name
    config.cluster_name = "hazelcast"

    # Enable SSL for encryption. Default CA certificates will be used.
    config.network_config.ssl_config.enabled = True

    # Enable Hazelcast.Cloud configuration and set the token of your cluster.
    config.network_config.cloud_config.enabled = True
    config.network_config.cloud_config.discovery_token = "token"

    # Start a new Hazelcast client with this configuration.
    client = hazelcast.HazelcastClient(config)

    my_map = client.get_map("map-on-the-cloud")
    my_map.put("key", "hazelcast.cloud")

    print(my_map.get("key"))

    client.shutdown()
