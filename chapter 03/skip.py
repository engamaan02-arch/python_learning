word = "amazing"
print(word[1:6:2])
#jumping of 2 last digit jump decide krta skip krvata h. 
#print(word[starting include rehti h 
#:kaha tak select krna  but exclude rehti h :
#  kitna skip karna hai ])
print(word[-1:-6:-1])
#negative slicing me skip krte waqt mag kam se zyada likhte hai 
#lower mag :heigher mag 
#but negative slicing me higher to lower maghai jab skip nhi krre 
print(word[:6:2])
print(word[:6:3])
print(word[::3])
print(word[::])