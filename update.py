import pickle
import mysql.connector as sql

db=sql.connect(host='localhost', user='ash', password='autobotsrollout')
cursor=db.cursor()

if db.is_connected():
    print("Connected")

source=open('dbcreate.sql')
lines=source.readlines()
for line in lines:
    if line[0]!='#':
        cursor.execute(line)

def update():
    files=('vaccines.dat', 'centers.dat')
    for file in files:
        table=open(file, 'rb')
        while True:
            try:
                data=pickle.load(table)
                dataset=data.split()

                if file=='vaccines.dat':
                    cursor.execute('INSERT INTO vaccines (vacc_id, name, status) VALUES ({0}, "{1}", "{2}");'.format(dataset[0], dataset[1], 'y' if dataset[2]=='Available' else 'n'))
                else:
                    cursor.execute('INSERT INTO centers (center_id, name, address, district, state, pincode) VALUES ({0}, "{1}", "{2}", "{3}", "{4}", {5});'.format(dataset[0], dataset[1], dataset[2], dataset[3], dataset[4], dataset[5]))

            except EOFError:
                break

update()
db.commit()

db.close()
