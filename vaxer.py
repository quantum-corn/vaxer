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
        cursor.execute(line)

# %% update static data tables
def update():
    files=('vaccines.dat', 'centers.dat')
    for file in files:
        table=open(file, 'rb')
        while True:
            try:
                data=pickle.load(table)

                try:
                    if file=='vaccines.dat':
                        cursor.execute('INSERT INTO vaccines VALUES ({0}, "{1}", "{2}");'.format(data[0], data[1], 'Y' if data[2]=='Available' else 'N'))
                    else:
                        cursor.execute('INSERT INTO centers VALUES ({0}, "{1}", "{2}", "{3}", "{4}", {5});'.format(data[0], data[1], data[2], data[3], data[4], data[5]))
                except sql.errors.IntegrityError:
                    pass

            except EOFError:
                break

    db.commit()

# %% tkinter root
root=Tk()
root.title("Vaxer")
root.geometry("500x500")
root.configure(bg= "ghost white")
# %% mainframe
mainframe=Frame(root, borderwidth= 25,bg="ghost white")

mainframe.grid(column=0, row=0)

# %% clearing a window
def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# %% first window
def greet():
    clear(mainframe)

    Label(mainframe, text="Welcome to Vaxer!", borderwidth=15, bg="ghost white",   font= ("Bodoni MT", 28,"bold"), padx=25, pady=15).grid(row=0)
    Label(mainframe, text="Who are you?", borderwidth=20,bg="ghost white", font= ("Bodoni MT", 28, "bold"), padx=25, pady=15).grid(row=1)

    buttonframe=Frame(mainframe, bg="lavender")
    buttonframe.grid(row=2)

    Button(buttonframe, text="Patient", command=patient, padx=30, pady=5, bg="lavender",bd=3, relief=RAISED,font= ("Bodoni MT", 18)).grid(column=0, row=0)
    Button(buttonframe, text="Administrator", command=admin, padx=30, pady=5, bg="lavender",bd=3, relief=RAISED,font= ("Bodoni MT", 18)).grid(column=1, row=0)

# %% Patient greet window
def patient():
    clear(mainframe)

    Label(mainframe, text="Welcome to Vaxer!", borderwidth=15, bg="ghost white",font= ("Bodoni MT", 28,"bold")).grid(row=0)

    fieldframe=Frame(mainframe, bg="lavender")
    fieldframe.grid(row=1)

    Label(fieldframe, text="Email",bg="lavender",font= ("Bodoni MT", 18), padx=25, pady=15).grid(row=0)
    Entry(fieldframe, textvariable=email, bg="ghost white",bd=3, relief=SUNKEN).grid(row=0, column=1)

    Label(fieldframe, text="Password",bg="lavender",font= ("Bodoni MT", 18),padx=25, pady=15).grid(row=1)
    Entry(fieldframe, textvariable=password, show="\u2022", bg="ghost white",bd=3, relief=SUNKEN).grid(row=1, column=1)

    Label(mainframe, text="New to Vaxer?",bg="ghost white",font= ("Bodoni MT", 18, "bold"),padx=25, pady=15).grid(row=2)
    Button(mainframe, text="Sign up", command=sign_up, padx=30, pady=5, bg="lavender",bd=3, relief=RAISED,font= ("Bodoni MT", 15)).grid(row=2, column=1)

    Label(mainframe, text="Have an account?",bg="ghost white",font= ("Bodoni MT", 18,"bold"),padx=25, pady=15).grid(row=3)
    Button(mainframe, text="Log in", command=log_in, padx=30, pady=5, bg="lavender",bd=3, relief=RAISED,font= ("Bodoni MT", 15)).grid(row=3, column=1)

# %% global log-in credentials
email=StringVar()
password=StringVar()

#global user variable
id=''

# %% Sign up System
def sign_up():
    global id
    id=email.get()
    auth=password.get()
    cursor.execute('SELECT * FROM login WHERE email="{0}";'.format(id))
    if cursor.fetchall() != []:
        Label(mainframe, text="E-mail already in use!").grid(row=4)
    else:
        cursor.execute('INSERT INTO login VALUES ("{0}", "{1}");'.format(id, auth))
        db.commit()
        dashboard()

# %% Log_in System
def log_in():
    global id
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
            dashboard()


# %% Dashboard
def dashboard():
    clear(mainframe)
    Label(mainframe, text='Welcome '+id, bg="ghost white",font= ("Bodoni MT", 18),padx=25, pady=15).grid(row=0)
    cursor.execute('SELECT * FROM registration WHERE email="{0}";'.format(id))
    result=cursor.fetchall()
    if result==[]:
        Button(mainframe, text='Register yourself', command=register,  padx=30, pady=5, bg="lavender",bd=3, relief=RAISED,font= ("Bodoni MT", 16)).grid(row=1)
    else:
        Button(mainframe, text='Show my details', command=show_my_details,  padx=30, pady=5, bg="lavender",bd=3, relief=RAISED,font= ("Bodoni MT", 16)).grid(row=1)

def show_my_details():
    cursor.execute('SELECT uidai, first_name, last_name, age, gender, vaccines.name, centers.name, centers.address, centers.district,  centers.state, centers.pincode, slot FROM registration INNER JOIN vaccines ON registration.vaccine=vaccines.vacc_id INNER JOIN centers ON registration.center=centers.center_id WHERE email="{0}";'.format(id))
    result=cursor.fetchall()
    clear(mainframe)

    list=['Aadhar Number', 'First Name', 'Last Name', 'Age', 'Gender', 'Vaccine Type']
    i=0

    for item in list:
        Lf=LabelFrame(mainframe, text=item,bg="lavender",font= ("Bodoni MT", 16),)
        L=Label(Lf, text=result[0][i],bg="ghost white")
        Lf.grid(column=0, row=i)
        L.grid()
        i+=1

    Lf=LabelFrame(mainframe, text='Vaccination Center',bg="ghost white",font= ("Bodoni MT", 16),padx=25, pady=15)
    L=Label(Lf, text=result[0][6]+'\n'+result[0][7]+'\n'+result[0][8]+'\n'+result[0][9]+'-'+str(result[0][10]),bg="ghost white",font= ("Bodoni MT", 14),padx=25, pady=15)
    Lf.grid(column=0, row=6)
    L.grid()

    Lf=LabelFrame(mainframe, text='Vaccination Timeslot',bg="ghost white",font= ("Bodoni MT", 16),padx=25, pady=15)
    r=int(result[0][11])-1
    L=Label(Lf, text='{0}:00-{1}:00'.format(9+2*r,11+2*r),bg="ghost white",font= ("Bodoni MT", 16),padx=25, pady=15)
    Lf.grid(column=0, row=7)
    L.grid()

# %% Register
def register():
    clear(mainframe)

    Label(mainframe,bg="lavender",font= ("Bodoni MT", 16),padx=25, pady=15, text=' Welcome {0}, kindly fill the form with the required details'.format(id)).grid(row=0)

    fieldframe=Frame(mainframe,bg="lavender")
    fieldframe.grid(row=1)


    list=['first name', 'last name', 'Aadhar number', 'age', 'gender', 'choice of vaccine', 'preferred vaccination center', 'preferred vaccination slot']
    i=0

    for item in list:
        Label(fieldframe,bg="lavender",font= ("Bodoni MT", 16),padx=25, pady=15, text='Enter your '+item).grid(row=i, column=0)
        i+=1

    Entry(fieldframe, textvariable=f_name,bg="ghost white",bd=3, relief=SUNKEN).grid(row=0, column= 1 )
    Entry(fieldframe, textvariable=l_name,bg="ghost white",bd=3, relief=SUNKEN).grid(row=1, column= 1 )
    Entry(fieldframe, textvariable=uidai,bg="ghost white",bd=3, relief=SUNKEN).grid(row=2, column= 1 )
    Scale(fieldframe, from_=0, to=100, variable=age, orient=HORIZONTAL,bg="ghost white").grid(row=3, column=1)
    Radiobutton(fieldframe, text="Male", variable=gender, value='M',bg="ghost white").grid(row=4,column=1)
    Radiobutton(fieldframe, text="Female", variable=gender, value='F',bg="ghost white").grid(row=4, column=2)
    cursor.execute('SELECT name FROM vaccines WHERE status="Y"')
    result=cursor.fetchall()
    options=[]
    vaccine.set("Choose the vaccine")
    for item in result:
        options.append(item[0])
    OptionMenu(fieldframe, vaccine, *options).grid(row=5, column= 1)
    cursor.execute('SELECT name, address, pincode FROM centers')
    result=cursor.fetchall()
    options=[]
    center.set("Choose the center")
    for item in result:
        options.append(item[0]+'\n'+item[1]+'\n'+str(item[2]))
    OptionMenu(fieldframe, center, *options).grid(row=6, column= 1)
    list=[("9:00AM - 11:00AM", '1'), ("11:00AM - 1:00PM", '2'), ("1:00PM - 3:00PM", '3'), ("3:00PM - 5:00PM", '4')]
    i=7
    for (item, value) in list:
        Radiobutton(fieldframe, text=item, variable=slot, value=value).grid(row=i, column= 1 )
        i+=1
    Button(fieldframe, text='Continue', command=fetch, padx=30, pady=5, bg="lavender",bd=3, relief=RAISED,font= ("Bodoni MT", 16)).grid(row=11, column=1)

# %% global variables for registration
uidai=StringVar()
f_name= StringVar()
l_name=StringVar()
age= IntVar()
gender= StringVar()
vaccine= StringVar()
center= StringVar()
slot = StringVar()

# %% registration processing
def fetch():
    cursor.execute('SELECT vacc_id FROM vaccines WHERE name="{0}"'.format(vaccine.get()))
    vacc=cursor.fetchall()[0][0]
    cursor.execute('SELECT center_id FROM centers WHERE CONCAT_WS(CHAR(10 USING UTF8), name, address, pincode)="{0}"'.format(center.get()))
    cent=cursor.fetchall()[0][0]
    cursor.execute('INSERT INTO registration VALUES ({0}, "{1}", "{2}", {3}, "{4}", {5}, {6}, "{7}", "{8}")'.format(uidai.get(), f_name.get(), l_name.get(), age.get(), gender.get(), vacc, cent, slot.get(), id))
    db.commit()
    dashboard()

# %% Admin access
def admin():
    clear(mainframe)
    Label(mainframe, text='Enter password to verify access',bg="lavender",font= ("Bodoni MT", 18), padx=25, pady=15).grid(row=0)
    Entry(mainframe, textvariable=password, show="\u2022",bg="ghost white",bd=3, relief=SUNKEN).grid(row=1)
    Button(mainframe, text="Verify", command=verify,padx=30, pady=5, bg="lavender",bd=3, relief=RAISED,font= ("Bodoni MT", 18)).grid(row=2)

# %% verify
def verify():
    key='tea=PSUs'
    if password.get()!=key:
        Label(mainframe, text='You do not have access').grid(row=3)
    else:
        verified()

# %% verified
def verified():
    pass

    Label(mainframe, text="What are the fields you want to filter your search by?")
    list=['Aadhar Number', 'First Name', 'Last Name', 'Age', 'Gender', 'Vaccine Type', 'State', 'District', 'Pincode', ]
    i=0
    for item in list:
        Label(mainframe, text=item).grid(row=i, column=0)
        i+=1

    district=StringVar()
    state=StringVar()
    age_max=IntVar()
    age_min=IntVar()
    a=[uidai, f_name, l_name, district, state, vaccine]
    for item in a:
        a.set('any')
    a=[pincode, age_max, age_min]
    for item in a:
        a.set(0)

#     display()
#
#
#     cursor.execute('SELECT uidai, first_name, last_name, age, gender, vaccines.name, centers.name, centers.address, centers.district,  centers.state, centers.pincode, slot FROM registration INNER JOIN vaccines ON registration.vaccine=vaccines.vacc_id INNER JOIN centers ON registration.center=centers.center_id WHERE email="{0}";'.format(id))
#     result=cursor.fetchall()
#
#
#
#     Lf=LabelFrame(mainframe, text='Vaccination Center')
#     L=Label(Lf, text=result[0][6]+'\n'+result[0][7]+'\n'+result[0][8]+'\n'+result[0][9]+'-'+str(result[0][10]))
#     Lf.grid(column=0, row=6)
#     L.grid()
#
#     Lf=LabelFrame(mainframe, text='Vaccination Timeslot')
#     r=int(result[0][11])-1
#     L=Label(Lf, text='{0}:00-{1}:00'.format(9+2*r,11+2*r))
#     Lf.grid(column=0, row=7)
#     L.grid()
#
# # %% display the records
# def display():
#     cursor.execute('SELECT uidai, first_name, last_name, age, gender, vaccines.name, centers.name, centers.address, centers.district,  centers.state, centers.pincode, slot FROM registration INNER JOIN vaccines ON registration.vaccine=vaccines.vacc_id INNER JOIN centers ON registration.center=centers.center_id WHERE email="{0}";'.format(id))
#     result=cursor.fetchall()
#     r=int(result[0][11])-1
#     time='{0}:00-{1}:00'.format(9+2*r,11+2*r)




# %% restart button
Button(root, text="Home", command=greet,  padx=30, pady=5, bg="lavender",bd=3, relief=RAISED,font= ("Bodoni MT", 18)).grid(row=1)

createdb()
update()
greet()

mainloop()

db.close()
