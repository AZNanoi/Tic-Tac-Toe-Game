# -*- coding: utf-8 -*-
import tictactoe_functions
import random

def createGamePlan(size, sign):
  gPlan = []
  for i in range(size):
    row = [sign]*size
    gPlan.append(row)
  return gPlan


def showGamePlan(gamePlan):
  i = 0
  numbers=list(range(0,len(gamePlan)))
  rowNr = [" "]+numbers
  for row in [numbers]+gamePlan:
    print(rowNr[i],end = " ")
    i += 1
    for cell in row:
      print(cell, end = " ")
    print()


def updateGamePlan(row,col,gamePlan,sign):
  gamePlan[row][col]=sign
  return gamePlan

def anyVacantBoxes(gamePlan,EMPTY):
  if EMPTY in gamePlan[0]:
    return True
  return False


def humanSelectABox(sign):
  print("\n---Din tur ("+sign+")---")
  row = int(input("Ange raden:"))
  col = int(input("Ange columnen:"))
  return row,col



def play2win(gamePlan, sign, message,EMPTY,WINROW):
  if sign == HUMAN:
    row,col = humanSelectABox(sign)
  else:
    row,col = tictactoe_functions.computerSelectABox(gamePlan,sign,EMPTY)

  print(updateGamePlan(row,col,gamePlan,sign))
  showGamePlan(updateGamePlan(row,col,gamePlan,sign))
  #if not anyVacantBoxes(gamePlan,EMPTY):
    #print("No winner!")
    #return True
  if(tictactoe_functions.lookForWinner(gamePlan,row,col,WINROW)):
    print(message)
    return True
  return False


if __name__ == "__main__":
  WINROW = 3
  SIZE = 3
  EMPTY = '-'
  HUMAN = 'X'
  COMPUTER = 'O'
  playersInfo = ((HUMAN,"\n****** You won! ******\n"), (COMPUTER, "\n****** Computer won! ******\n"))
  playerIndx = random.choice([0,1])
  gamePlan = createGamePlan(SIZE, EMPTY)
  print(gamePlan)
  showGamePlan(gamePlan)
  gameFinished = False
  while not gameFinished:
    gameFinished = play2win(gamePlan, playersInfo[playerIndx][0], playersInfo[playerIndx][1], EMPTY,WINROW)
    
    if playerIndx == 0:
      playerIndx = 1
    else:
      playerIndx = 0
