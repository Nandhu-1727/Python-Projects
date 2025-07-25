print("-----CALCULATOR-----")
print()
print("Calculator Operations")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.History")
print("6.Clear history")
print("7.Exit")
list1=[]

name = input("Enter the Name: ")
def addition():
    print("YOU ARE CHOOSE TO ADDITION OPERATION")
    num1 = int(input("Enter the num1 : "))
    num2 = int(input("Enter the num2 : "))
    ans=num1+num2
    print(f"{num1} + {num2} : {ans}")
    list1.append([num1,"+",num2,"=",ans])

def sub():
    print("YOU ARE CHOOSE TO SUBSTRACTION OPERATION")
    num1 = int(input("Enter the num1 : "))
    num2 = int(input("Enter the num2 : "))
    ans=num1-num2
    print(f"{num1} - {num2} : {ans}")
    list1.append([num1,"-", num2,"=",ans])


def mul():
    print("YOU ARE CHOOSE TO MULTIPLICATION OPERATION")
    num1 = int(input("Enter the num1 : "))
    num2 = int(input("Enter the num2 : "))
    ans=num1*num2
    print(f"{num1} * {num2} : {ans}")
    list1.append([num1,"*", num2,"=",ans])
def div():
    print("YOU ARE CHOOSE TO DIVISION OPERATION")
    num1 = int(input("Enter the num1 : "))
    num2 = int(input("Enter the num2 : "))
    ans=num1/num2
    print(f"{num1} / {num2} : {ans}")
    list1.append([num1,"/", num2,"=",ans])

def history():
    print(f"---{name} HISTORY---")
    for i in list1:
        for key in  i:
            print(key,end="")
        print()
def clear():
    list1.clear()
    print("Your history is cleared")


while True:

    choice=(input("Enter the choice in the calculator operation: "))


    if choice=="1":
        addition()
    elif choice=="2":
        sub()
    elif choice=="3":
        mul()
    elif choice=="4":
        div()
    elif choice=="5":
        history()
    elif choice=="6":
        clear()
    elif choice=="7":
        exit()
    else:
        print("Enter the valid choice")