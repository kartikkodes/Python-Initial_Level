import random
import time

def rps():
    for i in range(10):
        AI_one = random.choice(['Rock' , 'Paper' , 'Scissor'])
        AI_two = random.choice(['Rock' , 'Paper' , 'Scissor'])
        print("AI_one = ", AI_one)
        print("AI_two =  ", AI_two)
        print("And the result is: ")
        if AI_one == AI_two:
            print("Its a draw AI Assholes")
        elif AI_one == 'Rock' and AI_two == 'Scissor':
            print("AI_One wins and humanity loose")
        elif AI_one == 'Rock' and AI_two == 'Paper':
            print("AI_Two wins and humanity loose")        
        elif AI_one == 'Paper' and AI_two == 'Rock':    
            print("AI_One wins and humanity loose")
        elif AI_one == 'Paper' and AI_two == 'Scissor':    
            print("AI_Two wins and humanity loose")        
        elif AI_one == 'Scissor' and AI_two == 'Rock':    
            print("AI_Two wins and humanity loose")        
        elif AI_one == 'Scissor' and AI_two == 'Paper':    
            print("AI_One wins and humanity loose")
        print("*************************")        
        time.sleep(5)
    

rps();
