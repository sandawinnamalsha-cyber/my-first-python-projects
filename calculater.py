# addition
def add(a,b):
    return a+b 

# subtraction
def sub(a,b):
    return a-b

# multiplication
def mul(a,b):
    return a*b

# division
def div(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)

# power
def pow(a,b):
    return a ** b

# remainder
def remain(a,b):
    return a % b

while True:
    print('''Select operation.
    1.add : +
    2.subtract : -
    3.multiply : *
    4.division : /
    5.power : ^
    6.remainder : % ''')

    choice=input('Enter choice(+,-,*,/,^,%):')
    print(choice)

    while True:
        num1=input("Enter the first number:")
        try:
            num1=float(num1)
            break
        except:
            print("Not a valid number,please enter again")
            continue

    while True:
            num2=input("Enter the second number")
            try:
                num2=float(num2)
                break
            except:
                print("Not a valid number,please enter again")
                continue

    if choice=="+":
        print(num1,"+",num2,"=",add(num1,num2))

    elif choice=="-":
        print(num1, "-" ,num2, "=", sub(num1,num2))

    elif choice=="*":
            print(num1, "*",num2, "=", mul(num1,num2))
    elif choice=="/":
            print(num1, "/",num2, "=", div(num1,num2))

    elif choice=="^":
            print(num1, "^",num2, "=", pow(num1,num2))
    elif choice=="%":
            print(num1, "%",num2, "=", remain(num1,num2))

    else:
         print("Invalid operator,please try agan")
         continue
    ch=input("Do you want to calculate more?(y/n):")

    if ch=="y" or ch=="Y":
         continue
    else:
         print("Thank you for using our calculator")
         exit()
    

    

    
                        
                        
            
    

    


    