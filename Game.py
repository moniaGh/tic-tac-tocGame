from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('560x375')
button1 = ttk.Button(root, text=' ', command=lambda: buttonPressed(1))
button1.grid(row=0, column=0, ipadx=50, ipady=50)

button2 = ttk.Button(root, text=' ', command=lambda: buttonPressed(2))
button2.grid(row=0, column=1, ipadx=50, ipady=50)

button3 = ttk.Button(root, text=' ', command=lambda: buttonPressed(3))
button3.grid(row=0, column=2, ipadx=50, ipady=50)

button4 = ttk.Button(root, text=' ', command=lambda: buttonPressed(4))
button4.grid(row=1, column=0, ipadx=50, ipady=50)
button5 = ttk.Button(root, text=' ', command=lambda: buttonPressed(5))
button5.grid(row=1, column=1, ipadx=50, ipady=50)

button6 = ttk.Button(root, text=' ', command=lambda: buttonPressed(6))
button6.grid(row=1, column=2, ipadx=50, ipady=50)

button7 = ttk.Button(root, text=' ', command=lambda: buttonPressed(7))
button7.grid(row=2, column=0, ipadx=50, ipady=50)

button8 = ttk.Button(root, text=' ', command=lambda: buttonPressed(8))
button8.grid(row=2, column=1, ipadx=50, ipady=50)

button9 = ttk.Button(root, text=' ', command=lambda: buttonPressed(9))
button9.grid(row=2, column=2, ipadx=50, ipady=50)
player = 1


def buttonPressed(buttonNumber):
    global player
    if buttonNumber == 1 and player == 1:
        button1.config(text='X')
        player = 2
    elif buttonNumber == 1 and player == 2:
        button1.config(text="O")
        player = 1
    elif buttonNumber == 2 and player == 1:
        button2.config(text="X")
        player = 2
    elif buttonNumber == 2 and player == 2:
        button2.config(text="O")
        player = 1
    elif buttonNumber == 3 and player == 1:
        button3.config(text="X")
        player = 2
    elif buttonNumber == 3 and player == 2:
        button3.config(text="O")
        player = 1
    elif buttonNumber == 4 and player == 1:
        button4.config(text="X")
        player = 2
    elif buttonNumber == 4 and player == 2:
        button4.config(text="O")
        player = 1
    elif buttonNumber == 5 and player == 1:
        button5.config(text="X")
        player = 2
    elif buttonNumber == 5 and player == 2:
        button5.config(text="O")
        player = 1
    elif buttonNumber == 6 and player == 1:
        button6.config(text="X")
        player = 2
    elif buttonNumber == 6 and player == 2:
        button6.config(text="O")
        player = 1
    elif buttonNumber == 7 and player == 1:
        button7.config(text="X")
        player = 2
    elif buttonNumber == 7 and player == 2:
        button7.config(text="O")
        player = 1
    elif buttonNumber == 8 and player == 1:
        button8.config(text="X")
        player = 2
    elif buttonNumber == 8 and player == 2:
        button8.config(text="O")
        player = 1
    elif buttonNumber == 9 and player == 1:
        button9.config(text="X")
        player = 2
    elif buttonNumber == 9 and player == 2:
        button9.config(text="O")
        player = 1


root.mainloop()
