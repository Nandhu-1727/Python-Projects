print("----Welcome to the NK Library----")
print()
print("________________________")
print("   Choose the Choice    ")
print("1.Display books")
print("2.Add Book")
print("3.Borrow")
print("4.Return")
print("5.Borrow List")
print("6.Exit")
print("________________________")
print()
book={"cloud":3,"aws":5,"fds":5,"oops":6,"data":2}
stocks={}
name=input("Enter the name: ")

def display_books():
  print("Available Books In Library")
  print("B|Q    The list of books:")
  for key,values in book.items():
    print(values," - ",key)
def add_book():
    b_name=input("Enter the book name: ").lower()
    b_quanty=int(input(f"Enter how many {b_name} book added: "))
    if b_name in book:
            book[b_name]+=b_quanty
    else:
        book[b_name]=b_quanty

def borrow():

        num_book=int(input("How many books do u want to borrow (Max - 4): "))
        for i in range(num_book):
           book_id = (input("Enter the Book name : ")).lower()
           if book_id in book:
               print(f"Your {book_id} book is borrowed")
               book[book_id]-=1
               stocks[book_id]=1

def return_book():
    r_book=int(input("Enter how many books do u want to return: "))
    for i in range(r_book):
        b_name=input("Enter the book name: ").lower()
        for key in stocks:
            print(f"{b_name} is returned")
            stocks[b_name]=stocks[b_name]-1
            book[b_name]=book[b_name]+1
            break


def user_list():
    print(f"{name} borrowed list")
    for i in stocks:
        print(i,"-",stocks[i])

while True:
    choice=int(input("Enter the Choice : "))
    if choice==1:
        display_books()
        print("______________________")
    elif choice==2:
        add_book()

    elif choice==3:
        borrow()

    elif choice==4:
        return_book()

    elif choice==5:
        user_list()

    elif choice==6:
        exit()




