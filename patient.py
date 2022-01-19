from tkinter import *

root= Tk()
root.title('Vaxer')

mainframe=Frame(root)
mainframe.grid(column=0, row=0)

name= StringVar()
age= StringVar()
gender= StringVar()
type= StringVar()
centre= StringVar()
slot = StringVar()

def get_primary():
    Label(root, text='We have registered your primary info!').grid(row=0, column=0)
    Label(root, text=name.get()).grid(row=1,column=0)
    Label(root, text=age.get()).grid(row=2,column=0)
    Label(root, text=gender.get()).grid(row=3,column=0)

def get_details():
    Label(root, text='You have completed your vaccination registration!').grid(row=0, column=0)
    Label(root, text=type.get()).grid(row=1,column=0)
    Label(root, text=centre.get()).grid(row=2,column=0)
    Label(root, text=slot.get()).grid(row=3,column=0)

def preliminary():
    fieldframe=Frame(mainframe)
    fieldframe.grid(row=2)

    Label(fieldframe, text='Enter your name').grid(row=0, column=0)
    Entry(fieldframe, textvariable=name).grid(row=0, column= 1 )
    Label(fieldframe, text='Enter your age').grid(row=1, column=0)
    Entry(fieldframe, textvariable=age).grid(row=1, column= 1 )
    Label(fieldframe, text='Enter your gender').grid(row=2, column=0)
    Entry(fieldframe, textvariable=gender).grid(row=2, column= 1 )
    Button(fieldframe, text='Continue', command=get_primary).grid(row=3, column=1)

def details():
    fieldframe=Frame(mainframe)
    fieldframe.grid(row=2)

    Label(fieldframe, text='Which vaccine type would you like').grid(row=0, column=0)
    Entry(fieldframe, textvariable=type).grid(row=0, column= 1 )
    Label(fieldframe, text='Which vaccination centre would you like').grid(row=1, column=0)
    Entry(fieldframe, textvariable=centre).grid(row=1, column= 1 )
    Label(fieldframe, text='Which vaccination slot would you like').grid(row=2, column=0)
    Entry(fieldframe, textvariable=slot).grid(row=2, column= 1 )
    Button(fieldframe, text='Continue', command=get_details).grid(row=3, column=1)


Label(mainframe, text=' Welcome, kindly fill the form with the required details').grid(row=0)

buttonframe=Frame(mainframe)
buttonframe.grid(row=1)

Button(buttonframe, text='Enter preliminary details', command=preliminary).grid(column=0, row=0)
Button(buttonframe, text='Enter details for vaccination', command=details).grid(column= 1, row=0)
Button(buttonframe, text='View my details').grid(column= 2, row=0)


root.mainloop()
