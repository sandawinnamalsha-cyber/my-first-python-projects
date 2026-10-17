import numpy as np
Number=np.random.randint(1,100)
count=0
while(True):
    Gues_number=float(input("Gues a number"))
           
    
    
    try:
        number=float(Gues_number)
        count+=1
    
        if(Number<Gues_number):
           print("Too High!")
        elif(Number>Gues_number):
           print("Too Low!")
        elif(Number==Gues_number):
           print("Correct! You won in", count,"tries")
           break
    except ValueError:
       print("done")

     

        

               




