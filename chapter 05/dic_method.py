marks = {
    "harry" : 100,
    "amaan" : 99,
    "uday" : 98
}
# print(marks.items())
# print(marks.keys())
#left side is keys 
#right sides is values 
print(marks.values())
# marks.update({"harry" : 97 , "viju" : 91})
# print(marks)
print(marks.get("harry"))
#this and this is not  same 
#bcz [] this can give error
#but  get fxn not give error
print(marks["harry"])