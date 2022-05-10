def high_and_low(numbers):
    numbers = [int(item) for item in numbers.split()]
    return (str(max(numbers)) + " " + str(min(numbers)))
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Best Practice
# def high_and_low(numbers): 
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))