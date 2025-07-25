# PROGRAM - 1 ATM MACHINE

service ={"deposit":1,"withdraw":2,"balance":3,"exit":4}
for key in service:
    print(service[key],".",key)
print("------------ATM------------------")
name =input("Enter your Name  : ")
account ={}

def deposit():
    amount =float(input("Enter the Amount to deposit : "))
    account["amount"] =amount
    print("Your amount is deposited successfully.....")

def withdraw():
    print("_________________________________________")
    withdraw_amount = float(input("enter your withdraw amount :"))
    if withdraw_amount % 100 ==0 or withdraw_amount % 500==0:
        for key in account:
            if withdraw_amount < account[key]:
                account[key] -= withdraw_amount
                print("Amount is withdraw successfully.....")
            else:
                print("insufficient Balance")
    else:
        print("enter the amount only multiple of 100")

    print("____________________________________________")

def balance():
    print("----------------------account balance----------------- ")
    for key in account:
        print("your account balance  : ",account[key])
    print("_______________________________________________________")



condition =True
while condition==True:
    option= int (input("Enter your Option : "))
    if option ==1:
        deposit()
    elif option==2:
        withdraw()
    elif option==3:
        balance()
    elif option==4:
        condition=False
    else:
        print("enter the valid option....")
