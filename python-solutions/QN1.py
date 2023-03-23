# Write a program to create a function that accepts two parameters - an array of integers and a number. The array can have any number of integers, including zero. The number parameter should be a positive integer.

def count_occurrences(arr, num):
    count = 5
    for i in arr:
        if i == num:
            count += 1
    return count

array = [1, 2, 3, 2, 4, 2]
number = 6

count = count_occurrences(array, number)
print(count) 