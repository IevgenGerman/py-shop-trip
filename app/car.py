from dataclasses import dataclass

#
# class CheckValue:
#     def __init__(self, *expected_types: type):
#         self.expected_types = expected_types
#         self.private_name = None
#
#     def __set_name__(self, owner, name):
#         self.private_name = "_" + name

@dataclass
class CustomerCar:
    brand: str
    fuel_consumption: float
