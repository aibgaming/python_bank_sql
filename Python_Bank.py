import random,methods,os,subprocess
import yfinance as yf
import pandas as pd
import csv
import matplotlib.pyplot as plt
subprocess.Popen('python interest.py')

while True:
    print()
    print("Welcome to the bank!")
    print()
    print("1 to create a new account,2 to check balance,3 to deposit, 4 to transfer, 5 to delete account,6 to change password,7 to enter casino,8 to enter the stock market, else leave bank")
    opt=int(input("Enter option: "))
    if opt==1:
        try:
            account=input("Enter account name: ")
            amount=int(input("Enter amount: "))
            while True:
                print("Password should be over 5 characters in length, has to contain atleast one uppercase and lowercase character,one number,and one of the following symbols (@!#$%^&*-+)")
                password=input("Enter password: ")
                if methods.pass_strength(password):
                    print("Strong password!")
                    break
                else:
                    print("Weak password! Enter another password")
            email=input("Enter email id: ")
            verid=random.randint(10000,99999)
            msg="Welcome to python bank!\nHere is your verification code:\n"+str(verid)+"\nWe hope to continue serving you in the future.\n\n\n\nPlease ignore this message if it doesn't concern you"
            methods.mail(email,'Python bank verification code',msg)
            print("Verification email has been sent to your id")
            verified=False
            while True:
                verid_input=int(input("Enter verification id(Enter 0 to resend email, 1 to exit):"))
                if verid_input==verid:
                    print("Verified!")
                    verified=True
                    break
                elif verid_input==0:
                    print("Email resent")
                    methods.mail(email,'Python bank verification code',msg)
                    continue
                elif verid_input==1:
                    break
                else:
                    print("Wrong id")
            if verified:
                methods.create(account,amount,password,email)
            
        except:
            print("Invalid details")
        print()
    elif opt==2:
        try:
            account=input("Enter account name: ")
            password=input("Enter password: ")
            k=methods.balance(account,password)
            print("AccountName = ",k[0],"    Balance = ",k[1],"    Password = ",k[2],"    Email = ",k[3])
        except:
            print("Invalid account details")
        print()
    elif opt==3:
        try:
            account=input("Enter account name: ")
            amount=int(input("Enter amount: "))
            methods.update(account,amount)
            k=methods.money(account)
        except:
            print("Invalid account details")
        print()
    elif opt==4:
        try:
            acc1=input("Enter account name of sender: ")
            acc2=input("Enter account name of receiver: ")
            amount=int(input("Enter amount: "))
            k=methods.money(acc1)
            k=methods.money(acc2)
            methods.transfer(acc1,acc2,amount)
        except:
            print("Invalid account details")
        print()
    elif opt==5:
        try:
            account=input("Enter account name: ")
            password=input("Enter password: ")
            k=methods.balance(account,password)[1]
            methods.del_account(account,password)
        except:
            print("Invalid account details")
        print()
    elif opt==6:
        try:
            forgot=int(input("Enter 1 to enter old and new password, Enter 0 to send email if password forgotten: "))
            if forgot==1:
                account=input("Enter account name: ")
                pass1=input("Enter old password: ")
                k=methods.balance(account,pass1)[1]
                while True:
                    pass2=input("Enter new password: ")
                    if methods.pass_strength(pass2):
                        print("Strong password!")
                        break
                    else:
                        print("Weak password! Enter another password")
                methods.change_password(account,pass1,pass2)
            elif forgot==0:
                account=input("Enter account name: ")
                k=methods.display(account)
                msg="This is an email from python bank.\n"+"Your password is "+str(k[2])+"\n Thank you for using our service.\n\n\n\n Please ignore this email if it's not meant for you."
                methods.mail(k[3],'Your forgotten password',msg)
                
        except:
            print("Invalid details")
    elif opt==7:
        print()
        try:
            print("Enter account details to enter casino!")
            account=input("Enter account name: ")
            password=input("Enter password: ")
            k=methods.balance(account,password)[1]
        except:
            print("Wrong account details")
            continue
        print()
        while True:
            print()
            print("Welcome to the casino!")
            print()
            print("Enter 1 for Slot Machine, 2 for Dice Game, 3 for Higher or Lower, 4 for Tossing, 5 for Blackjack, else leave")
            choice=int(input("Enter choice of game: "))
            
            if choice==1:
                print()
                print("Welcome to the Slot Machine! Enter the amount you want to bet!")
                print("If 2 slots are equal then you win your money back and if 3 slots are equal you win twice the amount of the bet!")
                while True:
                    
                    print("You have $",methods.money(account))
                    print("Enter 0 for bet to stop playing")
                    bet=int(input("Enter the amount to bet: "))
                    if bet==0:
                        break
                    else:
                        methods.update(account,-bet)
                    L=["◆","⬤","★"]
                    x=random.choice(L)
                    y=random.choice(L)
                    z=random.choice(L)
                    print(x, y, z)
                    if x==y==z:
                        print("Jackpot!")
                        print("You win $",2*bet)
                        methods.update(account,2*bet)
                    elif x==y or y==z or x==z:
                        print("2 in a row!")
                        print("You get back $",bet)
                        methods.update(account,bet)


            elif choice==2:
                print()
                print("welcome to dice round")
                print("the rules are simple. if you get even number you will get 100 more added, if you get odd you will lose 300")
                while True:
                    play=int(input("Enter 0 to quit or 1 to continue playing: "))
                    i=random.randint(1,6)
                    if i%2==0:
                        print("You earn 100$")
                        methods.update(account,100)
                    elif i%2!=0:
                        print("You lose 300$")
                        methods.update(account,-300)
                    if methods.money(account)<=0 or play==0:
                        print("Game over!")
                        break
                    print(methods.money(account))

            elif choice==3:
                print()
                print("Welcome to Higher or Lower.")
                print("Guess whether a card is higher or lower than your current one ")
                D={"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "Queen":12, "King":13}
                keys = list(D.keys())
                print(keys)
                x=random.choice(keys)
                print("You got a",x)
                while True:
                    y=random.choice(keys)
                    guess=int(input("Enter 1 to guess higher and 0 to guess lower. Else -1 to quit the game: "))
                    print("You got a",y)
                    if D[y]>D[x] and guess==1:
                        print("Higher! You win 100$")
                        methods.update(account,100)
                    elif D[y]<D[x] and guess==0:
                        print("Lower! You win 100$")
                        methods.update(account,100)
                    elif D[y]>D[x] and guess==0 or D[y]<D[x] and guess==1:
                        methods.update(account,-200)
                        print("Wrong! You lose 200$")
                    elif guess==-1 or methods.money(account)<=0:
                        print("You quit Higher or Lower!")
                        break
                    print(methods.money(account))
                    x=y


            elif choice==4:
                print()
                while True:
                    bet=int(input("Enter bet"))
                    if bet==0:
                        break
                    flip=random.randint(1,2)
                    if flip ==1:
                        methods.update(account,bet)
                        print("Heads. You just won " + str(bet) + " dollars.  Your total money is " + str(methods.money(account)) + " dollars remaining.")
                    else:
                        methods.update(account,-bet)
                        print("Tails. You just lost " + str(bet) + " dollars. Your total money is " + str(methods.money(account)) + " dollars remaining.")



            elif choice==5:
                L = ['Spades','Clubs','Diamonds','Hearts']
                D = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'Ace':11,'King':10,'Queen':10,'Jack':10}
                L1= []*21
                while True:
                    bet = int(input("How much do you want to bet?"))
                    if bet > methods.money(account):
                        print("You don't have enough money")
                        continue
                    methods.update(account,-bet)
                    profit = 0
                    v=random.randint(1,13)
                    w=random.randint(1,13)
                    value = 0
                    z=0
                    y=0
                    f = 0
                    for i in D:
                        card1suit = random.choice(L)
                        card1value = D[i]
                        card1name = i
                        z+=1
                        if z == v:
                            L1+=[i]
                            break
                    for i in D:
                        card2suit = random.choice(L)
                        card2value = D[i]
                        card2name = i
                        y+=1
                        if y == w:
                            L1+=[i]
                            break
                    print("Your Cards are:-", card1suit ,card1name, "and" ,card2suit ,card2name)
                    value+= card1value + card2value
                    compvalue= random.randint(2,20)
                    while True:
                        while f == 0:
                            while True:
                                x = input("Do you want to draw or stand?")
                                if x == "Draw" or x== "draw":
                                    v= random.randint(1,13)
                                    z=0
                                    for i in D:
                                        if z == v:
                                            print("You drew", random.choice(L), i)
                                            value+= D[i]
                                            L1+= [i]
                                            print("Value is", value)
                                            break
                                        z+=1
                                elif x == "Stand" or x == "stand":
                                    f=1
                                    break
                                else:
                                    print("That isnt a valid option")
                                    continue
                                break
                            break
                        if compvalue <= 16:
                            while compvalue <= 16:
                                compvalue+= random.randint(1,9)
                            p=9
                        elif compvalue > 16:
                            p =9
                        if value > 21 and compvalue < 21 :
                            a = 0
                            for i in L1:
                                if i == "Ace":
                                    value -=10
                                    a = 1
                                    L1.remove(i)
                                    print("Value of Ace became 1")
                                    break
                            if a == 1:
                                continue
                            elif a == 0:
                                print("Your final Value is",value)
                                print("House Value is",compvalue)
                                print("You bust. House Wins")
                                break
                        elif compvalue > 21 and value < 21 :
                            print("Your final Value is",value)
                            print("House Value is",compvalue)
                            print("House busts. You win")
                            profit += 2*bet
                            break
                        elif value == 21 and compvalue !=21:
                            print("Your final Value is",value)
                            print("House Value is",compvalue)
                            print("Blackjack. You win")
                            profit += 3*bet
                            break
                        elif compvalue == 21 and value !=21:
                            print("Your final Value is",value)
                            print("House Value is",compvalue)
                            print("Blackjack. House wins")
                            break
                        elif compvalue >21 and value>21:
                            a = 0
                            for i in L1:
                                if i == "Ace":
                                    value = value -10
                                    a = 1
                                    print(value)
                                    L1.remove(i)
                                    break
                            if a == 1:
                                print("Your final Value is", value)
                                print("You Win")
                                profit += 2*bet
                                break
                            print("Your final Value is",value)
                            print("House Value is",compvalue)
                            print("You Draw")
                            profit = bet
                            break
                        if p == 9 and f ==1:
                            if value > compvalue:
                                print("Your final Value is",value)
                                print("House Value is",compvalue)
                                print("You win")
                                profit += 2*bet
                                break
                            elif compvalue> value:
                                print("Your final Value is",value)
                                print("House Value is",compvalue)
                                print("House wins")
                                break
                    methods.update(account,profit)
                    print("You have", methods.money(account),"money left.")
                    d= input("Do you want to continue.Yes or No only.")
                    if d == "Yes" or d=="yes":
                        continue
                    elif d == "No" or d=="no":
                        break
                    break
                
                    
            else:
                break

    elif opt==8:
        print()
        try:
            print("Enter account details to enter stock market!")
            account=input("Enter account name: ")
            password=input("Enter password: ")
            k=methods.balance(account,password)[1]
        except:
            print("Wrong account details")
            continue
        print()
        while True:
            print()
            print("Welcome to the stock market!")
            print("TSLA MSFT AAPL GOOG WORK UBER SHOP NVDA NFLX AMD")
            stock=input("Which stock do you want to trade(Enter 0 to exit): ")
            if stock=="0":
                break
            try:
                shares=int(input("How many shares do you want to buy?: "))
                data=yf.Ticker(stock)
                data=data.history(interval='1mo',start='2010-1-1', end='2020-1-1')
                data.to_csv(stock+'results.csv')
            except:
                break
            
            with open(stock+'results.csv','r') as F:
                DL=csv.reader(F)
                next(DL)
                for i in DL:
                    initial=i[2]
                    print("You bought",shares,"shares of",stock,'for',i[2],"per share.")
                    print("1 month later")
                    break
                for i in DL:
                    if i[2]=='':
                        continue
                    print('The current stock price is ',i[2],' do you wish to wait 1 month before selling it?')
                    wait=int(input("Enter 0 to sell stock, 1 to wait,2 to view graph: "))
                    curr_date=i[0]
                    if wait==0:
                        final=i[2]
                        print("You sold",shares,"shares of",stock,'for',float(final)*shares)
                        methods.update(account,shares*(float(final)-float(initial)))
                        break
                    elif wait==2:
                      with open(stock+'results.csv','r') as F:
                        D=csv.reader(F)
                        next(D)
                        x=[]
                        y=[]
                        for j in D:
                            if j[2]=='':
                                continue
                            x+=[j[0]]
                            y+=[float(j[2])]
                            if curr_date==j[0]:
                                break
                        plt.plot(x, y)  
                        plt.xlabel('Date')  
                        plt.ylabel('Stock Price')
                        plt.title(stock) 
                        plt.show()
                        
                            
        

    else:
        break
                



        


