f = open("file.txt")

print(f.read())

f.close()

'''this can be wriiten same by using
statement like this'''

with open("file.txt") as f:
    print(f.read())

'''now you dont have to close the file
automtic hojaiga close'''