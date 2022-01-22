# %% md
# # Vaxer
# ## Vaccination Management System

# %% md
# First we will import the packages needed

# %% imports
from tkinter import *
import pickle as pck
import mysql.connector as sql

# %% tkinter root
root=Tk()
root.title("Vaxer")

mainframe=Frame(root)
mainframe.grid(column=0, row=0)

# %% clearing a window
def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# %% first window
def greet():
    clear(mainframe)

    Label(mainframe, text="Welcome to Vaxer!").grid(row=0)
    Label(mainframe, text="Who are you?").grid(row=1)

    buttonframe=Frame(mainframe)
    buttonframe.grid(row=2)

    Button(buttonframe, text="Patient", command=patient).grid(column=0, row=0)
    Button(buttonframe, text="Administrator", command=admin).grid(column=1, row=0)

# %% Patient greet window
def patient():
    clear(mainframe)

    Label(mainframe, text="Welcome to Vaxer!").grid(row=0)

    textframe=Frame(mainframe)
    textframe.grid(column=0, row=1)

    entryframe=Frame(mainframe)
    entryframe.grid(column=1, row=1)

    Label(textframe, text="Email").grid(row=0)
    Entry(entryframe).grid(row=0)

    Label(textframe, text="Password").grid(row=1)
    Entry(entryframe, show="\u2022").grid(row=1)

    Label(mainframe, text="New to Vaxer?").grid(row=2)
    Button(mainframe, text="Sign up", command=sign_up).grid(row=2, column=1)

    Label(mainframe, text="Have an account?").grid(row=3)
    Button(mainframe, text="Log in", command=log_in).grid(row=3, column=1)

# %% Sign up System
def sign_up():
    pass

# %% Log_in System
def log_in():
    pass

# %% Admin access
def admin():
    pass





greet()

root.mainloop()
