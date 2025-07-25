
service = {"add income(or)expense": 1, "view summary": 2, "track by category":3,"exit": 4}
print("------Personal Finance Manager--------")

i = 0
for key in service:
    i += 1
    print(i, ". ", key)
print("___________________________________")


list_entry=[]
def income_info():
    date = input("Enter Date (DD-MM-YYYY) : ")
    category = input("Enter The Category (Food,Rent,Salary) : ")
    amount = int(input("Enter Amount : "))
    option = input("Enter Income / Expense : ").lower()
    print(f"Your {option} Entry Is Add Successfully")

    list_entry.append({
          "date":date,
          "category":category,
          "amount":amount,
          "option":option
      })


def summary():
    income_total = 0
    expense_total = 0
    category_expense = {}
    high = 0
    high_cat =""
    for key in list_entry:
        if key["option"] == "income":
            income_total += key["amount"]
        elif key["option"]=="expense" :
            expense_total += key["amount"]
            if key["category"] in category_expense:
                category_expense[key["category"]] += key["amount"]
            else:
                category_expense[key["category"]] = key["amount"]

    for key in category_expense:
        if high < category_expense[key]:
            high = category_expense[key]
            high_cat = key



    net_balance = income_total-expense_total
    print("Total Income : ",income_total)
    print("Expense Total  : ",expense_total)
    print("NET Balance : ",net_balance)
    print(f"Top Expense - {high_cat} :",high)

def track_user():

    track = input("enter category : ")
    for key in list_entry:
        if track==key["category"]:
            print(f"{key["date"]} - {key["option"]}  -{key["category"]} - {key["amount"]}")


condition = True
while condition == True:
    choice = int(input("Enter Your Choice (1-3) : "))

    if choice == 1:
        income_info()

    elif choice == 2:
        print("_________________________")
        summary()
        print("__________________________")
    elif choice==3:
        track_user()

    elif choice == 4:
        condition = False