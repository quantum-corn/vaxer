import mysql.connector as sqldb
db= sqldb.connect(host='localhost', user='ash', passwd='autobotsrollout', database='student')
Executecursor=db.cursor()
sqlquery="select * from student where name='anindita'"
Executecursor.execute(sqlquery)
Result= Executecursor.fetchall()
for details in Result:
    print(details)
