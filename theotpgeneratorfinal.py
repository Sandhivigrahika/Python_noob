import random
import string

number = string.digits

def input_mobilenumber():
    while True:
     x =input("plz enter 10 digit mobile number")
     if x.isdigit and len(x) == 10:
         return x
     else:
        print('The number you entered does not have 10 digits. TRY AGAIN!')
def otp_generator():
    otp1 = ''.join(random.choice(number) for _ in range(0, 4))
    print(otp1)
    otp2 = str(input('enter the otp recieved'))
    while True:
        if otp1 == otp2:
            print('access granted ')
            return 'otp matched'
        else:
            print('access denied. please try again')
            break
input_mobilenumber()
otp_generator()
