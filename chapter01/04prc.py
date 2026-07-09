import os
#specify the directory you want to list
directory_path = '/'
#list all files and directory in the specified path
contents = os.listdir(directory_path)
#print each files and directory name
for item in contents:
    print(item)