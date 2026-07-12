s1 = int(input("enter marks in subject 01:\n")) 
s2 = int(input("enter marks in subject 02:\n")) 
s3 = int(input("enter marks in subject 03:\n")) 

s4 = (s1+s2+s3)/3.0

if(s1>33 and s2 >33 and s3>33 and s4>40):
    print("congrats you are passed with " ,s4,"%")
else:
    print("you are failed with " , s4 ,"%")

