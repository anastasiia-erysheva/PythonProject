import functools
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f"TRACE: вызов {func_name}() с аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"TRACE: возвращаемое значение {func_name}(): {result!r}")
        return result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')
