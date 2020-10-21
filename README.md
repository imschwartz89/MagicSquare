# MagicSquare
Python scripts to help solve Magic Squares

## Background
Basic info (Links working on 10/21/2020)

https://en.wikipedia.org/wiki/Magic_square

http://www.mathematische-basteleien.de/magsquare.htm

## Script Files
**magicSquare2.py** - Python 2 version (tested on Python 2.7.17)

**magicSquare3.py** - Python 3 version (tested on Python 3.6.8)

## Miscellaneous Files
**output.txt** - output of 3x3 square using " " as separators
<br />**output2.txt** - output of 4x4 square using " " as separators
<br />**square4x4.txt** - input of an unsolved 4x4 square using " " as separators
<br />**square5x5.txt** - input of an unsolved 5x5 square using " " as separators
<br />**squareComma4x4.txt** - input of an unsolved 4x4 square using "," as separators
<br />**squareCommaInput.txt** - input of an unsolved 3x3 square using "," as separators
<br />**squareInput.txt** - input of an unsolved 3x3 square using " " as separators
<br />**testOutputComma.txt** - output of 4x4 square using "," as separators
<br />**testSquare.txt** - output of 3x3 square using "," as separators

## How to Use
*NOTE: Assumes python3 refers to Python 3 on command line and python2 refers to Python 2 on command line.*
*<br />(all commands shown in Python3, simply use python2 magicSquare2.py instead of python3 magicSquare3.py)*

<br /><br />Running the following bash command displays the accepted argument flags (flags are the same for Python2 and Python3):
<br />`$ python3 magicSquare3.py -h`
>usage: magicSquare3.py [-h] [-i I] [-o O] [-s S] [-v]
>
>Attempts to solve a magic square
>
>optional arguments:
><br />&nbsp;&nbsp;-h, --help         show this help message and exit
><br />&nbsp;&nbsp;-i I, -input I     input file name to bring in own square
><br />&nbsp;&nbsp;-o O, -output O    output file name to save solution
><br />&nbsp;&nbsp;-s S, -S S         separator value for input file, default is a 'space'
><br />&nbsp;&nbsp;-v, -V, --version  show program's version number and exit


For instance if you want to run **magicSquare3.py** on **square4x4.txt**, you would run the following command:
<br />`$ python3 magicSquare3.py -i square4x4.txt`

This will solve the 4x4 in **square4x4.txt** and display the results on the screen (formatting is different than what is shown):

>Magic Number: 34
><br /> 1 15  0  4 
><br />10  0  8  0 
><br /> 0  0  0 12 
><br /> 0  2  0 13 
>
> 1 15 14  4 
><br />10  0  8  5 
><br /> 0  0  0 12 
><br /> 0  2  0 13 
>
> 1 15 14  4 
><br />10 11  8  5 
><br /> 0  0  0 12 
><br /> 0  2  0 13 
>
> 1 15 14  4 
><br />10 11  8  5 
><br /> 0  6  9 12 
><br /> 0  2  0 13 
>
> 1 15 14  4 
><br />10 11  8  5 
><br /> 7  6  9 12 
><br />16  2  3 13 
>
>Solved!
><br />Solution: 
><br /> 1 15 14  4 
><br />10 11  8  5 
><br /> 7  6  9 12 
><br />16  2  3 13 
>
>Solution checked and is correct!

However, if you want to use a different separator than " " like "," perhaps. You could run the following command:
<br />`$ python3 magicSquare3.py -i squareComma4x4.txt -s ","`

This will solve the 4x4 in **squareComma4x4.txt** that has "," as a separator in the file. It will display the results on the screen.

If you also want to save the results into a file, you can save the final solve state by using the following command:
<br />`$ python3 magicSquare3.py -i squareComma4x4.txt -o testOutput.txt -s ","`

Which will solve the square **squareComma4x4.txt**, then create a file named ***testOutput.txt*** and write the final solution to ***testOutput.txt***
<br />***testOutput.txt*** looks like:
><br />1,15,14,4
><br />10,11,8,5
><br />7,6,9,12
><br />16,2,3,13


*NOTE: If you get "Cannot solve, too little information.": It means that there is not enough numbers to allow the computer to accurately determine the correct numbers. This script not currently have guessing capabilities.*


## Future Work
- [ ] Create a flag to allow user to control if program should wait during display.
- [ ] Create a flag to allow user to write steps and final state to a file.
- [ ] Create a flag to allow user to specify the output file's separator, so it can be unique from the input file's separator.
- [ ] Allow for guessing.
