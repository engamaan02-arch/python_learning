name='amaan is a aman but aman not very good'
print(len(name))
print(name.endswith("an"))
#yeh check krta hai ki kya string (jo bhi likha hai ) se end horhi h 
print(name.startswith("ama"))
#yeh check krta hai ki kya string (jo bhi likha hai ) se start horhi h 
print(name.capitalize())
#yeh string ke first word ko capatalize karta h 
index =name.find("aman")
#if i want  ki a find ho lekin dusra a find krna hai toh 
a =print(name.find("a")) #isse phela a find hoga string ka 
print(name.find("a" +1)) #isme +1 lagadoya toh dusra a string a find hoga bas aise hi carry on
#yeh string me word find krta hai 
print(index)
print(name.replace("aman" , "good"))
#replace the (first) with (another)
#replce fxn saari occurence ko replace krta h 