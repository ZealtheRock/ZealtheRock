import os

if os.path.isfile("file.txt"):
    f = open("file.txt","w")
    i=input()
    f.write(i)
    f.close()
else:
    print("File does not exist")