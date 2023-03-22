#  Prints the numbers from 1 to 100. But for multiples of three print "Patan" instead of the number and for 
# the multiples of five print "Campus".For numbers that are multiples of both three and five print "BCA".
for i in range(11):
    if(i %3 ==0  and i % 5 ==0):
        print("BCA")
    elif(i%3 ==0):
        print("Patan")   
    elif i%5==0 :
        print("Campus")  
    else:
        print(i)   
   



  