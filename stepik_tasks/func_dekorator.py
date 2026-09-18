from functools import wraps

def do_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper


@do_twice
def beegeek():
    print('beegeek')


print(beegeek())