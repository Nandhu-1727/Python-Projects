print("-----Student Attendance System-----")
print()
print("1.Entries  Student list ")
print("2.view Summary")
print("3.Monthly Summary")
print("4.Exit")
print()

list1=[]


def stu_attend():
    while True:
        name=input("Enter the Name of the student[Enter done to finish attendance]: ").lower()
        if name=="done":
            break
        date=input("Enter the date: ")
        present_absent=input("Enter present or absent (Present / Absent): ").lower()
        present = 0
        absent = 0
        if present_absent=="present":
            present+=1
            absent+=0
        elif present_absent=="absent":
            absent += 1
            present+=0
        list1.append({
            "student":name,"date":date,"present_absent":present_absent
        })

def view_summary():
    stu_name=input("Enter the student name: ")
    for key in list1:
        if key["student"]==stu_name:
            print(key["date"]," - ",key["present_absent"])

def month_summary():
    print("------------------Monthly Summary--------------")
    month_list = {}
    for key in list1:
        name = key["student"]
        if name not in month_list:
            month_list[name] = {"present":0,"absent":0}
        if key["present_absent"] =="present":
            month_list[name]["present"] +=1
        else:
            month_list[name]["absent"] +=1

    for key in month_list:
        print(key, "- Presents:", month_list[key]["present"], ", Absents:", month_list[key]["absent"])
    print("")


while True:
    option=(input("Enter the Option: "))
    if option=="1":
        stu_attend()
    elif option=="2":
        view_summary()
    elif option=="3":
        month_summary()
    elif option=="4":
        exit()
    elif option=="":
        print("Enter the num between 1 to 4")

    else:
        print("Invalid input")