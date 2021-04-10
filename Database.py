import sqlite3


cxn = sqlite3.connect("temp.db")
cur=cxn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS main (FROM_ID varchar(30), 
TO_ID varchar(30), 
SUBJECT varchar(120), 
BODY varchar(1000),
DT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)''')

#info = ('hemanthalva2708@gmail.com','sumanthalva04@gmail.com','trial','Trying out')
#cur.execute('insert into main (FROM_ID,TO_ID,SUBJECT,BODY) values (?,?,?,?)',info)
cxn.commit()
x = cxn.execute('select * from main')
for i in x:
    print(i)


cur.execute('''CREATE TABLE IF NOT EXISTS login (USER_ID varchar(30) PRIMARY KEY, 
PASSWORD varchar(30) NOT NULL)''')
#info1 = ('hemanthalva2708@gmail.com','abcd1234')
#cur.execute('insert into login (USER_ID,PASSWORD) values (?,?)',info1)
cxn.commit()
x = cxn.execute('select * from login')
for i in x:
    print(i)

    
cur.close()