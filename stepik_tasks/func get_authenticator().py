def get_authenticator():
    attempts = 3
    def auth(password):
        nonlocal attempts
        if attempts == 0:
            return "Доступ блокирован"
        if password == "python123":
            return "Доступ разрешен"
        else:
            attempts -= 1
            if attempts == 0:
                return "Доступ блокирован"
            else:
                 return "Неверный пароль"
    return auth
login = get_authenticator()

print(login("wrong_1"))
print(login("wrong_2"))
print(login("wrong_3"))
print(login("python123"))
print(login("qwerty12345"))









