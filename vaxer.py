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

# %% create the database
def createdb():
    source=open('dbcreate.sql')
    lines=source.readlines()
    for line in lines:
        if line[0]!='#':
            cursor.execute(line)

# %% update static data tables
def update():
    files=('vaccines.dat', 'centers.dat')
    for file in files:
        table=open(file, 'rb')
        while True:
            try:
                data=pickle.load(table)

                if file=='vaccines.dat':
                    cursor.execute('INSERT INTO vaccines (vacc_id, name, status) VALUES ({0}, "{1}", "{2}");'.format(data[0], data[1], 'y' if data[2]=='Available' else 'n'))
                else:
                    cursor.execute('INSERT INTO centers (center_id, name, address, district, state, pincode) VALUES ({0}, "{1}", "{2}", "{3}", "{4}", {5});'.format(data[0], data[1], data[2], data[3], data[4], data[5]))

            except EOFError:
                break

    db.commit()

# %% tkinter root
root=Tk()
root.title("Vaxer")

# %% mainframe
mainframe=Frame(root)
mainframe.grid(column=0, row=0)

# %% restart button
Button(root, text="Home", command=greet).grid(row=1)

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
    Entry(fieldframe, textvariable=email).grid(row=0, column=1)

    Label(fieldframe, text="Password").grid(row=1)
    Entry(fieldframe, ,textvariable=password, show="\u2022").grid(row=1, column=1)

    Label(mainframe, text="New to Vaxer?").grid(row=2)
    Button(mainframe, text="Sign up", command=sign_up).grid(row=2, column=1)

    Label(mainframe, text="Have an account?").grid(row=3)
    Button(mainframe, text="Log in", command=log_in).grid(row=3, column=1)

# %% global log-in credentials
email=StringVar()
password=StringVar()

# %% Sign up System
def sign_up():
    id=email.get()
    auth=password.get()
    cursor.execute('SELECT * FROM login WHERE email="{0}";'.format(id))
    if cursor.fetchall() not [];
        Label(mainframe, text="E-mail already in use!").grid(row=4)
    else:
        cursor.execute('INSERT INTO login (email, pass) VALUES ("{0}", "{1}");'.format(id, auth))
        db.commit()
        dashboard()

# %% Log_in System
def log_in():
    id=email.get()
    auth=password.get()
    cursor.execute('SELECT * FROM login WHERE email="{0}";'.format(id))
    row=cursor.fetchall()
    msg=Label(mainframe, text='').grid(row=4)
    if row==[]:
        msg.destroy()
        msg=Label(mainframe, text="Incorrect E-mail!").grid(row=4)
    else:
        if pass not row[0][1]:
            msg.destroy()
            msg=Label(mainframe, text="Incorrect password!").grid(row=4)
        else:
            dashboard()


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

# %% global variables for registration
uidai=StringVar()
f_name= StringVar()
l_name=StringVar()
age= StringVar()
gender= StringVar()
type= StringVar()
centre= StringVar()
slot = StringVar()

# %% registration processing
def fetch():
    pass

# %% Admin access
def admin():
    pass






createdb()
update()
greet()

root.mainloop()

db.close()
