# Strings are immutable

a = "vinit"
b = "PATHAK!!!!!!!!!"
c = "?????? Vinit ??????"
print(len(a))
print(a.upper())
print(b.lower())
print(b.rstrip("!"))  #it will remove the given character(tailing character - ending character)
print(a.replace("vinit","sarang"))
print(c.split(" ")) #it will split the sentence and displayed in list

str = "Welcome to the console !!!"
print(str.endswith("!!!"))  #it will return the output in boolean datatype

str = "Welcome to the console !!!"
print(str.endswith("to",4,10))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())  #it will return boolean datatype