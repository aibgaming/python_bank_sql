import smtplib,re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mysql.connector as my

try:
  mydb=my.connect(host='localhost',user='root',database='python_bank',password="password")
  C=mydb.cursor()
except:
  mydb=my.connect(host='localhost',user='root',password="password")
  C=mydb.cursor()
  C.execute("create database python_bank")
  C.execute("create table python_bank.account(acc_name varchar(25),balance integer(100),password varchar(25),email varchar(25))")
  mydb.commit()

def create(account_name,amount,password,email):
  C.execute("insert into account values('"+str(account_name)+"','"+str(amount)+"','"+str(password)+"','"+str(email)+"')")
  mydb.commit()
  print("Account created")
  

def balance(account_name,password):
  C.execute("select * from account where acc_name='"+str(account_name)+"' and password='"+str(password)+"'")
  k=C.fetchone()
  return k

def money(account_name):
  C.execute("select * from account where acc_name='"+str(account_name)+"'")
  k=C.fetchone()
  return k[1]

def update(account_name,amount):
  C.execute("update account set balance=balance+"+str(amount)+" where acc_name=\'"+str(account_name)+"\'")
  mydb.commit()

def transfer(acc1,acc2,amount):
  C.execute("update account set balance=balance-"+str(amount)+" where acc_name=\'"+str(acc1)+"\'")
  C.execute("update account set balance=balance+"+str(amount)+" where acc_name=\'"+str(acc2)+"\'")
  mydb.commit()
  print(str(amount)+" transferred")

def del_account(account_name,password):
  C.execute("delete from account where acc_name='"+str(account_name)+"' and password='"+str(password)+"'")
  mydb.commit()
  print("Account deleted")

def change_password(account_name,pass1,pass2):
  C.execute("update account set password='"+str(pass2)+"' where acc_name='"+str(account_name)+"' and password='"+str(pass1)+"'")
  mydb.commit()

def display(account_name):
  C.execute("select * from account where acc_name='"+str(account_name)+"'")
  k=C.fetchone()
  return k

def comp_interest():
  C.execute("update account set balance=balance*1.005")
  mydb.commit()


def mail(add,sub,msg):
  sender_address = 'pythonbanking@gmail.com'
  sender_pass = 'pythonbanking2020'
  receiver_address = add
  message = MIMEMultipart()
  message['Subject'] = sub
  message.attach(MIMEText(msg, 'plain'))
  session = smtplib.SMTP('smtp.gmail.com', 587)
  session.starttls()
  session.login(sender_address, sender_pass)
  text = message.as_string()
  session.sendmail(sender_address, receiver_address, text)
  session.quit()
  print('Mail Sent')

def pass_strength(p):
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
            return True
            passwordstrength = 100
            break

    if passwordstrength == 0:
        return False

