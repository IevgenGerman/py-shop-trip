import datetime

from app.create_variales import create_customers_examples, create_fuel_cost, create_shops_examples


def shop_trip():
    shops = create_shops_examples()
    fuel_cost = create_fuel_cost()
    customers = create_customers_examples()
    for customer in customers:
        calculate_min_result = []
        print(f"{customer.name}'s has {customer.money} dollars")
        dict_for_calculate_shop = {}
        for shop in shops:
            result = 0
            result += shop.milk * customer.milk + shop.bread * customer.bread + shop.butter * customer.butter
            calculate_min_result.append(result)
            print(f"{customer.name}'s trip to the {shop.name} costs {result}")
            dict_for_calculate_shop[shop.name] = result
        min_value = min(calculate_min_result)
        name_chip_shop = [key for key, value in dict_for_calculate_shop.items() if value == min_value][0]
        chippest_shop = [shop for shop in shops if shop.name == name_chip_shop][0]
        if customer.money < min_value:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
        else:
            print(f"{customer.name}'s rides to {name_chip_shop}\n")

            now = datetime.datetime.now()
            print(f"Data: {now.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            print(f"{customer.milk} milks for {(customer.milk * chippest_shop.milk):.1f}")
            print(f"{customer.bread} breads for {customer.bread * chippest_shop.bread}")
            print(f"{customer.butter} butters for {customer.butter * chippest_shop.butter}")
            print(f"Total cost is {min_value:.1f} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {(customer.money - min_value):.1f} dollars\n")

    # print(a)
    # print(b)
    # print(c)

shop_trip()