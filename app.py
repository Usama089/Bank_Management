# start xxamp, then run apache and mysql ,
# if sql gives error stop sql from taskmanager(as administator) > services > stop mysql

# then go to xxamp shell and enter mysql -uroot -p password: press_enter

import pymysql

con=None
cur=None

def connectDB():
    global con,cur
    con=pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='bank',
        )
    cur=con.cursor()

def disconnectDB():
    con.close()
    cur.close()

def OpenAcc():
    connectDB()
    n = input("Enter Your Name: ")
    ac = int(input("Enter Account Number: "))
    db = input("Enter Date Of Birth(YYYY-MM-DD): ")
    ad = input("Enter Address: ")
    p = input("Enter Phone Number: ")
    ob = int(input("Enter Opening Balance: "))
    data1=(n,ac,db,ad,p,ob)
    data2=(n,ac,ob)
    query1='insert into account values(%s,%s,%s,%s,%s,%s)'
    query2='insert into amount values(%s,%s,%s)'
    c = con.cursor()
    c.execute(query1,data1)
    c.execute(query2,data2)
    con.commit()
    print('')
    print("Account Created Successfully.")
    print('_________________________________________________')
    disconnectDB()

def DepositAmo():
    connectDB()
    am = int(input("Enter Amount: "))
    ac = input("Enter Account No: ")
    a = 'select Balance from amount where AccNo=%s'
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam = myresult[0]+am
    query='update amount set Balance=%s where AccNo=%s'
    d=(tam,ac)
    c.execute(query,d)
    con.commit()
    print('')
    print("Amount Credited.")
    print('_________________________________________________')
    disconnectDB()

def WithdrawAmo():
    connectDB()
    am = int(input("Enter Amount: "))
    ac = input("Enter Account Number: ")
    a = 'select Balance from amount where AccNo=%s'
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    query='update amount set Balance=%s where AccNo=%s'
    d = (tam,ac)
    c.execute(query,d)
    con.commit()
    print('')
    print("Money Debited.")
    print('_________________________________________________')
    disconnectDB()

def AccountBal():
    connectDB()
    ac = input("Enter Account Number: ")
    query = 'select Balance from amount where AccNo=%s'
    data=(ac,)
    c = con.cursor()
    c.execute(query,data)
    myresult=c.fetchone()
    print('')
    print("Balance of account number:",ac,"is",myresult[0],"rupees")
    print('_________________________________________________')
    disconnectDB()
    
def DispAccDetail():
    connectDB()
    ac = input("Enter Account Number: ")
    query = 'select * from account where AccNo=%s'
    data = (ac,)
    c = con.cursor()
    c.execute(query,data)
    myresult=c.fetchone()
    for i in myresult:
        print('')
        print(i,end=" ")
    print('_________________________________________________')
    disconnectDB()

def CloseAcc():
    connectDB()
    ac = input("Enter Account Number: ")
    query1='delete from account where AccNo=%s'
    query2='delete from amount where  AccNo=%s'
    data=(ac,)
    c = con.cursor()
    c.execute(query1,data)
    c.execute(query2,data)
    con.commit()
    print('')
    print("Account Closed.")
    print('_________________________________________________')
    disconnectDB()

while(True):
    print('''
1.Open New Account
2.Deposit Amount
3.Withdraw Amount
4.Balance Enquiry
5.Display Customer Details
6.Close Account
7.Exit
''')
    choice=int(input("Enter your choice: "))
    if choice==1:
        OpenAcc()
    elif choice==2:
        DepositAmo()
    elif choice==3:
        WithdrawAmo()
    elif choice==4:
        AccountBal()
    elif choice==5:
        DispAccDetail()
    elif choice==6:
        CloseAcc()
    elif choice==7:
        break
    else:
        print('')
        print("Wrong Choice Entered.")
        print('_____________________________________________')
