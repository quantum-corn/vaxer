from tkinter import *
root= Tk()
root.title('Vaxer')

def myclick1():
    myLabel1= Label(root,text='enter your name').grid(row= 3, column=0)
    e=Entry(root, width= 50, bg='yellow', fg='black', borderwidth=2).grid(row=3, column= 2 )
    myLabel2= Label(root,text='enter your age').grid(row= 4, column=0)
    e1=Entry(root, width= 50, bg='yellow', fg='black', borderwidth=2).grid(row=4, column= 2 )
    myLabel3= Label(root,text='enter your gender').grid(row= 5, column=0)
    e2=Entry(root, width= 50, bg='yellow', fg='black', borderwidth=2).grid(row=5, column= 2 )
    
  
myLabel= Label(root, text=' Welcome. Kindly fill the form with the required details').grid(row=0, column= 0)
mybutton1= Button(root, text='Enter preliminary details', padx= 10, pady= 5, bg='cyan', command=myclick1).grid(row=2, column= 0)
mybutton2= Button(root, text='Enter details for vaccination', padx= 10, pady= 5, bg='cyan').grid(row=2, column= 5)
mybutton3= Button(root, text='View my details', padx= 10, pady= 5, bg='cyan').grid(row=2, column= 15)


root.mainloop()

