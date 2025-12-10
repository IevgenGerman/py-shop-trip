import json
from functools import wraps

from app.check_if_exist import check_values
from app.customer import Customers
from app.shops import Shops

def read_value_from_file(name: str, mode: str) -> dict:
    with open(name, mode) as file:
        try:
            dataset = json.load(file)
        except FileNotFoundError:
            print(f"file {'config.json'} not found")
    return dataset

dataset = read_value_from_file("config.json", "rb")

def check_if_full_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if check_values(dataset, "FUEL_PRICE", "customers", "shops"):
            result = func(*args, **kwargs)
        return result
    return wrapper

@check_if_full_data
def create_customers_examples():
    customer_list = dataset["customers"]
    list_of_customer = []
    for customer in customer_list:
        list_of_customer.append(Customers.create_list_of_customers(customer))
    return list_of_customer

@check_if_full_data
def create_shops_examples():
    shop_list = dataset["shops"]
    list_of_shop = []
    for shop in shop_list:
        list_of_shop.append(Shops.create_list_of_shops(shop))
    return list_of_shop

@check_if_full_data
def create_fuel_cost():
    return dataset["FUEL_PRICE"]
