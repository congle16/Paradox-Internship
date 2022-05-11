def order(sentence):
    dict_numbers = { key : value for value in sentence.split() for key in value if key.isdigit() }
    return " ".join(dict_numbers[key] for key in sorted(dict_numbers.keys()))

print(order("is2 Thi1s T4est 3a"))

# Your task is to sort a given string. 
# Each word in the string will contain a single number. 
# This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. 
# The words in the input String will only contain valid consecutive numbers.

# Best Practices
# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))