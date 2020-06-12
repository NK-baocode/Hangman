'''
lilbaoboy 6/10/2020

Hangman
Code will pick a random word from a list of words, then present user with blanks for each letter, and a text drawing of a classic hangman. User will enter a single letter, and if it matches, blanks will replace with correct letter in correct places. if it does not, wrong letter will appear along with updated drawing, when drawing completes (6 wrong guesses), code displays full drawing and you lose. if all blanks are filled, code displays full word and you win. 
'''
# import packages
import random as rd
import numpy as np

# open sowpods file and convert to a list (note sowpods has 178691 entries total)
sowpods = open('SOWPODS.TXT', "r")
words = list(sowpods)

# pick random integer to out of possible 178691 entries, then index out of sowpods
wordnum = rd.randint(0,178691)
secretword = words[wordnum]

# our secret word has been selected!

#create an array of strings to represent the blank hangman 
hangman = np.array([["   __    "], ["  |  '   "], ["  |     "], ["  |     "]], dtype=str)

# hangman array will be indexed with new text drawings after each failed attempt

#print the blank hangman
print(hangman)

'''
create a list to be filled with blanks, a system must be created which can read each letter and print a blank for each one

send each letter in the secret word to a list, each letter the user inputs will be checked against that list
'''
# the secret word length is really one lower than python value (python starts count at 0)
secretlen = len(secretword) - 1


blanks = []
for i in range(secretlen): #read each letter and make blank for each
  blanks.append('_')

#print blanks for user under the hangman
print(blanks)

secretlist = []
for i in range(secretlen): # add each letter of secret word to new secret list
  secretlist.append(secretword[i])

# create another list to store previous guesses
usedlet = []
# create a function to ask a letter than check if letter is correct

def ask():
  global usedlet
  global inputlet
  global isright # trigger for if the letter is correct or not
  isright = False
  #create a while loop to validate inputs
  while True:
    inputlet = str(input('Enter a letter:\n')) # create an input for user to enter a letter
    if usedlet.count(inputlet) != 0: # if the letter is used, restart ask loop
      print("You have already entered that letter!")
      continue
    else: # if letter hasn't been used, end loop and continue
      usedlet.append(inputlet)
      break

  for i in range(secretlen): # go through blanks and replace blanks where letter is correct
    if secretlist[i] == inputlet:
      blanks[i] = inputlet
      isright = True # if there is a correct letter, answer is right

# create a list to store failed guesses to display to player

wronglet = [] 

# create checks for each failed attempt, on startup these would all be False
fail1 = False
fail2 = False
fail3 = False
fail4 = False
fail5 = False

gameover = False # check to see if player has lost

#  function to check if the letter is right, if wrong, if else tree for appropriate response
# if failed, update hangman drawing and add letter to incorrect list, then display both to player
def check():
  global inputlet
  global isright
  global fail1
  global fail2
  global fail3
  global fail4
  global fail5
  global wronglet
  global gameover
  if isright == True:
    print(blanks)
  else:
    if fail1 == True:
      if fail2 == True:
        if fail3 == True:
          if fail4 == True:
            if fail5 == True:
              hangman[3] = ["  | ( )  "]
              wronglet.append(inputlet)
              print(f"Incorrect: {wronglet}")
              print(hangman)
              print(blanks)
              print(f"You fail! :(\nYour word was {secretword}")
              gameover = True
            else:
              hangman[3] = ["  | (   "]
              fail5 = True
              wronglet.append(inputlet)
              print(f"Incorrect: {wronglet}")
              print(hangman)
              print(blanks)
          else:
            hangman[2] = [(r"  | (|)  ]")]
            fail4 = True
            wronglet.append(inputlet)
            print(f"Incorrect: {wronglet}")
            print(hangman)
            print(blanks)
        else:
          hangman[2] = ["  | (|   "]
          fail3 = True
          wronglet.append(inputlet)
          print(f"Incorrect: {wronglet}")
          print(hangman)
          print(blanks)
      else:
        hangman[2] = ["  |  |   "]
        fail2 = True
        wronglet.append(inputlet)
        print(f"Incorrect: {wronglet}")
        print(hangman)
        print(blanks)
    else:
      hangman[1] = ["  |  ò   "]
      fail1 = True
      wronglet.append(inputlet)
      print(f"Incorrect: {wronglet}")
      print(hangman)
      print(blanks)
    
# main engine of game, ask then check until no more blanks or player loses
while blanks.count('_') != 0 and gameover == False: 
  ask()
  check()

# when this loop ends, game is over
if gameover == False: # check if player has lost, if not, they won
  print(wronglet)
  print(hangman)
  print(blanks)
  print(f'You win! Your word was {secretword}')
      
  
  



