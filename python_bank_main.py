from tkinter import *
import mysql.connector as my
from methods import *
from tkinter import messagebox 
import random
import time
try:
  mydb=my.connect(host='localhost',user='root',database='python_bank',password="gautham2004")
  C=mydb.cursor()
except:
  mydb=my.connect(host='localhost',user='root',password="password")
  C=mydb.cursor()
  C.execute("create database python_bank")
  C.execute("create table python_bank.account(acc_name varchar(25),balance integer(100),password varchar(25),email varchar(25))")
  mydb.commit()
def confirm():
    global c
    while True:
        if code.get()== i:
            c = 1
            V.destroy()
            C.execute("insert into account values('"+username.get()+"','"+amount.get()+"','"+password.get()+"','"+email.get()+"')")
            mydb.commit()
            rs.destroy()
            return
        else:
            messagebox.showwarning("Incorrect Verification Code"," Please enter the correct verification code.")
            continue


def create():
    global V
    global code
    global i
    global c
    c = 2
    while True:
        p = password.get()
        while True:
            pass_strength(p)
            break
        if passwordstrength == 100:
            break
        else:
            return
    msg = "Welcome to python bank!\nHere is your verification code:\n"+i+"\nWe hope to continue serving you in the future.\n\n\n\nPlease ignore this message if it doesn't concern you"
    mail(email.get(),"Account Registration- Verification Code",msg)
    messagebox.showinfo("Verification Code", "A verification code has been sent to your inbox.")    
    V = Tk()
    V.title("Make Your Account")
    V.geometry("1366x768")
    Label(V, text="Enter verification code: ", bg="cyan").pack() 
    Label(V, text="").pack()
    code = Entry(V)
    code.pack()
    Label(V, text="").pack()
    Button(V, text="OK", width=10, height=1, bg="red", command = confirm).pack()
    Label(V, text="").pack()
    
    V.mainloop()
def cb():
    C.execute("select balance from account where acc_name='"+usernameB.get()+"' and password='"+passwordB.get()+"'")
    k=C.fetchone()
    messagebox.showinfo("Bank Balance","Your account balance is"+str(k[0])+"AED")    

    
def pass_strength(p):
    global passwordstrength
    passwordstrength = 0
    while True:  
        if (len(p)<6):
            break
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[0-9]",p):
            break
        elif not re.search("[@!#$%^&*-+]",p):
            break
        elif re.search("\s",p):
            break
        else:
            passwordstrength = 100
            break
    if passwordstrength == 100:
      pass
    else:
        messagebox.showwarning("Password isnt strong enough!", "Please Re-enter your password.")
    
def register():
    global rs
    global username
    global amount
    global password
    global email
    global x
    global i
    i = str(random.randint(10000,99999))
    rs = Tk()
    rs.title("Make Your Account")
    rs.geometry("1366x768")
    
    Label(rs, text="Make Your Account", bg="yellow",width=1366, height=10).pack()
    Label(rs, text="").pack()
    Label(rs, text="").pack()
    Label(rs, text="Enter account name: ", bg="cyan").pack()
    Label(rs, text="").pack()
    username = Entry(rs)
    
    username.pack()
    u = username.get()
    Label(rs, text="").pack()
    Label(rs, text="Enter amount: ", bg="cyan").pack()
    Label(rs, text="").pack()
    amount = Entry(rs)
    amount.pack()
    v = amount.get()
    Label(rs, text="").pack()
    Label(rs, text="Enter password: ", bg="cyan").pack()
    Label(rs, text="").pack()
    password = Entry(rs)
    password.pack()
    Label(rs, text="").pack()
        

    Label(rs, text="Enter email ID:", bg="cyan").pack()
    Label(rs, text="").pack()
    email = Entry(rs)
    email.pack()
    Label(rs, text="").pack()
    Label(rs, text="").pack()
    
    Label(rs, text="").pack()
    Button(rs, text="Register!", width=10, height=1, bg="red", command = create).pack()
    Label(rs, text="").pack()
    rs.mainloop()
def balance():
    global usernameB
    global passwordB
    b = Tk()
    b.title("Check you Balance")
    b.geometry("1366x768")
    
    Label(b, text="Check your Balance", bg="gold",width=1366, height=10).pack()
    Label(b, text="").pack()
    Label(b, text="").pack()
    Label(b, text="Enter account name: ", bg="green").pack()
    Label(b, text="").pack()
    usernameB = Entry(b)
    usernameB.pack()
    Label(b, text="Enter account name: ", bg="green").pack()
    Label(b, text="").pack()
    passwordB = Entry(b)
    passwordB.pack()
    Button(b, text="Check your Balance", width=30, height=5, bg="green", command = cb).pack()
    b.mainloop()
    


def depositsql():
  C.execute("update account set balance=balance+"+Deposit_amount.get()+" where acc_name=\'"+Deposit_username.get()+"\'")
  mydb.commit()
  messagebox.showinfo("Deposited","You deposited "+Deposit_amount.get()+" AED")
  de.destroy()

def deposit():
    global Deposit_username
    global Deposit_amount
    global de
    de = Tk()
    de.title("Deposit Money")
    de.geometry("1366x768")
    
    Label(de, text="Deposit Money", bg="aqua",width=1366, height=10).pack()
    Label(de, text="").pack()
    Label(de, text="").pack()
    Label(de, text="Enter account name: ", bg="turquoise").pack()
    Label(de, text="").pack()
    Deposit_username = Entry(de)
    Deposit_username.pack()
    Label(de, text="Enter amount to deposit: ", bg="turquoise").pack()
    Label(de, text="").pack()
    Deposit_amount = Entry(de)
    Deposit_amount.pack()
    Button(de, text="Deposit", width=30, height=5, bg="turquoise", command = depositsql).pack()
    de.mainloop()


def transfersql():
  C.execute("update account set balance=balance-"+transfer_amount.get()+" where acc_name=\'"+transfer_user1.get()+"\'")
  C.execute("update account set balance=balance+"+transfer_amount.get()+" where acc_name=\'"+transfer_user2.get()+"\'")
  mydb.commit()
  messagebox.showinfo("Transfered","You transferred "+transfer_amount.get()+" AED from "+transfer_user1.get()+" to "+transfer_user2.get())
  tr.destroy()

def transfer():
    global transfer_user1
    global transfer_user2
    global transfer_amount
    global tr
    tr = Tk()
    tr.title("Transfer Money")
    tr.geometry("1366x768")
    
    Label(tr, text="Transfer Money", bg="aqua",width=1366, height=10).pack()
    Label(tr, text="").pack()
    Label(tr, text="").pack()
    Label(tr, text="Enter account name of sender: ", bg="turquoise").pack()
    Label(tr, text="").pack()
    transfer_user1 = Entry(tr)
    transfer_user1.pack()
    Label(tr, text="Enter account name of receiver: ", bg="turquoise").pack()
    Label(tr, text="").pack()
    transfer_user2 = Entry(tr)
    transfer_user2.pack()
    Label(tr, text="Enter amount to transfer: ", bg="turquoise").pack()
    Label(tr, text="").pack()
    transfer_amount = Entry(tr)
    transfer_amount.pack()
    Button(tr, text="Transfer", width=30, height=5, bg="turquoise", command = transfersql).pack()
    tr.mainloop()

def deletesql():
  C.execute("delete from account where acc_name='"+delete_username.get()+"' and password='"+delete_password.get()+"'")
  mydb.commit()
  messagebox.showinfo("Deleted","You deleted your account!")
  dele.destroy()

def delete():
    global delete_username
    global delete_password
    global dele
    dele = Tk()
    dele.title("Delete")
    dele.geometry("1366x768")
    Label(dele, text="Delete Account", bg="aqua",width=1366, height=10).pack()
    Label(dele, text="").pack()
    Label(dele, text="").pack()
    Label(dele, text="Enter account name: ", bg="turquoise").pack()
    Label(dele, text="").pack()
    delete_username = Entry(dele)
    delete_username.pack()
    Label(dele, text="Enter password: ", bg="turquoise").pack()
    Label(dele, text="").pack()
    delete_password = Entry(dele)
    delete_password.pack()
    Button(dele, text="Delete", width=30, height=5, bg="turquoise", command = deletesql).pack()
    dele.mainloop()


def Bank():
  root = Tk()
  root.geometry("1366x768")

  Button(root, text="Register your Account", width=30, height=5, bg="red", command = register).pack()
  Button(root, text="Check your Balance", width=30, height=5, bg="red", command = balance).pack()
  Button(root, text="Deposit Money", width=30, height=5, bg="red", command = deposit).pack()
  Button(root, text="Transfer Money", width=30, height=5, bg="red", command = transfer).pack()
  Button(root, text="Delete Account", width=30, height=5, bg="red", command = delete).pack()

  Label(root, text="").pack()
  root.mainloop()


Bank()

