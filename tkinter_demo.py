import tkinter
from tkinter import messagebox
from tkinter import *
tk = tkinter.Tk()
tk.title('Tkinter Demo!!!')
tk.geometry('600x600')
#label for username
Label(tk, text='Username').place(x=40, y=60)
Label(tk, text='Password').place(x=40, y=100)
#message box
def Button1():
    messagebox.showinfo('status', "succssfully loggedin:)")
#button
b = Button(tk, text='Submit', command=Button1, bg="cyan", fg="orange").place(x=40, y=130)
username_input_area = Entry(tk, width=30).place(x=110, y=60)
password_input_area = Entry(tk, width=30).place(x=110, y=100)
# b.pack(side='top')
# r = Radiobutton(tk, text="python", value=1)
# r.pack(side='bottom')
v = StringVar(tk, '1')
values = {"RadioButton 1": "1",
          "RadioButton 2": "2",
          "RadioButton 3": "3",
          "RadioButton 4": "4",
          }
checkbutton1 = IntVar()
checkbutton2 = IntVar()
checkbutton3 = IntVar()
for (key, value) in values.items():
    Radiobutton(tk, text=key, variable=v, value=value, background="light blue").pack(ipady=5)
cb1 = Checkbutton(tk, text='Python', variable=checkbutton1, onvalue=1, offvalue=0, height=2, width=10)
cb1.pack()

tk.mainloop()