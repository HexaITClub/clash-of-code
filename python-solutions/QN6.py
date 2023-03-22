# Write a program to find the sum of all elements in an array that are not divisible by 3 or 7

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


sum = 0

for element in array:
    if element % 3 != 0 and element % 7 != 0:
        sum += element
print("The sum of elements in the array that are not divisible by 3 or 7 is:", sum)
