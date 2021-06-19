import random 
def main():
    player1 = 0
    player2 = 0
    global count1  
    global count2 
    count1=0
    count2=0

    for i in range(1,4):
      var = input("Enter 'y' if you want to roll the dice ptherwise enter 'n' ")
      player1 = (random.randint(1,6))
      player2 = (random.randint(1,6))
      print(player1)
      print(player2)

      if player1 > player2:
        print("Player 1 wins")
        count1 = count1+1
      elif player2 > player1:
        print("Player 2 wins")
        count2 = count2 + 1
      else:
        print("DRAW")  
      print("Score after round ",i," is :")   
      print("Player 1 ",count1)  
      print("Player 2 ",count2)  
main()
print("Final score is :")
print("Player 1 ",count1)
print("Player 2 ",count2)
