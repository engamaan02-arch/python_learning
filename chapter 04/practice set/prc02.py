marks=[]
f1 = int(input("enter marks of student 1 \n"))
marks.append(f1)
f2 = int(input("enter marks of student 2\n"))
marks.append(f2)
f3 = int(input("enter marks of student 3\n"))
marks.append(f3)
f4 = int(input("enter marks of student 4\n"))
marks.append(f4)
f5 = int(input("enter marks of student 5\n"))
# marks.insert(f5) eroor show hoga so we use
marks.append(f5)
marks.sort()
print(marks)