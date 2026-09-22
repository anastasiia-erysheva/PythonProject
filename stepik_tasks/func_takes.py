from functools import wraps
def takes(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            all_args = args + tuple(kwargs.values())
            for arg in all_args:
                if not isinstance(arg, types):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator
@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))