#function
def gd(name , ending):
    print("good day ," + name )
    print(ending)
''' or jo humne gd ke andar name 
and ending likha h 
vhi argument h '''
a1 =gd("amaan" , "thankyou")
print(a1)

#agar abhi me isko koi varaible ke equal krounga toh kuch nhi dega
''' but me isme 
aagar fxn me return daldounga
toh voh return hojaiga varaible me'''
def gt(name , ending):
    print("good day ," + name )
    print(ending)
    return "okh"
''' return me jo likhounga voh return
hojaiga '''

a = gt("amaan" , "thankyou")
print(a)
