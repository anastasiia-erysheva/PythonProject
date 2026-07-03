factory_data = [
    ("Анастасия", "Пошив", 1500),
    ("Михаил", "Сборка", 1200),
    ("Анастасия", "Пошив", 1800),
]
workers = {}
for name, shop, salary in factory_data:
    if name not in workers:
        workers[name] = (shop, salary)
    else:
        old_salary = workers[name][1]
        if salary > old_salary:
            workers[name] = (shop, salary)
print(workers)