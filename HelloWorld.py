def myFun(x):
    x[0] = 'Hello'
    
def myFun1(x):
    x = ['hello', 'world']
    
lst = [10, 11, 12, 13, 14, 15]

myFun1(lst) # -> ['Hello', 11, 12, 13, 14, 15]
# myFun(lst) # -> [10, 11, 12, 13, 14, 15]
print(lst)

def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
        
myFun(first ='Geeks', mid ='for', last='Geeks')   
