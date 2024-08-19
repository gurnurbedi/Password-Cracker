# importing random
from random import*
def find_func():
    #from random import*
    #from random import*
    user_pass = input("Enter your password")

    listt=["pass@123", "password", "gurnur"]
    for i in listt:
        if(user_pass==i):
            print("got it",i)

        else:
            password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z']
            guess = ""
            while (guess != user_pass):
                guess = ""
                for letter in range(len(user_pass)):
                    guess_letter = password[randint(0, 25)]
                    guess = str(guess_letter) + str(guess)
                print(guess)
            print("Your password is",guess)

print(find_func())
