def narcissistic( value ):
    narcissistic_number = str(value)
    return sum(int(digit) ** len(narcissistic_number) for digit in narcissistic_number) == value

print(narcissistic(153))

# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. 
# In this Kata, we will restrict ourselves to decimal (base 10).

# Best solution
# def narcissistic(value):
#     return value == sum(int(x) ** len(str(value)) for x in str(value))