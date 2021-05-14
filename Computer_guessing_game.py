import random

def comp_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != 'c':
        comp_guess = random.randint(low ,high)
        print(comp_guess)
        feedback = input("Was it low(l) , high(h) or correct(c)?")
        if feedback == 'h':  #The number is lower than that
            high = comp_guess - 1 
        elif feedback =='l': #That means number is higher than that
            low = comp_guess + 1
    print("AI fucked your shitty game!")


z = int(input("Enter the higher limit you want for your game: "))
comp_guess(z);  
