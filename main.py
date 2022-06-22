#  Random Project 21/06/2022
'''
NOTE1:
  
I STILL HAVE TO DO ERROR HANDLING TO ENSURE MOST OF THE BASIC ERRORS ARE HANDLED WITHOUT BREAKING THE CODE. USER INPUT, INFORMATION INCORRECT AND LOGISTIC PROBLEMS.

NOTE2:
  
Error handling still missing for half of the code, threading amd logging modules are to be prepared before joining the networking project. Server is already finished and is awaiting for testing. 21/06/22 by Theo
'''

from time import sleep # sleep function
from  random import randrange # randint functions

import asyncio

modes = {'easy':10, 'hard':50, 'hardcore':100}
lifes = 5

gameRules = """
Level Easy: range 1 to 10,
Level Hard: range 1 to 50,
Level Hardcore: range 1 to 100.

Rules:
  
Enter a guess (numbers only) if you enter anything other than a number, you'll be warned and then will be lost one life after until the game terminates. Should you like to quit the game, enter -1. 

Good Luck!
"""

class Error(Exception):
  def __init__(self, choice, message='Incorrect Choice! Game ended.'):
    self.choice = choice
    self.message = message
    
    super().__init__(self.message)
    
  def __str__(self):
    return f'{self.choice} -> {self.message}'


def welcome():
  print(103 * "-")
  sleep(1)
  print('Welcome to my game!')
  sleep(1)
  print(gameRules)
  print(103 * "-")


def generateRandom(ran):
  radnum = randrange(1, ran)
  return radnum


def verifyGuess(number):
  global lifes
  while lifes:
    try:
      guess = int(input('Enter your guess: '))
      if guess == number:
        print("Congratulations you have won the game!")
        break
     
      elif guess == -1:
        print('Oops you have ended the game!')
        break
      
      elif guess > number:
        print('Your guess is too high! Try lower.')
        lifes -= 1
      
      elif guess < number:
        print('Your guess is too low!, Try higher.')
        lifes -= 1
          
    except ValueError:
      print('Enter a number for a valid guess, you have lost a life now!')
      lifes -= 1
      
  if lifes <= 0:
    print("You don't have anymore lifes! You lost!")


# Flow Control
def main():
  welcome()
  try:
    u_in = input('Enter Level of difficulty: ')
    mode = modes[u_in]
    randNum = generateRandom(mode)
    print(f'You have selected: {u_in} mode!')
    
  except Exception:
    raise Error(u_in)
  
  verifyGuess(randNum)
  
# Runs the code
if __name__ == '__main__':
  main()