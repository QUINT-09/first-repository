""" import sys
import os
import subprocess """
import fetch
import store


cat = input("Enter cat.:")
what = input("Enter what:")
var = fetch.get_value(cat,what)

print(var)

#store.set_value("config","test",var)



""" ---------------------------------- """





#print(fetch.py data test)  
#exec(open("fetch.py").read())
""" variable1 = str(os.system('python fetch.py data test'))

print(variable1) """

#fetch(data,test) 



""" var = subprocess.call("python fetch.py data test")
print(var)
print(var) """
