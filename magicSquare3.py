from time import sleep
from math import sqrt
import argparse
import os.path
#time so that it doesnt appear at once
#math for sqrt function to determine the size quickly

##############################
# Author: Ian Schwartz
# Created: 10/7/2020
# Last Update: 10/9/2020
##############################

#prints out the square to stdoutput
#  requires sizeSquare: size of the square, square: the list holding the square
def printSquare(sizeSquare, square):
  for i in range(len(square)):
    print(f"{square[i]:{len(str(len(square)))}}", end=" ")
    if i % sizeSquare == (sizeSquare-1):
      print('')
  print('')


#function to find the magic number
#  requires sizeSquare: size of the square
#  returns the magic number value
def magicNum(sizeSquare):
  return int(sizeSquare * (((sizeSquare*sizeSquare)+1) / 2.0))


#check for one zero function, will return list of all indexes with only one zero,
#  will be 2D array with number system for which function to call on it
#  0, horizontal
#  1, vertical
#  2, diag1
#  3, diag2
#  first number will be index to run function on, second number will be function to run
#  requires sizeSquare: size of the square, square: the list holding the square
#  returns 2D list that contains where and how to solve the zero
def findOneZero(sizeSquare, square):
  oZeroes = []

  #check horizontal and vertical
  for i in range(sizeSquare):
    numNotZeroVert = 0
    numNotZeroHori = 0
    for j in range(sizeSquare):
      #check horizontal
      if square[(i*sizeSquare)+j] != 0:
        numNotZeroHori += 1
      #check vertical
      if square[i+(j*sizeSquare)] != 0:
        numNotZeroVert += 1

    #add horizontal and vertical to list, if there is only one zero in the row or column
    if numNotZeroHori == sizeSquare-1:
      oZeroes.append([i*sizeSquare, 0])
    if numNotZeroVert == sizeSquare-1:
      oZeroes.append([i, 1])

  #check diag1 and diag2
  numNotZeroDiag1 = 0
  numNotZeroDiag2 = 0
  offsetDiag1 = sizeSquare + 1
  offsetDiag2 = sizeSquare - 1
  for i in range(sizeSquare):
    #check diag1
    if square[i*offsetDiag1] != 0:
      numNotZeroDiag1 += 1
    #check diag2
    if square[(i*offsetDiag2)+offsetDiag2] != 0:
      numNotZeroDiag2 += 1

  #add diag1 and diag2 to list, if there is only one zero in the diagonal
  if numNotZeroDiag1 == sizeSquare-1:
    oZeroes.append([i, 2])
  if numNotZeroDiag2 == sizeSquare-1:
    oZeroes.append([i, 3])

  return oZeroes


#check that square is correctly solved
#  requires sizeSquare, square, magicNumber
#    sizeSquare: size of the square
#    square: the list holding the square
#    magicNumber: the magicNumber for the size of the square
#  returns True if it is solved or False if it is not solved
def isCorrect(sizeSquare, square, magicNumber):
  #check horizontal and vertical, works because square is one dimensional
  for i in range(sizeSquare):
    numVert = 0
    numHori = 0
    for j in range(sizeSquare):
      #check horizontal
      numHori += square[(i*sizeSquare)+j]
      #check vertical
      numVert += square[i+(j*sizeSquare)]

    #add horizontal and vertical to list
    if numHori != magicNumber:
      return False
    if numVert != magicNumber:
      return False

  #check diag1 and diag2
  numDiag1 = 0
  numDiag2 = 0
  offsetDiag1 = sizeSquare + 1
  offsetDiag2 = sizeSquare - 1
  for i in range(sizeSquare):
    #check diag1
    numDiag1 += square[i*offsetDiag1]
    #check diag2
    numDiag2 += square[i*offsetDiag2+offsetDiag2]

  #add diag1 and diag2 to list
  if numDiag1 != magicNumber:
    return False
  if numDiag2 != magicNumber:
    return False

  #all tests have passed, so it is correct
  return True


#will solve square until it cannot progress or has completely solved it
#  requires sizeSquare: size of the square, square: the list holding the square
#  returns -1 if unsolvable, or 0 if it has finished solving
def solve(sizeSquare, square):
  while anyZeroes(sizeSquare, square):
    oZeroes = findOneZero(sizeSquare, square)
    #print oZeroes
    if len(oZeroes) == 0:
      return -1
    solveOne(sizeSquare, square, oZeroes)
    printSquare(sizeSquare, square)
    sleep(1) # to allow user to see progress
  return 0


#will solve any box that can be solved at the current step using list from findOneZero() return
#  requires sizeSquare, square, oZeroes
#    sizeSquare: size of the square
#    square: the list holding the square
#    oZeroes: list of solvable rows, columns, or diagonals from findOneZero() return
def solveOne(sizeSquare, square, oZeroes):
  for i in range(len(oZeroes)):
    if oZeroes[i][1] == 0:
      horizontalCalc(sizeSquare, square, oZeroes[i][0])
    elif oZeroes[i][1] == 1:
      verticalCalc(sizeSquare, square, oZeroes[i][0])
    elif oZeroes[i][1] == 2:
      diag1Calc(sizeSquare, square)
    elif oZeroes[i][1] == 3:
      diag2Calc(sizeSquare, square)


#check if there are any zeroes in the square
#  requires sizeSquare: size of the square, square: the list holding the square
#  returns True: there are zeroes, or False: there are no zeroes
def anyZeroes(sizeSquare, square):
  for i in range(len(square)):
    if square[i] == 0:
      return True
  return False


#calculates value to put into column with index to complete it (index can be any number (NOTE: not any number))
#  NOTE: assumes there is only one missing value
#  sums up the vertical, then at the index of the missingNum it places the correct number
#    that will make the sum equal to the magicNum
#  requires sizeSquare, square, index
#    sizeSquare: size of the square
#    square: the list holding the square
#    index: the value from findOneZero()[][0], look at solveOne() for more clarity
def verticalCalc(sizeSquare, square, index):
  col = index % sizeSquare
  missingNum = -1
  sum = 0
  for i in range(sizeSquare):
    sum += square[col+(i*sizeSquare)]
    if square[col+(i*sizeSquare)] == 0:
      missingNum = col+(i*sizeSquare)
  if missingNum != -1:
    square[missingNum] = magicNum(sizeSquare) - sum


#calculates value to put into row with index to complete it (index can be any number (NOTE: not any number))
#  NOTE: assumes there is only one missing value
#  sums up the horizontal, then at the index of the missingNum it places the correct number
#    that will make the sum equal to the magicNum
#  requires sizeSquare, square, index
#    sizeSquare: size of the square
#    square: the list holding the square
#    index: the value from findOneZero()[][0], look at solveOne() for more clarity
def horizontalCalc(sizeSquare, square, index):
  offsetLeft = index % sizeSquare
  trueIndex = index - offsetLeft
  missingNum = -1
  sum = 0
  for i in range(sizeSquare):
    sum += square[(i+trueIndex)]
    if square[(i+trueIndex)] == 0:
      missingNum = (i+trueIndex)
  if missingNum != -1:
    square[missingNum] = magicNum(sizeSquare) - sum


#will always look from index of 0 to last index, NOTE: assumes there is only one missing value
#  sums up the diagonal, then at the index of the missingNum it places the correct number
#    that will make the sum equal to the magicNum
#  requires sizeSquare: size of the square, square: the list holding the square
def diag1Calc(sizeSquare, square):
  offsetDiag = sizeSquare + 1
  missingNum = -1
  sum = 0
  for i in range(sizeSquare):
    sum += square[i*offsetDiag]
    if square[(i*offsetDiag)] == 0:
      missingNum = i*offsetDiag
  if missingNum != -1:
    square[missingNum] = magicNum(sizeSquare) - sum


#will always look from top right corner to bottom left corner, NOTE: assumes there is only one missing value
#  sums up the diagonal, then at the index of the missingNum it places the correct number
#    that will make the sum equal to the magicNum
#  requires sizeSquare: size of the square, square: the list holding the square
def diag2Calc(sizeSquare, square):
  offsetDiag = sizeSquare - 1
  missingNum = -1
  sum = 0
  for i in range(sizeSquare):
    sum += square[(i*offsetDiag)+offsetDiag]
    if square[(i*offsetDiag)+offsetDiag] == 0:
      missingNum = (i*offsetDiag)+offsetDiag
  if missingNum != -1:
    square[missingNum] = magicNum(sizeSquare) - sum


#will read in a square from file: filename
#  requires filename, separator
#    filename: name of the file to write to
#    separator: the separator to place in between each number in the square
#  NOTE: expects numbers to be separated by separator (space as default)
#    and rows on new lines, ex:
#    4 0 0
#    0 0 0
#    8 0 6
#  returns the square that was extracted from the file
def readFromFile(filename, separator=" "):
  square = []
  with open(filename, "r") as f:
    data = f.read()
  data = data.split("\n")
  for i in range(len(data)):
    if data[i] != "":
      #splits at separator, converts from string to int, and stores into square list
      square.extend([int(x) for x in data[i].split(separator)])

  return square


#writes square to file using separator, will create file if needed
#  requires filename, separator, square, size
#    filename: name of the file to write to
#    separator: the separator to place in between each number in the square
#    square: the list that is holding the square
#    size: the size of the square
def writeToFile(filename, separator, square, size):
  text = squareToString(square, size, separator)
  with open(filename, "w+") as f:
    f.write(text)


#turns square into a string that is separated by the separator
#  requires square, size, separator
#    square: the list that is holding the square
#    size: the size of the square
#    separator: the separator to place in between each number in the square
#  NOTE: designed for writing to a file, not for printing to the screen
#  returns a string that has the square separated by the separator
def squareToString(square, size, separator):
  squareText = ""
  for i in range(size):
    for j in range(size):
      if j < size-1:
        squareText += str(square[i*size +j]) + separator
      else:
        squareText += str(square[i*size +j]) + "\n"

  return squareText

#####################################################################################

#MAIN METHOD
#runs and solves square if possible
def run():
  args = commandLineParse() #get command line args
  #default square if they do not give a file
  square = [4, 0, 0,
            0, 0, 0,
            8, 0, 6]

  #check if the given path is a real file
  if args.i != "":
    if not os.path.isfile(args.i):
      print("ERROR 1001 - File does not exist\nExiting...")
      exit()
    else:
      square = readFromFile(args.i, args.s)

  size = int(sqrt(len(square))) # calculate size of square which is needed for functions

  #print magic number and original square
  print('Magic Number: ' + str(magicNum(size)))
  printSquare(size, square)

  #solve square if possible
  num = solve(size, square)
  if num == -1:
    print('Cannot solve, too little information.\n')
  else:
    print('Solved!\nSolution: ')
    printSquare(size, square)

    #check to make sure solution is actually correct
    if isCorrect(size, square, magicNum(size)):
      print('Solution checked and is correct!')
    else:
      print('Uh-oh solution has an error...\n')

  #write solution to given file
  if args.o != "":
    writeToFile(args.o, args.s, square, size)

#####################################################################################
# ARGPARSER
#
def commandLineParse():
  parser = argparse.ArgumentParser(description="Attempts to solve a magic square")
  parser.add_argument("-i", "-input", default="", help="input file name to bring in own square")
  parser.add_argument("-o", "-output", default="", help="output file name to save solution")
  parser.add_argument("-s", "-S", default=" ", help="separator value for input file, default is a \'space\'")
  parser.add_argument("-v", "-V", "--version", action="version", version="Version: 0.01")
  return parser.parse_args()


#####################################################################################
#####
#####          main
#####
#####################################################################################

if __name__ == '__main__':
  run()

"""
# SOLVABLE SQUARES FOR CONVENIENCE

#solvable 3x3
#square = [4, 0, 0,
#          0, 0, 0,
#          8, 0, 6]

#no solution 3x3
#square = [0, 6, 1,
#          0, 5, 0,
#          9, 0, 0]

#solvable 4x4
#square = [1, 15, 0, 4,
#          0, 11, 8, 0,
#          7, 0, 9, 0,
#          16, 0, 0, 13]

#solvable 5x5
square = [2, 16, 0, 10, 14,
          9, 20, 3, 0, 0,
          0, 0, 13, 0, 19,
          0, 4, 5, 0, 15,
          12, 0, 21, 8, 0]

"""
