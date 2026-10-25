class employee:
    company = "microsoft"
    salary = "120000"    # these three are class atributes
    language  = "python"

amaan = employee()
amaan.name = "amaan"
amaan.language= "java" #this will overwrite on class 
print( amaan.name ,amaan.company , amaan.salary , amaan.language)