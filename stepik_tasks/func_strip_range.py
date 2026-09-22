from functools import wraps
def strip_range(start, end, char = "."):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            result = value[:start] + len(value[start:end]) * char + value[end:]
            return result
        return wrapper
    return decorator


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())