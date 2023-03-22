# Read a text file and count the frequency of letter "the".
# re Constraints: Create a text file yourself containing some English sentences.
#  File name should be "coc.txt". It can contain any, and any number of sentences.
 
with open("coc.txt", "r") as file:
    file = open("coc.txt", "r")
    data = file.read()
    words = data.split(" ") 
    count = 0
    for word in words:
        if(word == "the"):
            count = count+1
    print( "Total No of The in txt File :", count)
