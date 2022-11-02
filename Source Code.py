import random
from tkinter import *
import pyperclip

#Initialize tkinter
root = Tk()

#Set the size of the window
root.geometry("300x300")

#Declare a variable that is a string used to store password.
passstr = StringVar()

#Declare a variable that is an integer used to store length of password.
passlen = IntVar()

#Initially setting password length.
passlen.set(0)

#Function to generate the password
def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(',')']
    #Empty string declaration
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    #Set the password to the
    passstr.set(password)

def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

Label(root, text="Password Generator Application", font='helvetica 18 bold').pack()

Label(root, text="Enter password length").pack(pady=3)

Entry(root, textvariable = passlen).pack(pady=3)

Button(root, text="Generate Password", command=generate).pack(pady=3)

Entry(root, textvariable=passstr).pack(pady=3)

Button(root, text="Copy to Clipboard", command=copytoclipboard).pack()

root.mainloop()
