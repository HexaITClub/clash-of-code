# Write a program that reads in a text file and finds the longest word in that file.

n = int(input("Enter the value of N: "))

f = open("bb.txt","r")
s = f.read()
lst = s.split()

for i in lst:
    if(len(i)>n):
        print(i)
