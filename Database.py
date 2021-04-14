import sqlite3


cxn = sqlite3.connect("temp.db")
cur=cxn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS main (MID INTEGER PRIMARY KEY AUTOINCREMENT,FROM_ID varchar(30), 
TO_ID varchar(30), 
SUBJECT varchar(120), 
BODY varchar(1000),
DT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)''')

#info = ('mail@gmail.com','hemanthalva2708@gmail.com','trial','Trying out')
#cur.execute('insert into main (FROM_ID,TO_ID,SUBJECT,BODY) values (?,?,?,?)',info)
#info = ('hemanthalva2708@gmail.com','mail@gmail.com','trial','Trying out')
#cur.execute('insert into main (FROM_ID,TO_ID,SUBJECT,BODY) values (?,?,?,?)',info)
cxn.commit()
x = cxn.execute('select * from main')
for i in x:
    print(i)

#cur.execute('''CREATE TABLE IF NOT EXISTS labels 
#(MID INTEGER PRIMARY KEY AUTOINCREMENT,FROM_ID varchar(30), 
#TO_ID varchar(30), 
#STARRED INTEGER NOT NULL DEFAULT 0,
#SNOOZED INTEGER NOT NULL DEFAULT 0,
#SPAM INTEGER NOT NULL DEFAULT 0,
#DT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
#FOREIGN KEY(MID) REFERENCES main(MID),FOREIGN KEY(FROM_ID) REFERENCES main(FROM_ID),FOREIGN KEY(TO_ID) REFERENCES main(TO_ID))''')

#cxn.commit()
#x = cxn.execute('select * from labels')
#for i in x:
#    print(i)


cur.execute('''CREATE TABLE IF NOT EXISTS login (USER_ID varchar(30) PRIMARY KEY, 
PASSWORD varchar(30) NOT NULL)''')


info1 = ('h@gmail.com','h123')
cur.execute('insert into login (USER_ID,PASSWORD) values (?,?)',info1)

info1 = ('r@gmail.com','r123')
cur.execute('insert into login (USER_ID,PASSWORD) values (?,?)',info1)

info1 = ('s@gmail.com','s123')
cur.execute('insert into login (USER_ID,PASSWORD) values (?,?)',info1)

#info1 = ('mail@gmail.com','abc123')
#cur.execute('insert into login (USER_ID,PASSWORD) values (?,?)',info1)
cxn.commit()
x = cxn.execute('select * from login')
for i in x:
    print(i)

x = cxn.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in x:
    print(i)

#info = (2,'2021-04-14 12:02:45', 1)
#cur.execute('insert into hemanthalva2708 (MID,DT,STARRED) values (?,?,?)',info)
cxn.commit()
#col = []
t=cur.execute("PRAGMA TABLE_INFO(h)")
print(t.fetchall())
# for i in cur.fetchall():
#    col.append(i[1])
#print(col)

# cur.execute('UPDATE hemanthalva2708 SET STARRED = 0 WHERE MID = 1')

x = cur.execute('select * from h')
for i in x:
    print(i)
cur.close()
