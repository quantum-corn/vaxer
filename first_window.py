from tkinter import *

root=Tk()
root.title("Vaxer")

mainframe=Frame(root)
mainframe.grid(column=0, row=0)

Label(mainframe, text="Welcome to Vaxer!").grid(row=0)
Label(mainframe, text="Who are you?").grid(row=1)

buttonframe=Frame(mainframe)
buttonframe.grid(row=2)

Button(buttonframe, text="Patient").grid(column=0, row=0)
Button(buttonframe, text="Vaccination Centre").grid(column=1, row=0)
Button(buttonframe, text="Archive Administrator").grid(column=2, row=0)

root.mainloop()
