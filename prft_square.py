#write a porgram to find whether an inputted number is perfect square or not

from cmath import sqrt
import math
number=int(input("Enter a number\n"))
stringNumber=str(number)
if(str(math.sqrt(number)).endswith(".0")):
 print(number,"is perfect number")
else:
 print(number,"is not perfect number")