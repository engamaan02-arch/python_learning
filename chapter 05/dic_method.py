marks = {
    "harry" : 100, # {keys : value
    "amaan" : 99,  # keys : value
    "uday" : 98    # keys : value}
}
# print(marks.items())
print(marks.keys())
#left side is keys 
print(marks.values())
#right sides is values 
# marks.update({"harry" : 97 , "viju" : 91})
# print(marks)
print(marks.get("harry"))#---------|
#                                  |
#                                  |---#this and this is not  same 
#                                  |         |---#bcz [] this can give error 
print(marks["harry"])#-------------|#but  get fxn not give error  