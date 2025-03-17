def add_and_subtract(first_number: int, second_number: int, third_number: int) -> int:
    def sum_numbers():
        after_sum = first_number + second_number
        return after_sum

    def subtract():
        after_subtract = sum_numbers() - third_number
        return after_subtract
    return subtract()

try1 = add_and_subtract(1, 17, 30)
print(try1)