from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")


def restart_time():
    os.system("shutdown /r /t 20")


def logout():
    os.system("shutdown -l")


def shutdown():
    os.system("shutdown /s /t 1")


s = Tk()
s.title('ShutDown App')
s.geometry('500x500')
s.config(bg='light blue')
button = Button(s, text='Restart', font=("Time New Roman", 20, "bold"), bg='light cyan', cursor='plus', relief=RAISED, command=restart)
button.place(x=150, y=60, height=50, width=200)
button = Button(s, text='Restart Time', font=("Time New Roman", 20, "bold"), bg='light cyan', cursor='plus', relief=RAISED, command=restart_time)
button.place(x=150, y=160, height=50, width=200)
button = Button(s, text='Logout', font=("Time New Roman", 20, "bold"), bg='light cyan', cursor='plus', relief=RAISED, command=logout)
button.place(x=150, y=260, height=50, width=200)
button = Button(s, text='ShutDown', font=("Time New Roman", 20, "bold"), bg='light cyan', cursor='plus', relief=RAISED, command=shutdown)
button.place(x=150, y=360, height=50, width=200)
s.mainloop()