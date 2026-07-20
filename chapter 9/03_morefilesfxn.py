f = open("file.txt")

# lines = f.readlines()
# print(lines , type(lines))
#line by line
# line1 = f.readline()
# print(line1 , type(line1))
# line2 = f.readline()
# print(line2 , type(line2))
# line34 = f.readline()
# print(line34 , type(line34))
# line4= f.readline()
# print(line4 , type(line4))
# line5 = f.readline()
# print(line5 , type(line5))


#by loops
line = f.readline()
while(line!= ""):
    print(line)
    line = f.readline()


f.close()



