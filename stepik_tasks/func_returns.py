from functools import wraps
def returns(datatype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, datatype):
                raise TypeError
            return result
        return wrapper
    return decorator
@returns(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))