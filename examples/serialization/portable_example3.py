import hazelcast

from hazelcast.serialization.api import Portable
from hazelcast.serialization.portable.classdef import ClassDefinitionBuilder


class HomeAddress(Portable):
    CLASS_ID = 3
    FACTORY_ID = 1

    def __init__(self, city=None):
        self.city = city

    def get_factory_id(self):
        return Address.FACTORY_ID

    def get_class_id(self):
        return Address.CLASS_ID

    def write_portable(self, writer: hazelcast.serialization.api.PortableWriter):
        writer.write_utf("city", self.city)

    def read_portable(self, reader):
        self.city = reader.read_utf("city")

    def __str__(self):
        return self.city


class Address(Portable):
    CLASS_ID = 2
    FACTORY_ID = 1

    def __init__(self, state=None, home_address=None):
        self.state = state
        self.home_address = home_address

    def get_factory_id(self):
        return Address.FACTORY_ID

    def get_class_id(self):
        return Address.CLASS_ID

    def write_portable(self, writer: hazelcast.serialization.api.PortableWriter):
        writer.write_utf("state", self.state)
        if self.home_address:
            writer.write_portable("home_address", self.home_address)
        else:
            writer.write_null_portable("home_address", 1, 3)

    def read_portable(self, reader):
        self.state = reader.read_utf("state")
        self.home_address = reader.read_portable("home_address")

    def __str__(self):
        return "-{}-{}".format(self.state, self.home_address)


class Employee(Portable):
    CLASS_ID = 1
    FACTORY_ID = 1

    def __init__(self, name=None, salary=None, company_name=None, address=None):
        self.name = name
        self.salary = salary
        self.company_name = company_name
        self.address = address

    def get_factory_id(self):
        return Employee.FACTORY_ID

    def get_class_id(self):
        return Employee.CLASS_ID

    def write_portable(self, writer: hazelcast.serialization.api.PortableWriter):
        writer.write_utf("firstName", self.name)
        writer.write_int("salaryPerMonth", self.salary)
        writer.write_utf("companyName", self.company_name)
        if self.address:
            writer.write_portable("address", self.address)
        else:
            writer.write_null_portable("address", 1, 2)

    def read_portable(self, reader: hazelcast.serialization.api.PortableReader):
        self.name = reader.read_utf("firstName")
        self.salary = reader.read_int("salaryPerMonth")
        self.company_name = reader.read_utf("companyName")
        self.address = reader.read_portable("address")

    def __str__(self):
        return "{}-{}-{}-{}".format(self.name, self.salary, self.company_name, self.address)


def put_values_into_map(map):
    # uncomment the following to serialize null portable
    map.put("emp0", Employee("kyle", 3000, "hazel"))
    map.put("emp1", Employee("kyle", 3000, "hazel", Address("nj")))
    map.put("emp2", Employee("adam", 2330, "cast", Address("tx", HomeAddress("Dallas"))))
    map.put("emp3", Employee("david", 3500, "jet", Address("au"))).result()


def read_values_from_map(map):
    keys = map.key_set().result()

    for key in keys:
        print("{} -> {}".format(key, map.get(key).result()))


if __name__ == '__main__':
    config = hazelcast.ClientConfig()
    factory = {Employee.CLASS_ID: Employee, Address.CLASS_ID: Address}
    config.serialization_config.add_portable_factory(1, factory)

    home_address_class_def = ClassDefinitionBuilder(1, HomeAddress.CLASS_ID).add_utf_field("city").build()

    address_class_def = ClassDefinitionBuilder(1, Address.CLASS_ID)\
        .add_utf_field("state")\
        .add_portable_field("home_address", home_address_class_def)\
        .build()

    employee_class_def = ClassDefinitionBuilder(1, Employee.CLASS_ID) \
        .add_utf_field("firstName") \
        .add_int_field("salaryPerMonth") \
        .add_utf_field("companyName") \
        .add_portable_field("address", address_class_def) \
        .build()

    # config.serialization_config.class_definitions.add(home_address_class_def)
    # config.serialization_config.class_definitions.add(address_class_def)
    config.serialization_config.class_definitions.add(employee_class_def)

    client = hazelcast.HazelcastClient(config)

    my_map = client.get_map("map2")
    put_values_into_map(my_map)
    read_values_from_map(my_map)

    client.shutdown()
