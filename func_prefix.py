from functools import wraps
def prefix(string, to_the_end = False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if to_the_end:
                return result + string
            else:
                return string + result
        return wrapper
    return decorator


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())