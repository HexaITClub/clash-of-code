# Write a program to find the sum of all elements in an array except for the largest and smallest elements.
lst = []
n = int(input("Enter the total elements you want inside your list? "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)
sum = 0
i = 0
while i<len(lst):
    sum = sum+lst[i]
    i = i+1

print(sum)