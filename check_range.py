import random

x = random.randint(0,2000)

if x <= 100:
    print("Within 100")
elif x > 100 and x <= 1000:
    print("Within 1000")    
else:
    print("Greater than 1000")    

print(x)
