def min_max_sum(sequence):
    int_list = [int(x) for x in sequence.split()]
    min_number = min(int_list)
    max_number = max(int_list)
    sum_numbers = sum(int_list)

    return (f"The minimum number is {min_number}\n"
            f"The maximum number is {max_number}\n"
            f"The sum number is: {sum_numbers}")


numbers = input()
test1 = min_max_sum(numbers)
print(test1)