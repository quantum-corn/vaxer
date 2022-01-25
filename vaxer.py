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
    Entry(fieldframe, textvariable=password, show="\u2022").grid(row=1, column=1)

    Label(mainframe, text="New to Vaxer?").grid(row=2)
    Button(mainframe, text="Sign up", command=sign_up).grid(row=2, column=1)

    Label(mainframe, text="Have an account?").grid(row=3)
    Button(mainframe, text="Log in", command=log_in).grid(row=3, column=1)

# %% global log-in credentials
email=StringVar()
password=StringVar()

#global user variable
user=''

# %% Sign up System
def sign_up():
    id=email.get()
    auth=password.get()
    cursor.execute('SELECT * FROM login WHERE email="{0}";'.format(id))
    if cursor.fetchall() != []:
        Label(mainframe, text="E-mail already in use!").grid(row=4)
    else:
        cursor.execute('INSERT INTO login (email, pass) VALUES ("{0}", "{1}");'.format(id, auth))
        db.commit()
        user=id
        dashboard(id)

# %% Log_in System
def log_in(id):
    id=email.get()
    auth=password.get()
    cursor.execute('SELECT * FROM login WHERE email="{0}";'.format(id))
    row=cursor.fetchall()
    text=StringVar()
    msg=Label(mainframe, textvariable=text).grid(row=4)
    if row==[]:
        text.set("Incorrect E-mail!")
    else:
        if auth != row[0][1]:
            text.set("Incorrect password!")
        else:
            user=id
            dashboard(id)


# %% Dashboard
def dashboard(id):
    clear(mainframe)
    cursor.execute('SELECT * FROM registration WHERE email={0};'.format(id))
    result=cursor.fetchall()
    if result==[]:
        Button(fieldframe, text='Register yourself', command=register).grid(row=0)
    else:
        Button(fieldframe, text='Show my details', command=show_my_details).grid(row=0)

def show_my_details():
    cursor.execute('SELECT * FROM registration WHERE email={0};'.format(id))
    result=cursor.fetchall()
    clear(mainframe)
    Lf=(mainframe, text='First Name').grid(column=0, row=0)
    Label(LabelFrame, text=result[0][0])
    Lf=(mainframe, text='First Name').grid(column=0, row=1)
    Label(LabelFrame, text=result[0][0])
    Lf=(mainframe, text='Last Name').grid(column=0, row=2)
    Label(LabelFrame, text=result[0][1])
    Lf=(mainframe, text='Age').grid(column=0, row=3)
    Label(LabelFrame, text=result[0][2])
    Lf=(mainframe, text='Gender').grid(column=0, row=4)
    Label(LabelFrame, text=result[0][3])
    Lf=(mainframe, text='Vaccine Type').grid(column=0, row=5)
    Label(LabelFrame, text=result[0][4])
    Lf=(mainframe, text='Center').grid(column=0, row=6)
    Label(LabelFrame, text=result[0][5])
    Lf=(mainframe, text='Slot').grid(column=0, row=7)
    Label(LabelFrame, text=result[0][6])
    Lf=(mainframe, text='Email').grid(column=0, row=8)
    Label(LabelFrame, text=result[0][7])



# %% Register
def register():
    clear(mainframe)

    Label(mainframe, text=' Welcome, kindly fill the form with the required details').grid(row=0)

    fieldframe=Frame(mainframe)
    fieldframe.grid(row=1)

    Label(fieldframe, text='Enter your first name').grid(row=0, column=0)
    Entry(fieldframe, textvariable=f_name).grid(row=0, column= 1 )

    Label(fieldframe, text='Enter your last name').grid(row=0, column=0)
    Entry(fieldframe, textvariable=l_name).grid(row=1, column= 1 )

    Label(fieldframe, text='Enter your Aadhar number').grid(row=0, column=0)
    Entry(fieldframe, textvariable=uidai).grid(row=2, column= 1 )

    Label(fieldframe, text='Enter your age').grid(row=1, column=0)
    Entry(fieldframe, textvariable=age).grid(row=3, column= 1 )

    Label(fieldframe, text='Enter your gender').grid(row=2, column=0)
    Entry(fieldframe, textvariable=gender).grid(row=4, column= 1 )

    Label(fieldframe, text='Which vaccine type would you like').grid(row=3, column=0)
    Entry(fieldframe, textvariable=vaccine).grid(row=5, column= 1 )

    Label(fieldframe, text='Which vaccination center would you like').grid(row=4, column=0)
    Entry(fieldframe, textvariable=center).grid(row=6, column= 1 )

    Label(fieldframe, text='Which vaccination slot would you like').grid(row=5, column=0)
    Entry(fieldframe, textvariable=slot).grid(row=7, column= 1 )

    Button(fieldframe, text='Continue', command=fetch).grid(row=8, column=1)

# %% global variables for registration
uidai=StringVar()
f_name= StringVar()
l_name=StringVar()
age= StringVar()
gender= StringVar()
vaccine= StringVar()
centre= StringVar()
slot = StringVar()

# %% registration processing
def fetch():
    cursor.execute('INSERT INTO registration (uidai, first_name, last_name, age, gender, vaccine, centre, slot, email) VALUES ({0}, "{1}", "{2}", {3}, "{4}", {5}, {6}, "{7}", "{8}")'.format(uidai.get(), f_name.get(), l_name.get(), age.get(), gender.get(), vaccine.get(), center.get(), slot.get(), user))
    db.commit()
    clear(mainframe)
    Label(mainframe, text='You have registered!').grid(row=0)
    Button(mainframe, text='Show my data', command=show_my_details).grid(row=1)

# %% Admin access
def admin():
    pass





# %% restart button
Button(root, text="Home", command=greet).grid(row=1)

createdb()
update()
greet()

root.mainloop()

db.close()
