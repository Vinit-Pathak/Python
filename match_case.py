# Match case is similar to switch case of other programming languages like c, c++,etc
# In match case we don't have to use break keyword

'''x = int(input("Enter the value of x : "))

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
'''

#write a python program to print table of a number which lies betwn 1 and 10
while (True):
    num = int(input("Enter a number from 1 to 10 : "))

    match num:
    
        case 1:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case 2:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case 3:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case 4:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case 5:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case 6:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case 7:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case 8:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case 9:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case 10:
            for i in range(1,11):
                print(f"{num}X{i} = {num*i}")
        case _:
                print("Enter a valid number")
                if num > 10:
                    break;