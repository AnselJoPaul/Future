import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="ansel",database="store")
if conn.is_connected():
        print('')
c1=conn.cursor()
def createcloth():
        try:
                q='create table cloth(items varchar(20), qty int)'
                c1.execute(q)
        except:
                print('table exists')
createcloth()
def createcomment():
        try:
                q='create table comment(comment varchar(100))'
                c1.execute(q)
        except:
                print('table exists')
createcomment()
def createlogin():
        try:
                q='create table login(user_id int,passwd int)'
                c1.execute(q)
        except:
                print('table exists')
createlogin()
def createproblems():
        try:
                q='create table problems(rate_issues int,write_problems varchar(100))'
                c1.execute(q)
        except:
                print('table exists')
createproblems()
def createprice():
        try:
                q='create table price(items varchar(20),price int)'
                c1.execute(q)
        except:
                print('table exists')
createprice()
c1.execute('use store')
print('-'*140)
print(" "*70,"SAY CHEAP")
print(' ')
from time import gmtime,strftime
a=strftime("%a,%d%b%y",gmtime())
print(" "*69,a)
print('-'*140)
print(' ')
print("1.LOGIN")
print("2.TO CREATE ACCOUNT")
print("")
print('')
choice=int(input("ENTER YOUR CHOICE:"))
print(' ')
if choice==1:
    a=int(input("ENTER YOUR USER ID(in nos)."))
    c1.execute("select passwd from login where user_id = "+str(a)+" ;")
    data=c1.fetchall()
    data=data[0]
    data=list(data)
    data=data[0]
    data=str(data)
    print(' ')
    b=int(input("ENTER PASSSWORD:"))
    conn.cursor()
    conn.commit()
if choice==2:
    print('TO CREATE YOUR ACCOUNT PLEASE ENTER YOUR USER ID AND PASSWORD....')
    c1=conn.cursor()
    print('')
    name=input("YOUR FULL NAME PLEASE:")
    print('')
    user_id=input("CHOOSE YOUR ID:")
    print('')
    passwd=int(input("CREATE YOUR PASSWORD (in integer):"))
    print('')
    c1=conn.cursor()
    upd="insert into login values('"+user_id +"',"+ str(passwd)+")"
    c1.execute(upd)
    conn.commit()
    print("ACCOUNT CREATED")
print('')
print('-'*140)
print('')
print("※ IF SHOPPING IS DONE ENTER 1.")
print("※ IF YOU LIKE TO FILE A MARKETING PROBLEM ENTER 2.")
print("※ IF NO SHOPPING IS DONE ENTER 3.")
print('')
choice=int(input("PLEASE ENTER YOUR CHOICE="))
if choice==1:
    customer_name=input("ENTER YOUR NAME:")
    items=input("ENTER ITEM NAME:")
    qty=int(input("ENTER QUANTITY:"))
    SQL_INSERT="insert into cloth values('"+items+"',"+str(qty)+")"
    c1.execute(SQL_INSERT)
    q="select * from price where items='{}'".format(items,)
    c1.execute(q)
    x=c1.fetchall()
    a=x[0][1]
    p=qty*a
    print('PRICE=₹',p)
    print("THANK YOU.....FOR YOUR VISIT.HAVE A GOOD DAY!!! ")
if choice==2:
    c1.execute('use store')
    rate_issue=int(input("RATE YOUR DIFFICULTIES OUT OF 10="))
    write_problem=input("PLEASE CONVEY YOUR PROBLEM:")
    SQL_INSERT="insert into problems values("+str(rate_issue)+",'"+write_problem+"')"
    c1.execute(SQL_INSERT)
    print("Your problem will be rectified.SORRY for your inconvience....THANK YOU.")
if choice==3:
    c1.execute('use store')
    comment=input("COMMENTS ABOUT OUR STORE PLEASE:")
    SQL_insert="insert into comment values('"+comment+"')"
    c1.execute(SQL_insert)
    print("THANK YOU FOR YOUR VISIT ....HAVE A GOOD DAY.")
    print('-'*140) 
conn.commit()

