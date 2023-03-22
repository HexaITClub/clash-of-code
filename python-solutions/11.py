# 11) Write a function that accepts a string as input and calculate the length of given string. If the given string is NULL 
#    your function should return -1. Otherewise, it should return length of the string. Hint: Use loops.


def StringLength(a):
    if(a == ""):
        print("Empty")
        return -1
    else:
        print(a," StringLenght  is   :",len(a))

StringLength("")