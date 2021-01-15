"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""


class Discount:
    def __init__(self, discount: float):
        self.discount = discount

    def get_discount(self, order: "Order") -> float:
        return order.price * self.discount


class MorningDiscount(Discount):
    def __init__(self):
        super(MorningDiscount, self).__init__(0.5)


class EveningDiscount(Discount):
    def __init__(self):
        super(EveningDiscount, self).__init__(0.9)


class Order:
    def __init__(self, price: float, discount: Discount = None):
        self.price = price
        self.discount = discount

    def set_discount(self, new_discount: Discount):
        self.discount = new_discount

    def final_price(self) -> float:
        diff = self.discount().get_discount(self) if self.discount else 0
        return self.price - diff
