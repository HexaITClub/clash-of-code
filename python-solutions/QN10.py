# Write a function that accepts a string as input and calculate the length of given string. If the given string is NULL

def Week(number): 
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] 
    if number < 0:
        return days[0]
    elif number > 7:
        return days[6]
    else:
        return days[number]

numberDay = 3
totaldays = Week(numberDay)
print(totaldays) 

number = -1
days = Week(number)
print(days) 

num = 10
days = Week(num)
print(days) 

