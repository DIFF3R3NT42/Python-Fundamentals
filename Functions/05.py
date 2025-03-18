def get_even_numbers(*args):
    if len(args) == 1 and isinstance(args[0], str):
        num_list = [int(x) for x in args[0].split()]
    else:
        num_list = list(args)
    even_numbers = list(filter(lambda x: x % 2 == 0, num_list))
    return even_numbers

test1 = get_even_numbers(1, 2, 3, 4)
print(test1)