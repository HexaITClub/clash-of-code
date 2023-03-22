# Write a program to find the second most frequent character in a given string.

str = input("Enter String: ")
l = list(str)
freq = [l.count (ele) for ele in l]
d = dict(zip(l,freq))
print(d)
