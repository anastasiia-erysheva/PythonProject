from collections import namedtuple
Order = namedtuple("Order", ["id", "item", "amount", "status"], defaults = ["pending"])
orders_list = [
    Order(1, 'Телефон', 1, 'delivered'),
    Order(2, 'Наушники', 2),
    Order(3, 'Ноутбук', 1, 'delivered'),
    Order(4, 'Чехол', 5)
]
total_amount = 0
for order in orders_list:
    if order.status == 'pending':
        total_amount += order.amount
print(total_amount)
