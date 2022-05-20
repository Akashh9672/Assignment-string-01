statement=str(input("Plear enter your statement:"))
count=0
for i in statement: 
    if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u" :  
        count+=1
print("Your statement:",statement)    
print("Vowels:",count)               