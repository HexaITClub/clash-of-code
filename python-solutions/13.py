# Write a function to split string by spaces and print each word in new line. If the given string is empty, print "[empty]". 

def stringTowords(string):
    if string.strip() == "":
        print("[empty]")
    else:
        words = string.split()
        for word in words:
            print(word)
                 
stringTowords("This is String")
           