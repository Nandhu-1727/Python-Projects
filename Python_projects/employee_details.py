service = {"ADD EMPLOYEE":1,"DISPLAY PAY SLIP":2,"EXIT":3}
employee_list =[]
print("----------- MENU --------------")
print("_____________________________")
for key in service:
    print(service[key],".",key)
print("______________________________")

def add_emp():
    name = input("Enter The Employee name : ")
    id = int(input("Enter The Employee ID : "))
    basic_salary = float(input("Enter The Basic Salary Of The Employee : "))
    employee_list.append({
        "name":name,
        "id":id,
        "salary":basic_salary
    })
    print("EMPLOYEE ENTRY ADDED SUCCESSFULLY........")
    print("__________________________________________")

def pay_slip():
    print("______________________________")

    for key in employee_list:
        if 50000 > key["salary"] >= 30000:
            da = key["salary"] * 0.1
            hra =key["salary"]*0.20
            pf = key["salary"]*0.12
            tax = key["salary"]*0.1
            net_salary = (key["salary"] + hra - da - pf - tax) + dis
            print(f"----------PAY SLIP {key["name"].upper()}  -----------")
            print("__________________________________")
            print("EMPLOYEE NAME : ", key["name"])
            print("BASIC SALARY : ", key["salary"])
            print("HRA (20%): $", hra)
            print("DA (10%): $", da)
            print("PF (12%): $", pf)
            print("TAX (10%): $", tax)
            print("NET SALARY : $", net_salary)
            print("______________________________")
        elif key["salary"] >= 50000:
                dis = key["salary"] * 0.1
                net_salary = key["salary"] + dis
                hra,da,tax,pf = 0,0,0,0
                print(f"----------PAY SLIP {key["name"].upper()}  -----------")
                print("__________________________________")
                print("EMPLOYEE NAME : ", key["name"])
                print("BASIC SALARY : ", key["salary"])
                print("HRA (20%) : $", hra)
                print("DA (10%) : $", da)
                print("PF (12%) : $", pf)
                print("TAX (10%) : $", tax)
                print("DISCOUNT (10%) : $",dis)
                print("NET SALARY : $", key["salary"]+dis)
                print("______________________________")
        else:
            hra,da,tax,pf=0,0,0,0
            print(f"----------PAY SLIP {key["name"].upper()}  -----------")
            print("__________________________________")
            print("EMPLOYEE NAME : ", key["name"])
            print("BASIC SALARY : ", key["salary"])
            print("HRA (20%) : $", hra)
            print("DA (10%) : $", da)
            print("PF (12%) : $", pf)
            print("TAX (10%) : $", tax)
            print("NET SALARY : $",key["salary"])
            print("______________________________")


condition = True
while condition==True:
    option = int(input("Enter the Option In The Menu : "))
    if option==1:
        add_emp()
    elif option == 2:
        pay_slip()
    elif option==3:
        condition =False
    else:
        print("ENTER VALID OPTION......")
