"""
need 10 * 10 table ->use 2 for loops
need 2 colors indicating players position
need ladder symbol
need snake symbol
need 2 dices
"""
import tkinter
from tkinter import *
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def board():
    endd = 100
    start = 81
    for i in range(0, 10):
        if i % 2 == 0:
            end_temp = endd
            for j in range(10):
                print(f'{endd:>4}', end='')
                endd -= 1
            print('\n')
            endd = end_temp - 20
        else:
            start_temp = start
            for j in range(10):
                print(f'{start:>4}', end='')
                start += 1
            print('\n')
            start = start_temp - 20

tk = Tk()
tk.title("Snake & Ladders")
tk.geometry("1000x1000")
# tk.config(bg="white", border="black")
label = Label(tk, text='Welcome to snake and ladders')
label.pack()
button = Button(tk, text='click here to start the game', command=board, relief=RAISED)
button.pack()
tk.mainloop()
