#####################################################################################################################################################################
# In this assignment you will write a Python program that is a continuation of the previous Dice program.  This program will simulate a game of Craps.              #
# It will roll the pair of dice three times. It will keep score for the “house” (the computer), and for the player.                                                 #
# It will then display these scores each time the dice are rolled based on the rules listed below. It will lastly display a final winner at the end of the game.    #
#                                                                                                                                                                   #
# Rules of the game (and the program):                                                                                                                              #
#                                                                                                                                                                   #
# Player and “house” start with a score of 0 before the first roll.  Scores for both are accumulated through the number of rolls (1,2, and 3).                      #
# For each roll of the 2 dice: NOTE – this does not require a loop as we have not covered this, but you may use loops if you have moved ahead and mastered them.    #
# If the sum of the dice is 7 or 11, display “CRAPS” and increment “house score by 2”.                                                                              #
# If the dice are the same value (doubles) and the values are even, increment the player score by 2                                                                 #
# (NOTE – you should use the modulo operator with an operand of 2 for determining whether the value is even).                                                       #
# If the dice are the same value (doubles) and the values are odd, increment the “house” score by 2.                                                                #
# If not CRAPS or doubles, and the total is less than 7, houseScore = houseScore +2.                                                                                #
# If not CRAPS or doubles, and the total is greater than 7, playerScore = playerScore + 2.                                                                          #
# Determine the winner and display the results (with 3 rolls, there cannot be a tie!).                                                                              #
# Be sure to use comments for both structure of the program and documentation of the code.                                                                          #
# All code must completely be your own individual work product.                                                                                                     #
#####################################################################################################################################################################

import random                                                                                           # Import the random module

                ### We are just declaring variables here so we can quickly reference them later ###
choice = 'yes'                                                                                          # Declare choice as a variable and assign it 'yes'
playerScore = 0                                                                                         # Declare playerScore as a variable and assign it 0
houseScore = 0                                                                                          # Declare houseScore as a variable and assign it 0
dice1 = 0                                                                                               # Declare dice1 as a variable and assign it 0
dice2 = 0                                                                                               # Declare dice2 as a variable and assign it 0
diceTotal = 0                                                                                           # Declare diceTotal and assign it 0

def displayDice(dice):                                                         # This will return a picture of a dice
    if dice == 1:
        dice ="""*-------*"
|       |
|   *   |
|       |
*-------*"""
    elif dice == 2:
        dice ="""*-------*
| *     |
|       |
|     * |
*-------*"""
    elif dice == 3:
        dice ="""*-------*
| *     |
|   *   |
|     * |
*-------*"""
    elif dice == 4:
        dice ="""*-------*
| *   * |
|       |
| *   * |
*-------*"""
    elif dice == 5:
        dice ="""*-------*
| *   * |
|   *   |
| *   * |
*-------*"""
    elif dice == 6:
        dice ="""*-------*
| *   * |
| *   * |
| *   * |
*-------*"""
        
    return(dice)

choice = input('Would you like to play dice? \n')                                                       # Assign the choice variable as player input
while choice.casefold().startswith('y'):                                                                # create loop that begins if player says something that starts with y
    playerScore = 0                                                                                     # reset player score to 0 every time we would like to play again
    houseScore = 0                                                                                      # reset house score to 0 every time we would like to play again
    for rollNumber in range(1, 3 +1, 1):                                                                # create loop that will run 3 times (1 per roll of the dice) and go up by 1 each pass
        input('Press Enter to roll.')
        dice1 = random.randint(1, 6)                                                                    # assign dice1 a random interger between 1 and 6
        dice2 = random.randint(1, 6)                                                                    # assign dice2 a random interger between 1 and 6
        diceTotal = dice1 + dice2                                                                       # assign diceTotal the sum of dice1 and dice2
        print('Roll Number: ', rollNumber)                                                              # output the count of the for loop, to let user know how many rolls they have remaining
        print('Dice:', dice1,'Dice:' , dice2)                                                           # output the assigned numbers to the dice1 and dice2 variables
        print(displayDice(dice1),'\n' , displayDice(dice2))
        print('The sum of the rolls was', diceTotal)                                                    # output the sum of dice1 and dice2
        if (diceTotal == 7) or (diceTotal == 11):                                                       # if dice is equal to 7 or 11
            print("CRAPS")                                                                              # output CRAPS
            houseScore = houseScore + 2                                                                 # assign houseScore 2 points for the first roll and 2 more for every round this is true
            print('House gets 2 points', '\n', sep='')                                                  # let the user know that the house got 2 points
        elif (dice1 == dice2) and (dice1 %2==0):                                                        # if dice1 is equal to dice2 and it is even
            playerScore = playerScore + 2                                                               # assign playerScore 2 points for the first roll and 2 more for every round this is true
            print('Doubles and Even \n','Player gets 2 points', '\n', sep='')                           # let user know that they get 2 points and the conditions that dictated their vicrory
        elif (dice1 == dice2) and (dice1 %2==1):                                                        # if dice1 is equal to dice2 and it is odd
            houseScore = houseScore + 2                                                                 # assign houseScore 2 points for the first roll and 2 more for every round this is true
            print('Doubles and Odd \n','House gets 2 points', '\n', sep='')                             # let user know that the house gets 2 points and the conditions that dictated their loss
        elif (diceTotal < 7):                                                                           # if diceTotal is less than 7
            houseScore = houseScore + 2                                                                 # assign houseScore 2 points for the first roll and 2 more every round this is true
            print('Less than 7 \n','House gets 2 points', '\n', sep='')                                 # let user know that house won and the conditions that dictated the users loss
        elif (diceTotal > 7):                                                                           # if diceTotal is greater than 7
            playerScore = playerScore + 2                                                               # assign playerScore 2 points for the first roll and 2 more every round this is true
            print('Greater than 7 \n','Player gets 2 points', '\n', sep='')                             # let user know they won and the conditions that dictated their victory
        
    if (playerScore > houseScore):                                                                      # if playerScore is greater than houseScore
        print('Player Wins!\n','Player Score:', playerScore,' House Score:',houseScore ,'\n', sep='')   # let user know they won and what the point totals were
    else:                                                                                               # otherwise
        print('House Wins!\n','Player Score:', playerScore,' House Score:',houseScore ,'\n', sep='')    # let user know they lost and what the point totals were
    choice = input('Would you like to play again? \n')                                                  # let user decide if they want to play again and go back to start of the loop
               
print("Thank you for playing!")                                                                         # Thank the player for playing when they no longer want to play
