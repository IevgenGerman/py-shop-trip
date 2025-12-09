import json

from app.car import CustomerCar
from app.product_card import ProductCard


class Customers(ProductCard, CustomerCar):
    def __init__(self,
                 name: str | float,
                 location: list,
                 money: int | float,
                 milk: int | float,
                 bread: int | float,
                 butter: int | float,
                 brand: str,
                 fuel_consumption: float) -> None:
        ProductCard.__init__(self, milk, bread, butter)
        CustomerCar.__init__(self, brand, fuel_consumption)
        self.name = name
        self.location = location
        self.money = money

    def __repr__(self) -> str:
        return f"Customer name = {self.name}"

def create_customers() -> list:
    customer_list = []
    with open("config.json", "rb") as file:
        dataset = json.load(file)
        customers = dataset["customers"]
        fuel_price = dataset["FUEL_PRICE"]
        shops = dataset["shops"]
        for i, user in enumerate(customers):
            customer_list.append(
                Customers(user["name"],
                          user["location"],
                          user["money"],
                          user["product_cart"]["milk"],
                          user["product_cart"]["bread"],
                          user["product_cart"]["butter"],
                          user["car"]["brand"],
                          user["car"]["fuel_consumption"],
                          )
            )
    return customer_list

