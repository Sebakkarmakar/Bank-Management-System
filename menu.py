from accountoperation import *
def menu():
    while True:
        print("\ Bank Management System")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Deposit Amount")
        print("4.Withdrawl Amount")
        print("5. Check Balance")
        print("6. Exit")
        choice=int(input("Enter your choice"))
        if choice==1:
            create_account()
        elif choice==2:
            view_account()
        elif choice==3:
            deposit_amount()
        elif choice==4:
            withdrawl_amount()
        elif choice==5:
            check_balance()
        elif choice==6:
            print("Exist from Bank system ..... Thank you !!!!!")
            break
        else:
            print("Invalid Choice Please correct choice........ ")
