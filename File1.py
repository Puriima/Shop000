class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Пример использования
store1 = Store("Best Buys", "123 Market St")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2 = Store("Tech Gadgets", "456 Tech Ave")
store2.add_item("mouse", 10)
store2.add_item("keyboard", 20)

store3 = Store("Book Heaven", "789 Bibliophile Blvd")
store3.add_item("Python Programming", 59.99)
store3.add_item("Effective Java", 49.99)

# Тестируем методы на store1
print(store1.get_price("apples"))  # 0.5
store1.update_price("apples", 0.6)
print(store1.get_price("apples"))  # 0.6
store1.remove_item("apples")
print(store1.get_price("apples"))  # None