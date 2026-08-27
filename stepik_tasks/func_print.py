old_print = print
def custom_print(*args, **kwargs):
    new_args = []
    for elem in args:
        if isinstance(elem, str):
            new_args.append(elem.upper())
        else:
            new_args.append(elem)
    if 'sep' in kwargs and isinstance(kwargs['sep'], str):
        kwargs['sep'] = kwargs['sep'].upper()
    if 'end' in kwargs and isinstance(kwargs['end'], str):
        kwargs['end'] = kwargs['end'].upper()
    old_print(*new_args, **kwargs)
print = custom_print
words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')

