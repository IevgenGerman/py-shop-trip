from app.customer import create_customers


def shop_trip():
    customer_list = create_customers()
    for customer in customer_list:
        print(customer)


shop_trip()