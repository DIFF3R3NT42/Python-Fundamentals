def sort_numbers(sequence):
    num_list = [int(x) for x in sequence.split()]
    return sorted(num_list)

numbers = input()

sorted_result = sort_numbers(numbers)
print("Sorted numbers:", sorted_result)