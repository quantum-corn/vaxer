from tkinter import *

root= Tk()
root.title('Vaxer')

mainframe=Frame(root)
mainframe.grid(column=0, row=0)

def preliminary():
    fieldframe=Frame(mainframe)
    fieldframe.grid(row=2)

    Label(fieldframe, text='Enter your name').grid(row=0, column=0)
    name=Entry(fieldframe).grid(row=0, column= 1 )
    Label(fieldframe,text='Enter your age').grid(row=1, column=0)
    age=Entry(fieldframe).grid(row=1, column= 1 )
    Label(fieldframe,text='Enter your gender').grid(row=2, column=0)
    gender=Entry(fieldframe).grid(row=2, column= 1 )

def details():
    fieldframe=Frame(mainframe)
    fieldframe.grid(row=2)

    Label(fieldframe, text='Which vaccine type would you like').grid(row=0, column=0)
    type=Entry(fieldframe).grid(row=0, column= 1 )
    Label(fieldframe, text='Which vaccination centre would you like').grid(row=1, column=0)
    centre=Entry(fieldframe).grid(row=1, column= 1 )
    Label(fieldframe, text='Which vaccination slot would you like').grid(row=2, column=0)
    Slot=Entry(fieldframe).grid(row=2, column= 1 )


Label(mainframe, text=' Welcome, kindly fill the form with the required details').grid(row=0)

buttonframe=Frame(mainframe)
buttonframe.grid(row=1)

Button(buttonframe, text='Enter preliminary details', command=preliminary).grid(column=0, row=0)
Button(buttonframe, text='Enter details for vaccination', command=details).grid(column= 1, row=0)
Button(buttonframe, text='View my details').grid(column= 2, row=0)


root.mainloop()
