from typing import Tuple


def odd_and_even_sum(number: int) -> Tuple[int, int]:
    digits = str(number)

    odd_sum = 0
    even_sum = 0

    for digit in digits:
        num = int(digit)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return odd_sum, even_sum

try1 = odd_and_even_sum(1000435)
print(f"Odd sum = {try1[0]}, Even sum = {try1[1]}")