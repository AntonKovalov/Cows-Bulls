from random import randint
import random
from tkinter import *
import sys

print("\t\t\t\tCows and Bulls")
print("I will generate a 4 digit random number and you try to guess it! Each integer is unique in this number.")
print("\nFor every number at a wrong place you will get a bit of a Cow")
print("and in another case a Bull")
print("Make your decisions wisely and analyze previous steps.If you want to stop the game write\"exit\". ")
print("\nPress enter to start")
key = input()
if key =="exit":
    sys.exit()
print("\n\n")


#master = Tk()
digit_t = []
for digit in range(1,10):
    digit_t.append("%d"%digit)

class Number:
    def __init__(self,value,race):
        self.r = race
        self.val = value
        ran = []
        if race != "human":
            for i in range(0,4):
                ran.append(random.choice(digit_t))
                del digit_t[digit_t.index(ran[i])]
            self.val = ''.join(ran)
        else:
            self.val = value

p1  = Number("sixty 9","ai")


def game(num,x):
    c = 0
    b = 0
    guess = input("%d. Your guess:\n>>>"%x)
    if num == guess:
        print("Victory! The number is %s" %num)
        print("__________________________")
        print("Number of guesses: %d"%x)
    elif guess == "exit":
        sys.exit()
    else:
        print(guess, end = " ")
        for j in range (len(num)):
            for k in range (len(num)):
                if num[j] == guess[k] and k == j :
                    b = b + 1
                elif num[j] == guess[k] and k != j:
                    c = c + 1

        print("  Bulls:%d\tCows:%d\n"%(b,c))
        x = x + 1
        game(p1.val,x)

game(p1.val,1)
    #e1 = Entry(master).grid(row = 1,column = 0)
    #Button(master,text="Quit",command = quit).grid(row=3,column=0,sticky=W,pady=4)
    #Button(master,text="Play",command = ).grid(row=3, column=1, sticky=W,pady=4)
#mainloop()
