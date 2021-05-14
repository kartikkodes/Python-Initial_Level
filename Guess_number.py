import random
_number = random.randint(1,10)

def game():
    count = 5
    for i in range(5):
        user_number = int(input("Hello Player \nEnter any number: "))
        if user_number > _number:
            print("Your number is gretaer than the actual number")
            print("Chances left ",count-i-1)
        elif user_number < _number:
            print("Your number is less than the actual number")
            print("Chances left ",count-i-1)  
        else:
            print("Whoo hoo ! You won") 
            break;
        
    print("************************************************Game over")    

yes_or_no = input("Enter Y if you want to play the game")

if yes_or_no == "Y":
    game();
