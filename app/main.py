import json

from dataclasses import dataclass

from Tools.scripts.dutree import store


class ProductCard:
    def __init__(self,
                 milk: int | float,
                 bread: int | float,
                 butter: int | float) -> None:
        self.milk = milk
        self.bread = bread
        self.butter = butter


class CustomerCar:
    def __init__(self,
                 brand: str,
                 fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption


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


def shop_trip():
    with open("config.json", "rb") as file:
        dataset = json.load(file)
        customers = dataset["customers"]
        fuel_price = dataset["FUEL_PRICE"]
        shops = dataset["shops"]
        customer_list = []
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

        for customer in customer_list:
            print(customer)


shop_trip()