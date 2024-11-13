
import re
from tkinter import *

def password_strength():

    password = entry_window.get()

    if len(password) < 12:
        strengthText.set('Weak password: must be longer than 12 characters')
        return 
    if not re.search("[A-Z]", password):
        strengthText.set('Weak password: must contain at least 1 uppercase letter')
        return
    if not re.search("[a-z]", password):
        strengthText.set('Weak password: must contain at least 1 lowercase letter')
        return 
    if not re.search("[0-9]", password):
        strengthText.set('Weak password: must contain at least 1 number')
        return 
    if not re.search("[!@#$%^&*()]", password):
        strengthText.set('Weak password: must contain at least 1 special character')
        return 
    strengthText.set('Strong Password') 

root = Tk()
root.title('Word Guesser Game')
root.configure(background = 'white')
root.geometry("300x150")

name = Label(root, text='Password Strength Checker')
name.pack()

passText = Label(root, text = 'Enter your password:')
passText.pack()

entry_window = Entry(root, width=40, borderwidth=4, show='*')
entry_window.pack()

btn_check = Button(root, text = 'Check', command = password_strength)
btn_check.pack()

btn_quit= Button(root, text='Quit', command = root.destroy)
btn_quit.pack()

strengthText = StringVar()
strength = Label(root, textvariable = strengthText)
strength.pack()

root.mainloop()