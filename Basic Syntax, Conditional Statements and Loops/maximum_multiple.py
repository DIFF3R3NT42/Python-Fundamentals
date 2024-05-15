def find_largest_integer(divisor, bound):
    return bound // divisor * divisor


divisor = int(input())
bound = int(input())

result = find_largest_integer(divisor, bound)
print(result)
