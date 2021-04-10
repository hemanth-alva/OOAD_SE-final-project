import sqlite3

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
            print("Welcome")
            self.username = username
            self.password = password
        con.close()

class send_mail():
    def __init__(self, from_id, to_id, subject, body):
        self.from_id = from_id
        self.to_id = to_id
        self.subject = subject
        self.body = body
    
    print("Sending\n")
   
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
        print("-------------HOMEPAGE-------------\n")
        print("1. Send Mail")
        print("2. Close")
        t1 = int(input())
        if(t1==1):
            print("\n Compose Mail \n")
            to_id = input("Mail to be sent to: ")
            subject = input("Subject: ")
            body = input("Body: ")
            mail = send_mail(uname,to_id,subject,body)
        elif(t1==2):
            break
        else:
            print("Invalid input")
#print("Welcome")