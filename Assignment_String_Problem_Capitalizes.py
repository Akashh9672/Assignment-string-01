
statement=str(input("Enter the statement:"))
statement=statement.title()
wordlist=statement.split(" ")
string=""
for i in wordlist:
    string = i[:-1]
    string = string + i[-1].upper() + " "
    print(string, end=" ")