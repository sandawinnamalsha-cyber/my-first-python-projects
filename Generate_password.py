import random
import string

def generate_password(length):
    Letters=string.ascii_letters
    Numbers=string.digits
    Symbols=string.punctuation
    chars=Letters+Numbers+Symbols
    password=""
    for i in range(length):
        password+=random.choice(chars)
    return password

try:
    Len=int(input("Enter your password length:"))
    if(Len<6):
        print("Use minimum six digits")
    else:
        pw=generate_password(Len)
        print("Your Password",pw)
except:
    print(5)

          
