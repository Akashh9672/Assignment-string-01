from ctypes.wintypes import WORD
from pickle import TRUE
from re import I


statement=str(input("Please enter your statement:"))
print("statement:",statement)
list=[]
count=0
for i in statement:
       character=ord(i)
       list.append(character)
for n in list:
       if n<65 and n>32:
              count=1    
       else:
              count=2
if count==1:
       print("string is not accepted")                
if count==2:       
       print("string is accepted")