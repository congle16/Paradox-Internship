def is_isogram(string):
    string = string.lower()
    list_of_letters = [item for item in string if string.count(item) == 1]
    return True if len(list_of_letters) == len(string) else False

print(is_isogram("Dermatoglyphics"))
print(is_isogram("aAbg"))
print(is_isogram("aaa"))

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.


# Best Practice
# def is_isogram(string):
#     return len(string) == len(set(string.lower()))