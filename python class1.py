intro=input("Enter your introduction")
print(intro)
charcount=0
wordcount=1
for i in intro:
    charcount=charcount+1
    if(i==" "):
        wordcount=wordcount+1
print("NO.OF Words in the string:")
print(wordcount)
print("NO.OF Characters in the string:")
print(charcount)         