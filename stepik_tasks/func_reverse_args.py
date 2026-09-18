from functools import wraps
def reverse_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args[::-1], **kwargs)
        return result
    return wrapper


@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))