from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Vaxing")

mainframe=ttk.Frame(root)
mainframe.grid(column=0, row=0)

ttk.Label(mainframe, text="Welcome to Vaxing!").grid(row=0)
ttk.Label(mainframe, text="Who are you?").grid(row=1)

buttonframe=ttk.Frame(mainframe)
buttonframe.grid(row=2)

ttk.Button(buttonframe, text="Patient").grid(column=0, row=0)
ttk.Button(buttonframe, text="Vaccination Centre").grid(column=1, row=0)
ttk.Button(buttonframe, text="Archive Administrator").grid(column=2, row=0)

root.mainloop()
