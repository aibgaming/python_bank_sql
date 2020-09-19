from tkinter import *
import mysql.connector as my
import methods
from tkinter import messagebox 
import random
import time
import smtplib,re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import ImageTk
import PIL.Image
import pygame
import random,methods,os,subprocess
import yfinance as yf
import pandas as pd
import csv
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
import random
import copy
subprocess.Popen('python interest.py')

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
    messagebox.showinfo("Bank Balance","Your account balance is"+""+str(k[0])+"AED")    

    
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
    Label(b, text="Enter password: ", bg="green").pack()
    Label(b, text="").pack()
    passwordB = Entry(b)
    passwordB.pack()
    Label(b, text="").pack()
    Label(b, text="").pack()
    Button(b, text="Check your Balance", width=30, height=5, bg="green", command = cb).pack()
    b.mainloop()
def cpa():
    global accname
    global passnew
    global passold
    global cp
    cp = Tk()
    cp.geometry("600x400")
    Label(cp, text="Enter account name: ", bg="Azure").pack()
    Label(cp, text="").pack()
    accname = Entry(cp)
    accname.pack()
    Label(cp, text="").pack()
    Label(cp, text="Enter old password: ", bg="Azure").pack()
    Label(cp, text="").pack()
    passold = Entry(cp)
    passold.pack()
    Label(cp, text="").pack()
    Label(cp, text="").pack()
    Label(cp, text="Enter new password: ", bg="Azure").pack()
    Label(cp, text="").pack()
    passnew = Entry(cp)
    passnew.pack()
    Button(cp, text="Change", width=30, height=5, bg="Aquamarine", command = cp1).pack()
    cp.mainloop()
def cp1():
    while True:
        p = passnew.get()
        while True:
            pass_strength(p)
            break
        if passwordstrength == 100:
            break
        else:
            return
    C.execute("update account set password='"+passnew.get()+"' where acc_name='"+accname.get()+"' and password='"+passold.get()+"'")
    mydb.commit()
    cp.destroy()
    Change.destroy()
def fga():
    global fg
    global accnamefg
    fg = Tk()
    Label(fg, text="Enter account name: ", bg="Turquoise").pack()
    Label(fg, text="").pack()
    accnamefg = Entry(fg)
    accnamefg.pack()
    Button(fg, text="Get Password", width=30, height=5, bg="red", command = fg1).pack()
    fg.mainloop()
def fg1():    
    C.execute("select * from account where acc_name='"+accnamefg.get()+"'")
    k=C.fetchone()
    mail(k[3],"","Your Password is :-"+k[2])
    fg.destroy()
    Change.destroy()

def change():
    global Change
    Change = Tk()
    Change.geometry("1366x768")

    Label(Change, text="""If you wish to change your password, please choose the change option.
                          Alternatively, if you have forgotten your password, please choose the forgot password option. """, bg="blue",font=(None, 20)).pack()
    Button(Change, text="Change Password", width=30, height=5, bg="pink", command = cpa).pack()
    Label(Change, text="").pack()
    Label(Change, text="").pack()
    Button(Change, text="Forgot Password", width=30, height=5, bg="lime", command = fga).pack()
    Label(Change, text="").pack()
    Label(Change, text="").pack()
    Change.mainloop()
def BANK():
    bank = Tk()
    bank.geometry("1366x768")
    Button(bank, text="Register your Account", width=30, height=5, bg="red", command = register).pack()
    Label(bank, text="").pack()
    Button(bank, text="Check your Balance", width=30, height=5, bg="red", command = balance).pack()
    Label(bank, text="").pack()
    Button(bank, text="Change your Password", width=30, height=5, bg="red", command = change).pack()
    Label(bank, text="").pack()
    Button(bank, text="Deposit Money", width=30, height=5, bg="red", command = deposit).pack()
    Label(bank, text="").pack()
    Button(bank, text="Transfer Money", width=30, height=5, bg="red", command = transfer).pack()
    Label(bank, text="").pack()
    Button(bank, text="Delete Account", width=30, height=5, bg="red", command = delete).pack()
    Label(bank, text="").pack()
    Label(bank, text="").pack()
    bank.mainloop()
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
def slotgui():
  global slot_username
  global slot_password
  global slt
  slt = Tk()
  slt.title("Delete")
  slt.geometry("1366x768")
  Label(slt, text="Welcome to Slot Machine", bg="aqua",width=1366, height=10).pack()
  Label(slt, text="").pack()
  Label(slt, text="").pack()
  Label(slt, text="Enter account name: ", bg="turquoise").pack()
  Label(slt, text="").pack()
  slot_username = Entry(slt)
  slot_username.pack()
  Label(slt, text="Enter password: ", bg="turquoise").pack()
  Label(slt, text="").pack()
  slot_password = Entry(slt)
  slot_password.pack()
  Button(slt, text="Use Slot Machine", width=30, height=5, bg="turquoise", command = slot).pack()
  slt.mainloop()

def slot():
  import turtle
  import random
  import time
  trt = turtle.Screen()
  trt.setup(width=800, height=500)
  trt.title("Slot Machine")
  trt.colormode(255)
  trt.bgcolor("darkslategray")
  turtle.penup()
  turtle.hideturtle()
  turtle.speed(0)
  turtle.goto(-300, 150)
  turtle.color("white")
  turtle.pendown()
  turtle.pensize(8)
  for side in range(2):
    turtle.fd(600)
    turtle.right(90)
    turtle.fd(300)
    turtle.right(90)
  turtle.penup()
  turtle.fd(200)
  turtle.setheading(270)
  turtle.pendown()
  turtle.fd(300)
  turtle.penup()
  turtle.setheading(90)
  turtle.fd(300)
  turtle.setheading(0)
  turtle.fd(200)
  turtle.setheading(270)
  turtle.pendown()
  turtle.fd(300)
  slot_shape1 = turtle.Turtle()
  slot_shape1.speed(2)
  slot_shape1.penup()
  slot_shape1.goto(-200, 0)
  slot_shape1.shape("triangle")
  slot_shape1.setheading(90)
  slot_shape1.shapesize(5)
  slot_shape1.color("cyan")
  slot_shape2 = turtle.Turtle()
  slot_shape2.speed(2)
  slot_shape2.penup()
  slot_shape2.shape("circle")
  slot_shape2.setheading(90)
  slot_shape2.shapesize(5)
  slot_shape2.color("darkturquoise")
  slot_shape3 = turtle.Turtle()
  slot_shape3.speed(2)
  slot_shape3.penup()
  slot_shape3.goto(200, 0)
  slot_shape3.shape("square")
  slot_shape3.setheading(90)
  slot_shape3.shapesize(5)
  slot_shape3.color("cadetblue")
  done = turtle.Turtle()
  done.speed(0)
  done.penup()
  done.hideturtle()
  done.goto(0, 200)
  done.write("Press s to spin", align="center", font=("Helvetica", 20, "bold"))
  time.sleep(1.9)
  done.clear()
  def spin0():
    if True:
      global x
      global y
      global z
    x = random.randint(1,3)
    y = random.randint(1,3)
    z = random.randint(1,3)

  def spin():
    if x == 1:
      slot_shape1.shape("triangle")
      slot_shape1.color("cyan")
    elif x == 2:
      slot_shape1.shape("circle")
      slot_shape1.color("darkturquoise")
    elif x == 3:
      slot_shape1.shape("square")
      slot_shape1.color("cadetblue")
    if y == 1:
      slot_shape2.shape("triangle")
      slot_shape2.color("cyan")
    elif y == 2:
      slot_shape2.shape("circle")
      slot_shape2.color("darkturquoise")
    elif y == 3:
      slot_shape2.shape("square")
      slot_shape2.color("cadetblue")
    if z == 1:
      slot_shape3.shape("triangle")
      slot_shape3.color("cyan")
    elif z == 2:
      slot_shape3.shape("circle")
      slot_shape3.color("darkturquoise")
    elif z == 3:
      slot_shape3.shape("square")
      slot_shape3.color("cadetblue")

  def spin2():
    for action in range(10):
      spin0()
      spin()
      time.sleep(0.3)
    spin3()
    
  def spin3():
    if x == y and x == z:
      done.write("YOU WON 500!!!", align="center", font=("Helvetica", 20, "bold"))
      C.execute("update account set balance=balance+500 where acc_name=\'"+slot_username.get()+"\'")
      mydb.commit()
      time.sleep(1)
      done.clear()
    else:
      done.write("You lost 100", align="center", font=("Verdana", 20, "bold"))
      C.execute("update account set balance=balance-100 where acc_name=\'"+slot_username.get()+"\'")
      mydb.commit()
      time.sleep(1)
      done.clear()
  trt.listen()
  trt.onkeypress(spin2, "s")

#Load Images
icon = pygame.image.load('resources/icon.png')
cBack = pygame.image.load('resources/cards/cardback.png')
diamondA = pygame.image.load('resources/cards/ad.png')
clubA = pygame.image.load('resources/cards/ac.png')
heartA = pygame.image.load('resources/cards/ah.png')
spadeA = pygame.image.load('resources/cards/as.png')
diamond2 = pygame.image.load('resources/cards/2d.png')
club2 = pygame.image.load('resources/cards/2c.png')
heart2 = pygame.image.load('resources/cards/2h.png')
spade2 = pygame.image.load('resources/cards/2s.png')
diamond3 = pygame.image.load('resources/cards/3d.png')
club3 = pygame.image.load('resources/cards/3c.png')
heart3 = pygame.image.load('resources/cards/3h.png')
spade3 = pygame.image.load('resources/cards/3s.png')
diamond4 = pygame.image.load('resources/cards/4d.png')
club4 = pygame.image.load('resources/cards/4c.png')
heart4 = pygame.image.load('resources/cards/4h.png')
spade4 = pygame.image.load('resources/cards/4s.png')
diamond5 = pygame.image.load('resources/cards/5d.png')
club5 = pygame.image.load('resources/cards/5c.png')
heart5 = pygame.image.load('resources/cards/5h.png')
spade5 = pygame.image.load('resources/cards/5s.png')
diamond6 = pygame.image.load('resources/cards/6d.png')
club6 = pygame.image.load('resources/cards/6c.png')
heart6 = pygame.image.load('resources/cards/6h.png')
spade6 = pygame.image.load('resources/cards/6s.png')
diamond7 = pygame.image.load('resources/cards/7d.png')
club7 = pygame.image.load('resources/cards/7c.png')
heart7 = pygame.image.load('resources/cards/7h.png')
spade7 = pygame.image.load('resources/cards/7s.png')
diamond8 = pygame.image.load('resources/cards/8d.png')
club8 = pygame.image.load('resources/cards/8c.png')
heart8 = pygame.image.load('resources/cards/8h.png')
spade8 = pygame.image.load('resources/cards/8s.png')
diamond9 = pygame.image.load('resources/cards/9d.png')
club9 = pygame.image.load('resources/cards/9c.png')
heart9 = pygame.image.load('resources/cards/9h.png')
spade9 = pygame.image.load('resources/cards/9s.png')
diamond10 = pygame.image.load('resources/cards/10d.png')
club10 = pygame.image.load('resources/cards/10c.png')
heart10 = pygame.image.load('resources/cards/10h.png')
spade10 = pygame.image.load('resources/cards/10s.png')
diamondJ = pygame.image.load('resources/cards/jd.png')
clubJ = pygame.image.load('resources/cards/jc.png')
heartJ = pygame.image.load('resources/cards/jh.png')
spadeJ = pygame.image.load('resources/cards/js.png')
diamondQ = pygame.image.load('resources/cards/qd.png')
clubQ = pygame.image.load('resources/cards/qc.png')
heartQ = pygame.image.load('resources/cards/qh.png')
spadeQ = pygame.image.load('resources/cards/qs.png')
diamondK = pygame.image.load('resources/cards/kd.png')
clubK = pygame.image.load('resources/cards/kc.png')
heartK = pygame.image.load('resources/cards/kh.png')
spadeK = pygame.image.load('resources/cards/ks.png')

#Set Icon
pygame.display.set_icon(icon)

#Global Constants
black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

cards = [ diamondA, clubA, heartA, spadeA, \
          diamond2, club2, heart2, spade2, \
          diamond3, club3, heart3, spade3, \
          diamond4, club4, heart4, spade4, \
          diamond5, club5, heart5, spade5, \
          diamond6, club6, heart6, spade6, \
          diamond7, club7, heart7, spade7, \
          diamond8, club8, heart8, spade8, \
          diamond9, club9, heart9, spade9, \
          diamond10, club10, heart10, spade10, \
          diamondJ, clubJ, heartJ, spadeJ, \
          diamondQ, clubQ, heartQ, spadeQ, \
          diamondK, clubK, heartK, spadeK ]
cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]
card10 = [ diamond10, club10, heart10, spade10, \
            diamondJ, clubJ, heartJ, spadeJ, \
            diamondQ, clubQ, heartQ, spadeQ, \
            diamondK, clubK, heartK, spadeK ]

def cardvaluee(card):
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
def draw(cList, xList):
    cA = 0
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    if card in cardA:
        cA = 1
    return card, cA

def choose(cList, uList, dList):

    userA = 0
    dealA = 0
    card1, cA = draw(cList, uList)
    userA += cA
    card2, cA = draw(cList, dList)
    dealA += cA
    card3, cA = draw(cList, uList)
    userA += cA
    card4, cA = draw(cList, dList)
    dealA += cA
    return cardvaluee(card1) + cardvaluee(card3), userA, cardvaluee(card2) + cardvaluee(card4), dealA
def Casino():
    global cassname
    global casspass
    casin = Tk()
    casin.geometry("1366x768")
    Label(casin, text="WELCOME TO THE CASINO!", bg="yellow",width=1366, height=10).pack()
    Label(casin, text="").pack()
    Label(casin, text="").pack()
    Label(casin, text="Enter account name: ", bg="turquoise").pack()
    Label(casin, text="").pack()
    cassname = Entry(casin)
    cassname.pack()
    Label(casin, text="Enter password: ", bg="turquoise").pack()
    Label(casin, text="").pack()
    casspass = Entry(casin)
    casspass.pack()
    Label(root, text="").pack()
    Label(root, text="").pack()

    Button(casin, text="Blackjack", width=30, height=5, bg="red", command = main).pack()
    Label(casin, text="").pack()
    Label(casin, text="").pack()
    Button(casin, text="Dice", width=30, height=5, bg="red", command = dice).pack()
    Label(casin, text="").pack()
    Label(casin, text="").pack()
    Button(casin, text="Slot Machine", width=30, height=5, bg="red", command = slotgui).pack()
    Label(casin, text="").pack()
    Label(casin, text="").pack()
    casin.mainloop()
def dice():
    global label1
    global label2
    global label3
    global idice
    global rollbutton
    global ldice
    global cdice
    
    r = Tk()
    r.geometry('700x700')
    r.title('Roll Dice')
    Label(r, text="WELCOME TO THE DICE GAME", bg="yellow",width=1366, height=10).pack()
    Label(r, text="").pack()
    Label(r, text="").pack()

    cdice = Canvas(r, width=700, height=700)
    cdice.pack()

    idice= ''
    ldice = Label(r, text='', font=('Times', 120),fg='green')
    rollbutton = Button(r, text='Roll the dice', font=('times', 20,"bold"),state="disabled",background="brown",foreground='yellow',height=1, width=15, command=roll_dice)
    cdice.create_window(350, 120, window=rollbutton)
    button1 = Button(r, text='Start/Restart game', font=('times', 20,"bold"),background="blue",foreground='white',height=1, width=15, command=restart)
    cdice.create_window(350, 50, window=button1)
    label1 = Label(r, text='', font=('Times',20,'bold'),fg='brown')
    cdice.create_window(180, 550, window=label1)
    label2 = Label(r, bg='purple',fg='yellow',width=12)
    cdice.create_window(480, 550, window=label2)
    label3 = Label(r, text="""The rules are simple. If your dice add up to 12 atleast once in 10 games, you will earn 600""", font=('Times',13,'bold'),fg='white',bg="black")
    cdice.create_window(350, 620, window=label3)

    r.mainloop()


def roll_dice():
    global bttn_clicks
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
    die1 = random.choice(dice)
    die2 = random.choice(dice)
    ldice.configure(text=f'{die1} {die2}')
    cdice.create_window(350, 250, window=ldice)
    res = d[die1]+d[die2]
    label2.configure(text="You got  "+str(res))
    bttn_clicks += 1
    label1['text'] = "Dice rolled: " + str(bttn_clicks) + " times"
    if (bttn_clicks == 10 and res != 12):
        rollbutton.configure(state='disabled')
        methods.update(cassname.get(),-100)

       
        
    elif (res == 12):
        rollbutton.configure(state='disabled')
        methods.update(cassname.get(),600)

        
        

def restart():
    global bttn_clicks
    methods.update(cassname.get(),-100)

    bttn_clicks= 0
    label1.configure(text="")
    label2.configure(text="Not rolled yet")
    if idice:
        cdice.delete(idice)
    rollbutton.configure(state='normal')



def main():
    ccards = copy.copy(cards)
    stand = False
    userCard = []
    dealCard = []
    methods.update(cassname.get(),-100)

    pygame.init()
    methods.update(cassname.get(),-100)
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Blackjack')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Hit', 1, black)
    standTxt = font.render('Stand', 1, black)
    restartTxt = font.render('Retry', 1, black)
    gameoverTxt = font.render('Match Complete', 1, white)
    userSum, userA, dealSum, dealA = choose(ccards, userCard, dealCard)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,206,209))
    hitB = pygame.draw.rect(background, gray, (10, 445, 75, 25))
    standB = pygame.draw.rect(background, gray, (95, 445, 75, 25))

    while True:
        gameover = True if (userSum >= 21 and userA == 0) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True


        #checks for mouse clicks on buttons
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
                card, cA = draw(ccards, userCard)
                userA += cA
                userSum += cardvaluee(card)
                print ('User: %i',userSum)
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                stand = True
                while dealSum < 17:
                    card, cA = draw(ccards, dealCard)
                    dealA += cA
                    dealSum += cardvaluee(card)
                    print ('Dealer: %i',  dealSum)
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
                #restarts the game, updating scores
                if userSum == dealSum:
                    methods.update(cassname.get(),0)    

                elif userSum <= 21 and len(userCard) == 5:
                    methods.update(cassname.get(),300)
                elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                    methods.update(cassname.get(),300)    
                else:
                    methods.update(cassname.get(),0)    
                gameover = False
                stand = False
                userCard = []
                dealCard = []
                ccards = copy.copy(cards)
                userSum, userA, dealSum, dealA = choose(ccards, userCard, dealCard)
                restartB = pygame.draw.rect(background, (192,192,192), (270, 225, 75, 25))

        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (39, 448))
        screen.blit(standTxt, (116, 448))
        for card in dealCard:
            x = 10 + dealCard.index(card) * 110
            screen.blit(card, (x, 10))
        screen.blit(cBack, (120, 10))

        for card in userCard:
            x = 10 + userCard.index(card) * 110
            screen.blit(card, (x, 295))

        if gameover or stand:
            screen.blit(gameoverTxt, (270, 200))
            restartB = pygame.draw.rect(background, gray, (270, 225, 75, 25))
            screen.blit(restartTxt, (287, 228))
            screen.blit(dealCard[1], (120, 10))
            
        pygame.display.update()
            



root = Tk()
root.geometry("1366x768")
Button(root, text="Bank", width=30, height=5, bg="red", command = BANK).pack()
Label(root, text="").pack()
Label(root, text="").pack()
Button(root, text="Casino", width=30, height=5, bg="red", command = Casino).pack()
Label(root, text="").pack()
Label(root, text="").pack()



root.mainloop()
