from collections import namedtuple

# Добавили цену (price) в структуру
Order = namedtuple("Order", ["id", "item", "amount", "price", "status"], defaults=["pending"])

orders_list = [
    Order(1, 'Телефон', 1, 50000, 'delivered'),
    Order(2, 'Наушники', 2, 3000, 'pending'),
    Order(3, 'Ноутбук', 1, 90000, 'delivered'),
    Order(4, 'Чехол', 5, 500, 'pending')
]
total_revenue = 0
for order in orders_list:
    if order.status == 'delivered':
        total_revenue += order.amount * order.price
print(total_revenue)