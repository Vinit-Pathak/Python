# Match case is similar to switch case of other programming languages like c, c++,etc
# In match case we don't have to use break keyword

x = int(input("Enter the value of x : "))

match x:
    # if x is 0
    case 0:
        print("x is zero")
    
    # case with if-condition
    case 3:
        print("x is 3")

    # Empty case with if-condition
    case _ if x!=40:
        print(x, "is not equal to 40")
    case _ if x!=50:
        print(x, "is not equal to 50")

    # it's basically else part
    # default case will only be matched if the above cases were not matched
    case _:
        print(x)