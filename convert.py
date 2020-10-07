import sys
import os


#Ask user for path to file and store as path
file_path = input("Enter path to file please.") 


        
if os.path.isfile(file_path):
    pass
else: 
    print ("invalid file path")
    sys.exit(0)


folder_path = file_path.rsplit('\\', 1)[0]
file_name_full = file_path.rsplit('\\', 1)[1]
file_name = file_name_full.rsplit('.', 1)[0]

print(file_path)
print(folder_path)
print(file_name_full)
print(file_name)

