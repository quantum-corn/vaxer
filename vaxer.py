# %% md
# # Vaxer
# ## Vaccination Management System

# %% md
# First we will import the packages needed

# %% imports
from tkinter import *
import pickle
import mysql.connector as sql

# %% database connector
db=sql.connect(host='localhost', user='ash', password='autobotsrollout')
cursor=db.cursor()

# %% update static data tables
def update():
    files=('vaccines.dat', 'centers.dat')
    for file in files:
        table=open(file, 'rb')
        while True:
            try:
                data=pickle.load(table)
                dataset=data.split()

                if file=='vaccines.dat':
                    cursor.execute('INSERT INTO vaccines (vacc_id, name, status) VALUES ({0}, {1}, {2});'.format(dataset[0], dataset[1], "'y'" if dataset[2]=='Available' else "'n'"))
                else:
                    cursor.execute('INSERT INTO centers (center_id, name, address, district, state, pincode) VALUES ({0}, {1}, {2}, {3}, {4}, {5});'.format(dataset[0], dataset[1], dataset[2], dataset[3], dataset[4], dataset[5]))

            except EOFError:
                break

# %% tkinter root
root=Tk()
root.title("Vaxer")

# %% mainframe
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

    fieldframe=Frame(mainframe)
    fieldframe.grid(row=1)

    Label(fieldframe, text="Email").grid(row=0)
    Entry(fieldframe).grid(row=0, column=1)

    Label(fieldframe, text="Password").grid(row=1)
    Entry(fieldframe, show="\u2022").grid(row=1, column=1)

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

# %% Dashboard
def dashboard():
    pass

# %% Register
def register():
    clear(mainframe)

    Label(mainframe, text=' Welcome, kindly fill the form with the required details').grid(row=0)

    fieldframe=Frame(mainframe)
    fieldframe.grid(row=1)

    Label(fieldframe, text='Enter your name').grid(row=0, column=0)
    Entry(fieldframe, textvariable=name).grid(row=0, column= 1 )

    Label(fieldframe, text='Enter your age').grid(row=1, column=0)
    Entry(fieldframe, textvariable=age).grid(row=1, column= 1 )

    Label(fieldframe, text='Enter your gender').grid(row=2, column=0)
    Entry(fieldframe, textvariable=gender).grid(row=2, column= 1 )

    Label(fieldframe, text='Which vaccine type would you like').grid(row=3, column=0)
    Entry(fieldframe, textvariable=type).grid(row=3, column= 1 )

    Label(fieldframe, text='Which vaccination center would you like').grid(row=4, column=0)
    Entry(fieldframe, textvariable=center).grid(row=4, column= 1 )

    Label(fieldframe, text='Which vaccination slot would you like').grid(row=5, column=0)
    Entry(fieldframe, textvariable=slot).grid(row=5, column= 1 )

    Button(fieldframe, text='Continue', command=fetch).grid(row=6, column=1)

def fetch():
    pass

# %% Admin access
def admin():
    pass






cursor.execute('SOURCE dbcreate.sql')
update()







greet()

root.mainloop()
