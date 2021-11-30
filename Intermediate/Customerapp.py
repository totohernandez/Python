class Customer:
    def __init__(self, id, name, subscription):
        self.id = id
        self.name = name
        self.subscription = subscription

    def upgrade_subscription(self, new_subscription):
        print("Cambio su subscripcion:")
        self.subscription = new_subscription

    def __str__(self):
        return self.name + " " + self.subscription

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.subscription == other.subscription:
            return True
        else:
            return False

    # def read_customer():
    #     print("Reading from DB")



# c = Customer(1, "Toto", "1 mes")
# print(c.id, c.name, c.subscription)

customers = [Customer(1, "Toto", "1 mes"),
            Customer(2, "Ricardo", "1 anio")]

# print(customers[0].name)

# print(customers[0].subscription)
# customers[0].upgrade_subscription("1 anio")
# print(customers[0].subscription)

# print(customers[1])

Customer.print_all_customers(customers)

print(customers[0])