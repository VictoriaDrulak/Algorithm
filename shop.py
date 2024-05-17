class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop name: {self.shop_name}")
        print(f"Store type: {self.store_type}")

    def open_shop(self):
        print(f"The online shop {self.shop_name} is now open.")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, increment):
        self.number_of_units += increment


class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discount_products(self):
        print(f"Discounted products at {self.shop_name}:")
        for product in self.discount_products:
            print(product)



from shop import Shop, Discount

store = Shop("MyStore", "Online")
print("Shop name:", store.shop_name)
print("Store type:", store.store_type)
store.describe_shop()
store.open_shop()

store1 = Shop("Store1", "Retail")
store2 = Shop("Store2", "Grocery")
store3 = Shop("Store3", "Clothing")
store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

print("\nInitial number of units:", store.number_of_units)
store.number_of_units = 10
print("Updated number of units:", store.number_of_units)

store.set_number_of_units(20)
print("Number of units after set_number_of_units method:", store.number_of_units)

store.increment_number_of_units(5)
print("Number of units after incrementing by 5:", store.number_of_units)

store_discount = Discount("DiscountStore", "Retail")
store_discount.discount_products = ["Product A", "Product B", "Product C"]

store_discount.get_discount_products()


from shop import Shop

all_store = Shop("AllStore", "Various")
all_store.open_shop()