name='amaan is a aman but aman not very good'
print(len(name))
print(name.endswith("an"))
#yeh check krta hai ki kya string (jo bhi likha hai ) se end horhi h 
print(name.startswith("ama"))
#yeh check krta hai ki kya string (jo bhi likha hai ) se start horhi h 
print(name.capitalize())
#yeh string ke first word ko capatalize karta h 
index =name.find("aman")
#yeh string me word find krta hai 
print(index)
print(name.replace("aman" , "good"))
#replace the (first) with (another)
#replce fxn saari occurence ko replace krta h 