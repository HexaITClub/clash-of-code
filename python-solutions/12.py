# #  Write a program to calculate product of two floating point numbers using loop.

num1 =21
num2 = 30
product = 0
#  range(1,num2+1)
for i in range(num2):
    product=product+num1
print("The product of two number:", product)

# in Function
def twoNumberProduct(a,b):
    p =0
    for i in range(1,b+1):
        p =p+a
    print("Product no :", p)  

twoNumberProduct(2,3)