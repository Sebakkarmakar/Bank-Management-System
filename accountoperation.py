from matplotlib.backend_tools import cursors
from numpy import insert
from dbconfig import connect
def create_account():
    name=input("Please Enter your name")
    email=input("Enter your Email")
    balance=eval(input("enter your opening balance"))
    db=connect()
    cursor=db.cursor()
    sql= "INSERT INTO accounts(name, email, balance) VALUES (%s, %s, %s)"
    values=(name,email,balance)
    cursor.execute(sql,values)
    db.commit()
    print("Account created succefully")
    db.close()
def view_account():
    db=connect()
    cursor=db.cursor()
    cursor.execute("select * from accounts")
    accounts=cursor.fetchall()
    print("All Accounts")
    for i in accounts:
        print(f"id:{i[0]},name:{i[1]}, email: {i[2]}, balance:{i[3]}")
    db.close()
def deposit_amount():
    acc_id=int(input("enter the acc_id"))
    amount=eval(input("enter the amount"))
    db=connect()
    cursor=db.cursor()
    cursor.execute("update accounts set balance = balance + %s where id = %s",(amount,acc_id))
    db.commit()
    print("The amount deposit succesfully......")
    db.close()
def withdrawl_amount():
    acc_id=int(input("Enter the acc_id"))
    amount=eval(input("enter how much money you want to  withdrawl"))
    db=connect()
    cursor=db.cursor()
    cursor.execute("select balance from accounts where id=%s",(acc_id,))
    ans=cursor.fetchone()
    if ans and ans[0]>=amount:
        cursor.execute("update accounts set balance=balance - %s where id =%s",(amount,acc_id))
        db.commit()
        print("Withdrawl Successfully")
    else:
        print("Insufficicant Balance in your account....")
  
    db.close()
def check_balance():
    acc_id=int(input("enter the id"))
    db=connect()
    cursor=db.cursor()
    cursor.execute("select name, balance from accounts where id=%s",(acc_id,))
    result=cursor.fetchone()
    if result:
        print(f"Account holder:{result[0]}, Balance:{result[1]}")
    else:
        print("Account Not found!!!!!!!")
    db.close()

