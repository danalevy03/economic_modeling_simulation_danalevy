# make an example of a method and magic method of luxury shops
class LuxuryShop:
    def __init__(self, name, revenue, location):
        self.name = name
        self.location = location
        self.revenue = revenue

    def annual_profit(self, expenses):
        return self.revenue - expenses

    def __str__(self):
        return f"{self.name} is located in {self.location} and has a revenue of {self.revenue}"

    def __eq__(self, other):
        return self.revenue == other.revenue

shop1 = LuxuryShop("Gucci", 1000000, "New York")
shop2 = LuxuryShop("Prada", 1000000, "Paris")

expenses = 500000
profit1 = shop1.annual_profit(expenses)
profit2 = shop2.annual_profit(expenses)
print("Annual profit of Gucci is", profit1)
print("Annual profit of Prada is", profit2)

print("String representation of Gucci is", str(shop1))

if shop1 == shop2:
    print("The two shops have the same revenue.")
else:
    print("The two shops have different revenue.")



