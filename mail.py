import sqlite3
import time

class login:
    def __init__(self):
        self.username = 'admin'
        self.password = 'password'
    def check(self,username,password):
        con = sqlite3.connect("temp.db")
        cur = con.cursor()
        state = f"SELECT USER_ID FROM login WHERE USER_ID='{username}' AND PASSWORD='{password}';"
        cur.execute(state)
        if not cur.fetchone():
            print("Login failed\n")
            x = input("Enter 1 to retry or press any key to exit: ")
            if x == '1':
                username = input("Enter mail id:")
                password = input("Enter password:")
                log = login()
                log.check(username,password)
            else:
                exit()
        else:
            print("\n Welcome \n")
            self.username = username
            self.password = password
        con.close()

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
    state = f"SELECT FROM_ID,SUBJECT,BODY,dt FROM main WHERE TO_ID='{uname}' ORDER BY DT DESC;"
    x = cur.execute(state)
    for i in x:
        print("From_ID: ", i[0])
        print("Subject: ", i[1])
        print("Body: ", i[2])
        print("Data and time: ", i[3])
        print("\n")
    cxn.close()
   
def check(answer,uname,to_id,subject,body):
    mail = send_mail(uname,to_id,subject,body)
    time.sleep(5)
    if answer == '1':
        mail.waiting()
    else:
        print("To late")
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
        log.check(username,password)
        uname = log.username
    elif(temp == "2"):
        exit()
    else:
        print("Invalid input")

    while(1):
        print("\n-------------HOMEPAGE-------------\n")
        print("1. Send Mail")
        print("2. Received Mail")
        print("3. Close")
        t1 = int(input())
        if(t1==1):
            print("\n Compose Mail \n")
            to_id = input("Mail to be sent to: ")
            subject = input("Subject: ")
            body = input("Body: ")

            print("1.UNDO (With in 5 sec)")
            print("Any key for sending")
            answer = "2"
            answer = input()
            check(answer,uname,to_id,subject,body)
        elif(t1==2):
            print("\n Received mail \n")
            received(uname)
        else:
            break
            print("Invalid input")
#print("Welcome")
