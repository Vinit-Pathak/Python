def checkPalindrome(number):
 palindrome=0
 while(number!=0):#120
  palindrome=(int(number%10))+palindrome*10
  number=number//10
 return palindrome

number=int(input("Enter a number : "))
if(number==checkPalindrome(number)):
 print(number,"is a palindrome ")
else:
 print(number,"is not a palindrome")