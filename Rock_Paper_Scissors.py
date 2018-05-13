import random
import sys

def Computers_Play():
    com = random.randint(1,3)

    if com == 1:
        return "rock"
    elif com == 2:
        return "paper"
    elif com == 3:
        return "scissors"

def Players_Play():
    print(" ")
    play = input("What will you do, Rock, Paper, or Scissors?: ")

    if len(play) < 1:
      print("Not a valid input.")
      print(" ")
      return False
      
    
    if len(play) >= 1:
      if play.lower() == "rock" or play.lower() == "r":
          print(u"\u270A") #rock
          print(u"\u270B") #paper
          print(u"\u270C") #scissors
          return "rock"
      elif play.lower() == "paper" or play.lower() == "p":
          print(u"\u270A") #rock
          print(u"\u270B") #paper
          print(u"\u270C") #scissors
          return "paper"
      elif play.lower() == "scissors" or play.lower() == "s":
          print(u"\u270A") #rock
          print(u"\u270B") #paper
          print(u"\u270C") #scissors
          return "scissors"
      else:
        print("Not a valid input.")
        print(" ")
        return False
        
    

print("We are going to play Rock, Paper, Scissors!")

userwins = 0
compwins = 0
ties = 0

def Main():

  while True:
    ComP = Computers_Play()
    PlayP = Players_Play()
    global userwins
    global compwins
    global ties

    def score():
            print(" ")
            print("Score:")
            print("User:", userwins, "Computer:", compwins, "Ties:", ties)
            print(" ")

    if PlayP == ComP:
        print("It's a Tie!")
        ties = ties+1
        score()
        
    elif PlayP == "rock" and ComP == "scissors":
       print("You used", u"\u270A", " You Win!")
       userwins= userwins+ 1
       score()
    elif PlayP == "rock" and ComP == "paper":
       print("You used", u"\u270A", " You Lose.")
       compwins = compwins + 1
       score()

    elif PlayP == "paper" and ComP == "rock":
       print("You used", u"\u270B", " You Win!")
       userwins= userwins+ 1
       score()
    elif PlayP == "paper" and ComP == "scissors":
       print("You used", u"\u270B", " You Lose.")
       compwins = compwins + 1
       score()

    elif PlayP == "scissors" and ComP == "paper":
       print("You used", u"\u270C", " You Win!")
       userwins= userwins+ 1
       score()
    elif PlayP == "scissors" and ComP == "rock":
       print("You used", u"\u270C", " You Lose.")
       compwins = compwins + 1
       score()

    print("Do you want to play again?")

    global again
    again = input("Yes/No: ")   
    while again.lower() not in ("yes", "y", "no", "n"):
        print(" ")
        print("Not a valid input.")
        print("Do you want to play again?")
        again = input("Yes/No: ")
        if again.lower() == "no" or again.lower() == "n":
            print(" ")
            again = "no"
            sys.exit()
    if again.lower() == "no" or again.lower() == "n":
        print(" ")
        sys.exit()

    Main()
Main()
       
