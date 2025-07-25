dic = {"ADD":1,"VIEW":2,"MARK":3,"SORT":4,"EXIT":5}
print("________________________________")
for i in dic:
    print(dic[i],".",i)
print("________________________________")
list_task =[]
def add():
    print("________________________________")
    status = "❌"
    task_name = input("Enter the task name : " )
    date = input("Enter the Date : ")
    priority= input("Enter The Priority (high/medium/low) : ")
    list_task.append({
        "task":task_name,
        "date":date,
        "priority":priority,
        "status":status
    })

    print("task added successfully.............🎉")
    print("________________________________")


def mark():
    task_done = input("Enter The Task Name You Want To Mark As Done : ")
    for key in list_task:
        if key["task"]==task_done:
            key["status"]="👍"
            print("Your Task is Marked As Done")

def view():
    print("________________________________")
    for key in list_task:
        for i in key:
            print("Task Name - ",key["task"],"|","Date - ",key["date"],"|","Priority - ",key["priority"],"Status - ",key["status"])
            break
    print("________________________________")

def sort():
    print("______________________________________")
    for key in list_task:
        for value in key:
            if key["priority"]=="high":
                print(key["task"], "|", key["date"], "|", key["priority"], key["status"])
                break
    for key in list_task:
        for value in key:
            if key["priority"]=="medium":
                print(key["task"], "|", key["date"], "|", key["priority"], key["status"])
                break
    for key in list_task:
        for value in key:
            if key["priority"] == "low":
                print(key["task"], "|", key["date"], "|", key["priority"], key["status"])
                break

condition = True
while condition == True:
    option  = int(input("Enter your option : "))
    if option == 1:
        add()
    elif option==2:
        view()
    elif option == 3:
        mark()
    elif option==4:
        sort()
    elif option==5:
        condition= False
    else:
        print("enter the valid input....")
