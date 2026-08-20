friend = ["apple" , "orange" , 5 , 345.06 , False , "amaan" , "uday"]
print(friend)
friend.append("viju")
#use for adding item in list in the end
print(friend)

l1 = [1, 23, 54, 12, 334,51, 66,23]
l1.sort()
#sort the list 
print(l1)
l1.reverse()
#reverse the list
print(l1)
l1.insert(4 , 4345)
#phele index fir number jo insert karna h 
#jis number pe insert krna h voh phele 
#or jo likhna  h fir usko likho 
print(l1)
l1.pop(3)#uss  index ko nikal dega
#jis index value ko likhounga voh nikal jaigi list se
print(l1)
print(l1.pop(3))# pop index  ko print karega
l1.remove(334)
#yeh remove krdega uss value ko jo bi (xyz) dalogai
print(l1)
