import numpy as np
No1=np.random.randint(0,10)
No2=np.random.randint(0,10)
No3=np.random.randint(0,10)
No4=np.random.randint(0,10)
Number=No1,No2,No3,No4
count=0
print('start')
while(True):
    
    try:
        Gues_number1, Gues_number2, Gues_number3, Gues_number4=input("Enter 4 numbers:").split()
       
        number1=float(Gues_number1)
        number2=float(Gues_number2)
        number3=float(Gues_number3)
        number4=float(Gues_number4)
        count=count+1
        if(No1==number1):
            print("Your First Number is correct")
        if(No2==number2):
            print("Your second Number is correct")
        if(No3==number3):
            print("Your Third Number is correct")
        if(No4==number4):
            print("Your Fourth Number is correct")
        if(No1==number1 and No2==number2 and No3==number3 and No4==number4):
            print("You won!!!""You win",count,"tries")
            break
    except ValueError:
        pass
