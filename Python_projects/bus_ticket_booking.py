print("---Welcome to the Bus Seat Booking System---")
print()
print("Available seats (0-Available  X-Booked)")
print("_________________________________________")
print()

rows=10
cols=4
seats=[["0"for _ in range(cols)]for _ in range(rows)]
def display():
    print("R|c",end=" ")
    for c in range(cols):
        print(f"C{c}",end=" ")
    print()
    for r in range(rows):
        print(f"R{r}",end="  ")
        for col in range(cols):
            print(seats[r][col],end="  ")
        print()

while True:
    display()
    print()
    print("0 - Available  X - Booked")
    print("_________________________________________")
    print()
    booking=int(input("How many seats would you like to book(Enter 0 to exit) : "))
    if booking==0:
       break
    for i in range(booking):
                seat_row=int(input("Enter the seat row number [1 to 4](Enter 0 to exit): "))
                seat_col=int(input("Enter the seat column number[1 to 3](Enter 0 to exit) : "))
                if seat_row==0 and seat_col==0:
                    break
                elif seat_row>5 or seat_col>5:
                    print("Enter the valid Seat number ")
                if seats[seat_row][seat_col]=="X":
                    print("Seat is Already Booked!!! ")
                else:
                    seats[seat_row][seat_col]="X"
                    print(f"Great !!! Your R{seat_row}C{seat_col} Seat is Booked🎉")
                    print("________________________________________________")

    display()
    break