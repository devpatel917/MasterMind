GamesWon=0 #Sets the initial amount of games won to 0. This is because I plan on creating the ability to play multiple games.
GamesLost=0 #Same purpose as above but setting the initial amount of games lost to 0
PlayerOneGamesWon=0 #purpose is to allow multiple games on two player (this is for the 1st player)
PlayerTwoGamesWon=0 # purpose is to allow multiple games on two player (this is for the 2nd player)
gameType=input("Do you want to play one player or two player. Type one or two")  #get user input to play one or two player, so I can use this information to differntiate what to do when it's two player and one player
#this function checks the user input. the reason that this function is present is because if the user doesn't make a proper input, then the game won't play and the program will result in an error. the function checks the length of the guess and the presecne of commas
def checkUserInput(userGuess,properInput):
    if len(userGuess) != 7 or userGuess[1] != "," or userGuess[3] != "," or userGuess[5] != ",":
        properInput = False
    return(properInput)
#function actually creates the computer guess. first, 4 random numbers are generated. Those 4 random numbers are are associated with a random position in the colors array. The 4 random colors are appended to another array (computer guess)
def createComputerGuess(computerGuess,colors):
 import random
 for z in range(0, 4):
     computerGuess.append(colors[random.randrange(0, len(colors))])
 return(computerGuess)
#calculates black pegs. for the same position, it compares every letter of the user guess to computer guess and if they are the same (in the same position), then it adds 1 black peg
def calculateBlackPegs(userGuess,computerGuess,blackPegs):
 for i in range(0, 4):

     if userGuess[i] == computerGuess[i]:
         blackPegs = blackPegs + 1
 return(blackPegs)
#for white pegs there are two criteria: that it is in both guesses and they are not in the same position, therefore, since there are only two options for each criteria, i used booleans
#i used a nested for loop to compare each letter of user guess to computer guess. if the letters do match, then the boolean is true otherwise it is already default to false
#because x and i are both positions, i used them to check if the letters are in the same position or not
#for duplicates, i knew that just doing the basic 2 criteria for white pegs wasn't going to give me purely white pegs, but rather white pegs that are double counting the black pegs as well.
#therefore, the logic was that a peg can either be a white peg or a black peg, so i differentiated between pure black pegs and pure white pegs
#the final if statement combines all the criteria for a truly pure white peg that works with duplicates. i then return the value
def calculateWhitePegs(userGuess,computerGuess,whitePegs):
 for x in range(0, len(userGuess)):
     InBothArrays = False

     NotInSamePosition = False
     for i in range(0, len(computerGuess)):
         if (userGuess[x] == computerGuess[i]):
             InBothArrays = True
         if x != i:
             NotInSamePosition = True

     BlackPeg = False
     if userGuess[x] == computerGuess[x]:
         BlackPeg = True
     if (InBothArrays == True and NotInSamePosition == True and BlackPeg == False):
         whitePegs = whitePegs + 1
 return(whitePegs)
#another method i could've used to calculate white pegs is that i could've only done white pegs and only done black pegs, then subtracted black pegs from white pegs
#that method would've been shorter in lines but this was my original idea, so i used this: the idea that if it's a white peg, it can't be black and if it's black, it can't be white

#this function allows to make changes according to easy, medium, or hard levels. if it's easy, then there is nothing to do, therefore, nothing is in this function for easy
#for medium and hard, more colors are added, so the computer has a wider range of colors to randomly select, making the game harder
#the amount played also increases per difficulty level
def AdjustmentsPerDifficultyAmountPlayed(difficulty,MaxAmountPlayed):
    if difficulty=="medium":
        MaxAmountPlayed=7
    if difficulty=="hard":
        MaxAmountPlayed=6
    return(MaxAmountPlayed)
def AdjustmentsPerDifficultyColors(difficulty,colors):
 if difficulty == "medium":
     colors.append("v")
     colors.append("i")

 if difficulty == "hard":
     colors.append("v")
     colors.append("i")
     colors.append("t")

 return(colors)
def MasterMind():
 global GamesLost
 global GamesWon
 global gameType
 global PlayerOneGamesWon
 global PlayerTwoGamesWon
 # I need to make these variables global in order to allow multiple games for the user to play, so i keep track of the games won throughout those multiple games
 bestScore=0 #this is necessary because i need to provide a starting point for this variable before i actually apply it within the next lines
 MaxAmountPlayed=8#this is the default for the easy level
 AmountPlayed = 0
 blackPegs = 0
 whitePegs = 0
 #above variables are self explanatory


 if gameType=="one":
     difficulty = input("What difficulty level do you want to play: Type easy, medium, or hard")#difficulty level
     colors = ["r", "g", "b", "y", "o", "p", "g", "m"] #the colors in which the computer picks in order to make the comp's guess or choice
     colors=AdjustmentsPerDifficultyColors(difficulty, colors)
     MaxAmountPlayed=AdjustmentsPerDifficultyAmountPlayed(difficulty,MaxAmountPlayed)
# t=turqois, i=indigo,v=violet
# r=red,g=green,b=blue,y=yellow,o=orange,p=purple,g=gray,m=magenta
 computerGuess = [] #initially starts out as blank but colors get appended. this is necessary because i can't just introduce a new array in a new function. it has to have a value before

 # rather than making an entire separate function or anothe part for two player which would be redundant because the comparision code and much of the code will be the same
 # in order to abstract that concept, i decided to merely create if statements into my already one player game but now thec omputer guess is player 1 choice and the user guess is player 2 guess
 if gameType=="one":
     print(createComputerGuess(computerGuess, colors))
 if gameType=="two":
     computerGuess=input("Player 1, type in a 4 color sequence separated by commas that you want player 2 to guess")

     computerGuess=computerGuess.split(",")
     #because in one player, the computer guess was already an array, i had to split this computer guess (player 1's choice) so that it will also become an array
 # the while loop plays the game until 8 rounds are done or when there are 4 black pegs
 hintChoice="no"
 #this is the default option that the user won't pick a hint. this is also necessary because i need to mention that variable because i apply it in the while loop
 while (blackPegs < 4 and AmountPlayed < MaxAmountPlayed):#this while loop allows the game to go on until either black pegs reaches 4 or max amount played is reached
     blackPegs = 0
     whitePegs = 0
     if gameType=="one":
         if hintChoice=="no": #this is from the previous round. if they decided to use a hint last time, they can't do it this time
             hintChoice = input("You get 1 hint per game, so use it carefully. Do you want a hint?Type yes or no")
             if (hintChoice == "yes"):
                 print("Your hint is that: ", computerGuess[3], "is a part of the answer")


         print(colors)
         userGuess = input(
             "What Guess would you like. You need to make 4 choices. Enter abbreviations and in commas. Choose between the above colors: ") #purpose of this to help the user out when picking the colors (giving them options)
     if gameType=="two":
         userGuess=input("player 2, what is your guess as to what the sequence is. sepearate your guess by commas")

     properInput=True #assumes that the user input is true and the next lines calls a function to check that
     checkUserInput(userGuess,properInput)



     while (checkUserInput(userGuess,properInput)==False): #this while loop only stops when the the user gives a correct input. this while loop because this section is also necessary in order to make sure that that inproper guess doesn't count as an attempt in the game
         userGuess=input("Type again. Make sure you type only 4 colors each seperated by 1 comma")
         checkUserInput(userGuess, properInput)





     userGuess = userGuess.split(",") #removes the commas and it becomes an array so that it is easier to compare to the computer guess
     AmountPlayed = AmountPlayed + 1 #adds one to each time you guess
     blackPegs=calculateBlackPegs(userGuess,computerGuess,blackPegs)
     print("Black Pegs: ", blackPegs)
     #this if statement calculates the best score. it compares the previous black pegs score to the best score, if it is greater, then it becomes the new best score
     if blackPegs>bestScore:
         bestScore = blackPegs

     print("White Pegs: ", calculateWhitePegs(userGuess, computerGuess, whitePegs))
     print("Best Score: ", bestScore)
     #two ways to decide the end of the game: either you get 4 black pegs or you play until you are out of attempts
     if blackPegs == 4:
         #differntiation between one player and two player(what to print)
         if gameType=="two":
             PlayerTwoGamesWon=PlayerTwoGamesWon+1 #keeps track of games won
             print("Player 1, you lost! Player 2, you won!")
             print("Player 1 Games Won: ",PlayerOneGamesWon)
             print("Player 2 Games Won: ",PlayerTwoGamesWon)

         if gameType=="one":
             GamesWon = GamesWon + 1 #keeps track of games won
             print("You Win! Games Won: ", GamesWon)
             print("Games Lost: ", GamesLost)

         choice=input("Do you want to play again? Type yes or no")
         if choice == "yes":
             MasterMind()
     if AmountPlayed == MaxAmountPlayed:
         print("The answer is: ", computerGuess)
         #differentiation between one player and two player (what to type when lost)
         if gameType=="two":
             PlayerOneGamesWon=PlayerOneGamesWon+1
             print("Player 1, you won! Player 2, you lost!")
             print("Player 1 Games Won: ", PlayerOneGamesWon)
             print("Player 2 Games Won: ", PlayerTwoGamesWon)
         #player 1 won 1 game, player 2 lost 1 game
         if gameType=="one":
             GamesLost = GamesLost + 1 #keeps track of games lost

             print("You Lose! Games Lost: ", GamesLost)
             print("Games Won: ", GamesWon)



         choice=input("Do you want to play again? Type yes or no")
         if choice=="yes":
             MasterMind() #calling the actual game to start but this is with all of the information like games lost and won
MasterMind() #calling the actual game to start (initial start)


