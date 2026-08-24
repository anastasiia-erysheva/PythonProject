class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass
def is_good_password(string):
    has_digit = any(x.isdigit() for x in string)
    has_upper = any(x.isupper() for x in string)
    has_lower = any(x.islower() for x in string)
    if len(string) < 9:
        raise LengthError()
    if not has_upper or not has_lower:
        raise LetterError()
    if not has_digit:
        raise DigitError()
    return True