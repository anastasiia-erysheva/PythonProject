def bank_account():
    balance = 0
    result = balance

    while True:
        value = yield result

        if value == "show":
            result = balance

        elif value == "reset":
            balance = 0
            result = balance

        elif value == "double":
            balance *= 2
            result = balance

        elif value == "status":
            if balance > 0:
                result = "active"
            else:
                result = "empty"

        elif value < 0:
            if abs(value) <= balance:
                balance += value
            result = balance

        elif value > 0:
            balance += value
            result = balance

gen = bank_account()
next(gen)

print(gen.send(100))
print(gen.send(-30))
print(gen.send("double"))
print(gen.send("show"))
print(gen.send("reset"))
print(gen.send("double"))
print(gen.send(50))
print(gen.send("status"))
print(gen.send("reset"))
print(gen.send("status"))