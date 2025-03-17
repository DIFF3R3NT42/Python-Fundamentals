def smallest_number(first_number: int, second_number: int, third_number: int) -> int:
    smallest_n = min(first_number, second_number, third_number)
    return smallest_n

try1 = smallest_number(2, 5, 3)
print(try1)