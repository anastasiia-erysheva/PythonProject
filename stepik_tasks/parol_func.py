def verification(login, password, success, failure):
    has_letter = any('A' <= c <= 'Z' or 'a' <= c <= 'z'  for c in password)
    has_upper = any('A' <= c <= 'Z' for c in password)
    has_lower = any('a' <= c <= 'z' for c in password)
    has_digit = any('0' <= c <= '9' for c in password)
    if not has_letter:
        failure(login, "в пароле нет ни одной буквы")
    elif not has_upper:
        failure(login, "в пароле нет ни одной заглавной буквы")
    elif not has_lower:
        failure(login, "в пароле нет ни одной строчной буквы")
    elif not has_digit:
        failure(login, "в пароле нет ни одной цифры")
    else:
        success(login)

def success(login):
    print(f'Привет, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

verification('timyrik20', 'Beegeek314', success, failure)
