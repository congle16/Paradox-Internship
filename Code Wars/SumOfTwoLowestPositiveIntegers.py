def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
print(sum_two_smallest_numbers([5, 8, 12, 19, 22]))

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# Best Practice
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])