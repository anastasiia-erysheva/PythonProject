def is_good_password(string):
    has_digit = any(x.isdigit() for x in string)
    has_upper = any(x.isupper() for x in string)
    has_lower = any(x.islower() for x in string)
    return len(string) >= 9 and has_digit and has_upper and has_lower
