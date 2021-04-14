import sqlite3
import time
import string
from os import system

class login:
    def __init__(self):
        self.username = 'admin'
        self.password = 'password'
        self.table = 'label'
    def check(self,username,password):
        con = sqlite3.connect("temp.db")
        cur = con.cursor()
        state = f"SELECT USER_ID FROM login WHERE USER_ID='{username}' AND PASSWORD='{password}';"
        cur.execute(state)
        if not cur.fetchone():
            print("Login failed\n")
            x = input("Enter 1 to retry or press any key to exit: ")
            if x == '1':
                # username = input("Enter mail id:")
                # password = input("Enter password:")
                # log = login()
                # log.check(username,password)
                con.close()
                return 2
            else:
                exit()
        else:
            system('cls')
            print("\nWelcome ",username[:-10])
            self.username = username
            self.password = password
            self.table = username[:-10]
            cur.execute('''CREATE TABLE IF NOT EXISTS {} (
                MID INTEGER PRIMARY KEY,
                DT varchar(30) NOT NULL,
                STARRED INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY(MID) REFERENCES main(MID), FOREIGN KEY(DT) REFERENCES main(DT))
            '''.format(self.table))
            #x = cur.execute('select * from {}'.format(self.table))
            #for i in x:
            #    print(i)
            con.close()
            return 1
        # print("#")
        # con.close()

class send_mail():
    def __init__(self, from_id, to_id, subject, body):
        self.from_id = from_id
        self.to_id = to_id
        self.subject = subject
        self.body = body
    def sending(self):
        cxn = sqlite3.connect("temp.db")
        cur = cxn.cursor()
        info = (self.from_id,self.to_id,self.subject,self.body)
        cur.execute('insert into main (FROM_ID,TO_ID,SUBJECT,BODY) values (?,?,?,?)',info)
        cxn.commit()
        cxn.close()
        print("Mail sent\n")
    def waiting(self):
        print("\nPrevious To address: ",self.to_id)
        print("Previous Subject: ", self.subject )
        print("Previous Body: ", self.body)
        print("\nEnter proper mail:\n ")
        self.to_id = input("Mail to be sent to: ")
        self.subject = input("Subject: ")
        self.body = input("Body: ")
        self.sending()

def received (uname):
    cxn = sqlite3.connect("temp.db")
    cur = cxn.cursor()
    state = f"SELECT FROM_ID,SUBJECT,BODY,dt,TO_ID FROM main WHERE TO_ID='{uname}' ORDER BY DT DESC;"
    x = cur.execute(state)
    for i in x:
        print("From_ID: ", i[0])
        print("Subject: ", i[1])
        print("Body: ", i[2])
        print("Data and time: ", i[3])
        print("\n")
    cxn.commit()
    cxn.close()

def received_label(uname):
    cxn = sqlite3.connect("temp.db")
    cur = cxn.cursor()
    mid = []
    state = f"SELECT FROM_ID,SUBJECT,BODY,dt,TO_ID,MID FROM main WHERE TO_ID='{uname}' ORDER BY DT DESC;"
    x = cur.execute(state)
    for i in x:
        print("From_ID: ", i[0])
        print("Subject: ", i[1])
        print("Body: ", i[2])
        print("Data and time: ", i[3])
        print("***  MID  ***: ",i[5])
        mid.append(i[5])
        print("\n")
    cxn.commit()
    cxn.close()
    return mid
    
def display_labels(uname):
    col = []
    i =2
    cxn = sqlite3.connect("temp.db")
    cur = cxn.cursor()
    print("\n  Display Label \n")
    cur.execute("PRAGMA TABLE_INFO({})".format(table))
    for j in cur.fetchall():
        col.append(j[1])
    print("\n Present Labels: ")
    while i<len(col):
        print(str(i-1)+". "+str(col[i]))
        i += 1
    print("Choose number associated with label:")
    print("Choose 0 to exit: ")
    clabel = input()
    if (int(clabel) == 0):
        exit()
    elif (int(clabel) >0) and (int(clabel) < len(col)-1):
        colm = col[int(clabel)+1]
        print("--"+colm+"--")
        display(table,colm)
    else:
        print("Invalid input")
        display_labels(uname,table)

def display(table,col):
    cxn = sqlite3.connect("temp.db")
    cur = cxn.cursor()
    query = "SELECT main.FROM_ID,main.SUBJECT,main.BODY,main.dt FROM MAIN INNER JOIN "+table+" ON main.MID = "+table+".MID WHERE "+table+"."+col+" = 1 ORDER BY main.DT DESC;"
    x = cur.execute(query)
    for i in x:
        print("From_ID: ", i[0])
        print("Subject: ", i[1])
        print("Body: ", i[2])
        print("Data and time: ", i[3])
        print("\n")
    cxn.close()

def set_label(table,date,mid,col):
    #info = (table,mid,date)
    cxn = sqlite3.connect("temp.db")
    cur = cxn.cursor()
    #print(table,type(table),type(mid),date,type(date))
    try:
        cur.execute('INSERT INTO ' + table + ' (MID,DT) VALUES (?,?)',(mid,date[0]))
    except:
        pass
    # cur.execute('INSERT INTO {} (MID,DT) VALUES (?,?)'.format(table.replace('"', '""')),(mid, date,))
    # cxn.commit()

    mid=str(mid)
    cur.execute('UPDATE '+ table + ' SET ' + col + ' = 1 WHERE MID = ' + mid)
    # cur.execute('UPDATE {} SET ? = 1'.format(table.replace('"', '""')), (col,))
    cxn.commit()

    temp=cur.execute('SELECT * FROM '+ table)
    # print(temp.fetchall())

    cxn.close()
    print("Done")


def label_function(uname,table):
    print("Enter 1 to add mail to label")
    print("Enter 2 to add label")
    print("Enter 3 to delete label")
    print("Enter 4 to remove mail from label")
    print("Enter any to exit")
    temp = input()
    if (temp == '1'):
        mid_list = received_label(uname)
        #print(mid_list)
        col = []
        i =2
        cxn = sqlite3.connect("temp.db")
        cur = cxn.cursor()
        print("Enter the mail ID you want to change label: \n OR enter 0 to exit")
        mid = int(input())
        if (mid in mid_list):
            state = f"SELECT dt FROM main WHERE MID='{mid}'"
            data = cur.execute(state)
            for k in data:
                date = k
            #print(date,mid)
        elif(mid == 0):
            exit()
        else:
            print("\n Invalid input \n")
            label_function(uname,table)
        cur.execute("PRAGMA TABLE_INFO({})".format(table))
        for j in cur.fetchall():
            col.append(j[1])
        print("\n Present Labels: ")
        while i<len(col):
            print(str(i-1)+". "+str(col[i]))
            i += 1
        print("Choose number associated with label:")
        print("Choose 0 to exit: ")
        clabel = input()
        if (int(clabel) == 0):
            exit()
        elif (int(clabel) >0) and (int(clabel) < len(col)-1):
            colm = col[int(clabel)+1]
            set_label(table,date,mid,colm)
        else:
            print("Invalid input")
            label_function(uname,table)
    elif (temp == '2'):
        i = 2
        col = []
        cxn = sqlite3.connect("temp.db")
        cur = cxn.cursor()
        system('cls')
        print("----------\n Add label\n---------")
        label = input("Enter label name: ")

        col2=[]
        cur.execute("PRAGMA TABLE_INFO({})".format(table))
        for j in cur.fetchall():
            col2.append(j[1])

        if label not in col2[2:]:
            query = "ALTER TABLE "+table+" ADD COLUMN "+label+" INTEGER NOT NULL DEFAULT 0"
            cur.execute(query)
            cxn.commit()
        else:
            print("Label already present")

        print("\n  Display Label \n")
        cur.execute("PRAGMA TABLE_INFO({})".format(table))
        
        for j in cur.fetchall():
            col.append(j[1])
        print("\n Present Labels: ")
        while i<len(col):
            print(str(i-1)+". "+str(col[i]))
            i += 1
        cxn.close()

    elif (temp == "3"):
        i = 2
        col = []
        cxn = sqlite3.connect("temp.db")
        cur = cxn.cursor()
        print("Delete label")
        print("\n  Display Label \n")
        cur.execute("PRAGMA TABLE_INFO({})".format(table))
        for j in cur.fetchall():
            col.append(j[1])
        print("\n Present Labels: ")
        while i<len(col):
            print(str(i-1)+". "+str(col[i]))
            i += 1
        if(len(col)==3):
            print("No labels other than starred present")
            return
        print("Choose number associated with label:")
        print("Choose 0 to exit: ")
        clabel = input()
        if (int(clabel) == 0):
            exit()
        elif (int(clabel) >0) and (int(clabel) < len(col)-1):
            colm = col[int(clabel)+1]
            print(colm)

            cur.execute('''CREATE TABLE IF NOT EXISTS {} (
                MID INTEGER PRIMARY KEY,
                DT varchar(30) NOT NULL,
                FOREIGN KEY(MID) REFERENCES main(MID), FOREIGN KEY(DT) REFERENCES main(DT))
            '''.format("temp_"+table))

            del_label=int(clabel)+1
            for i in range(2,len(col)):
                if i!=del_label :
                    cur.execute("ALTER TABLE temp_"+table+" ADD COLUMN "+col[i]+" INTEGER NOT NULL DEFAULT 0")


            query = "INSERT INTO temp_"+table + " SELECT MID,DT"
            for i in range(2,len(col)):
                if i!=del_label:
                    query = query + "," + col[i]
            query= query+ " FROM " + table

            cur.execute(query)

            cur.execute(" DROP TABLE IF EXISTS "+ table)
            cur.execute("ALTER TABLE temp_"+table + " RENAME TO "+ table)
            cxn.commit()

            cxn.close()
        else:
            print("Invalid input")
            label_function(uname,table)
        
    elif (temp == "4"):
        print("Remove mail from label")
        rem_mail(table)
    else:
        exit()


def rem_mail(table):
    i = 2
    col = []
    mid_list = []
    cxn = sqlite3.connect("temp.db")
    cur = cxn.cursor()
    query ="SELECT * FROM "+table
    cur.execute("PRAGMA TABLE_INFO({})".format(table))
    for j in cur.fetchall():
        col.append(j[1])
    while i<len(col):
        print(str(i-1)+". "+str(col[i]))
        i += 1
    x = cxn.execute(query)
    #print(x)
    for k in x:
        i = 2
        print("MID : ",k[0])
        mid_list.append(k[0])
        while i < len(col):
            print(col[i]+": "+ str(k[i]))
            i+=1 
        print("\n")
    mid = input("Enter valid mid: ")
    if int(mid) in mid_list:
        i =2 
        while i<len(col):
            print(str(i-1)+". "+str(col[i]))
            i += 1
        print("Choose number associated with label:")
        print("Choose 0 to exit: ")
        clabel = input()
        if (int(clabel) == 0):
            exit()
        elif (int(clabel) >0) and (int(clabel) < len(col)-1):
            colm = col[int(clabel)+1]
            cur.execute('UPDATE '+ table + ' SET ' + colm + ' = 0 WHERE MID = ' + mid)
            cxn.commit()
        else:
            print("Invalid input")
            rem_mail(uname,table)
        
    else:
        print("Invalid input")
        rem_mail(table)
    
def delete_mail(uname):
    mid_list = received_label(uname)
    if(len(mid_list)==0):
        print("Empty inbox")
        return
    del_mid = int(input("Enter the MID of the mail you wish to delete from your inbox : "))
    if del_mid in mid_list:
            cxn = sqlite3.connect("temp.db")
            cur = cxn.cursor()
            cur.execute('DELETE FROM main WHERE MID = '+str(del_mid))
            cur.execute('DELETE FROM ' + uname[:-10] + ' WHERE MID = '+str(del_mid))
            cxn.commit()
            cxn.close()
    else:
        print("Invalid mid. Kindly recheck")
        delete_mail(uname)

def check(answer,uname,to_id,subject,body):
    mail = send_mail(uname,to_id,subject,body)
    time.sleep(5)
    if answer == '1':
        mail.waiting()
    else:
        #print("Too late")
        mail.sending()
    
if __name__ == '__main__':
    print("\n------Welcome to Mail System-------\n")
    print("1. Login")
    print("2. Close")
    temp = input()
    uname= ""
    if(temp == '1'):
        username = input("Enter mail id: ")
        password = input("Enter password: ")
        log = login()
        temp2=1
        while temp2:
            redo=log.check(username,password)
            if redo==1:
                break
            username = input("Enter mail id: ")
            password = input("Enter password: ")
            
        uname = log.username
        table = log.table
    elif(temp == "2"):
        exit()
    else:
        print("Invalid input")
        exit()

    while(1):
        print("\n-------------HOMEPAGE-------------\n")
        print("1. Send Mail")
        print("2. Received Mail")
        print("3. Manage Labels")
        print("4. Labels")
        print("5. Delete from received mail")
        print("6. Close")
        t1 = int(input())
        if(t1==1):
            system('cls')
            print("-------------\n Compose Mail \n------------")
            to_id = input("Mail to be sent to: ")
            subject = input("Subject: ")
            body = input("Body: ")

            print("1.UNDO")
            print("Press ANY key to send")
            answer = "2"
            answer = input()
            check(answer,uname,to_id,subject,body)
        elif(t1==2):
            system('cls')
            print("------------\n Inbox \n---------------")
            received(uname)
        elif(t1==3):
            system('cls')
            print("------------\n Manage Labels\n-----------")
            label_function(uname,table)
            #manage_labels(uname)
        elif(t1==4):
            system('cls')
            print("--------------\n Labels\n-------------")
            display_labels(uname)
        elif(t1==5):
            system('cls')
            print("------------\n Delete mail\n--------------")
            delete_mail(uname)
        else:
            print(" SHUTTING DOWN MAILING SYSTEM ")
            break
#print("Welcome")
