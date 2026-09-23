def add_attrs(**kwargs):
    def decorator(func):
        func.__dict__.update(kwargs)
        return func
    return decorator


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)