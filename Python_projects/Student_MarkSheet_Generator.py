h_mark=0
h_tamil=0
h_english=0
h_maths=0
high_total=""
high_tamil_mark=""
high_english_mark=""
high_maths_mark=""

print("----Student Result Sheet Generator---- ")
print()
list1=[]
mark_total = {}
student=int(input("Enter the number of Students(enter 0 to exit): "))
for i in range(student):
          if student==0:
            break
          name=input("Enter the name: ")
          sub1=int(input("Enter the Tamil subject mark: "))
          sub2=int(input("Enter the English Subject mark: "))
          sub3=int(input("Enter the Maths Subject mark: "))
          print("------------------------")
          total=sub1+sub2+sub3
          average_mark=total//3
          mark_total[name]=total
          if average_mark>80:
              grade="A"
          elif average_mark>65:
              grade="B"
          elif average_mark>50:
              grade="C"
          elif average_mark>35:
              grade="D"
          else:
              grade="Fail"
          list1.append(
              {"Student_name": name, "Tamil": sub1, "English": sub2, "Maths": sub3, "total": total,
               "average_mark": average_mark, "Grade": grade})
          detail={"Student_name":name,"Tamil":sub1,"English":sub2,"Maths":sub3 ,"Total":total,"Average_mark":average_mark,"Grade":grade}
          for key, values in detail.items():
               print(key, " - ", values)
          print("------------------------")


for key in mark_total:
              if h_mark<mark_total[key]:
                  h_mark=mark_total[key]
                  high_total=key
for key in list1:
    if h_tamil<key["Tamil"]:
        h_tamil=key["Tamil"]
        high_tamil_mark=key["Student_name"]

for key in list1:
    if h_english<key["English"]:
        h_english=key["English"]
        high_english_mark=key["Student_name"]

for key in list1:
    if h_maths<key["Maths"]:
        h_maths=key["Maths"]
        high_maths_mark=key["Student_name"]

print(f"Topper is {high_total} - ",h_mark)
print(f"Tamil highest mark is {high_tamil_mark} - ",h_tamil)
print(f"English highest mark is {high_english_mark} - ",h_english)
print(f"Maths highest mark is {high_maths_mark} - ",h_maths)
print("-------------------------------------")
