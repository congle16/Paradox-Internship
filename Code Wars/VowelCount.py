def get_count(sentence):
    list_item_of_vowels = [item for item in sentence if item == 'a' or item == 'e' or item == 'i' or item == 'o' or item == 'u']
    return (len(list_item_of_vowels))
    pass

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# Best Practice
# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiou")
