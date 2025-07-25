#print=A:

for row in range(6):
    for col in range(6):
        if col!=row and col==0 or col==5 and row!=0 or 0 < col <5 and row==0 or row==3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=B:

for row in range(7):
    for col in range(7):
        if col==0 or row==3 and col!=6 or row==0 and col!=6 or row==6 and col!=6 or col==6 and row!=0 and row!=3 and row!=6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()



#print=C:

for row in range(6):
    for col in range(6):
        if col==0 and row!=0 and row!=5  or row==0 and col!=0 or (row==5 and col!=0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=D:

for row in range(7):
    for col in range(7):
        if col==0 or row==0 and col!=6 or row==6 and col!=6 or row==1 and col==6 or col==6 and row!=6 and row!=0 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=E:

for row in range(7):
    for col in range(7):
        if col==0 or row==0 or row==3 or row==6 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=F:

for row in range(7):
    for col in range(7):
        if col==0 or row==0 or row==3  :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=G:

for row in range(7):
    for col in range(7):
        if row==0 and col!=0 or col==0 and row!=0 or row==6 and col!=4 and col!=5 and col!=6 or col==3 and row!=1 and row!=2 and row!=3 or row==4 and col!=1 and col!=2 or col==6 and row!=1 and row!=2 and row!=3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=H:

for row in range(7):
    for col in range(7):
        if col==0 or row==3 or col==6  :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=I:

for row in range(7):
    for col in range(7):
        if row==0 or row==6 or col==3  :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=J:

for row in range(7):
    for col in range(7):
        if row==0 or col==3 or row==6 and col!=4 and col!=5 and col!=6 and col!=0 or col==0 and row!=1 and row!=2 and row!=3 and row!=6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=K:

for row in range(7):
    for col in range(7):
        if col==0 or row==0 and col==5 or row==1 and col==4 or row==2 and col==3 or row==3 and col==1 or row==3 and col==2 or row==4 and col==3 or row==5 and col==4 or row==6 and col==5 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=L:

for row in range(7):
    for col in range(7):
        if col==0 or row==6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=M:

for row in range(7):
    for col in range(7):
        if col==0 or col==6 or row==1 and col==1 or row==2 and col==2 or row==3 and col==3 or row==2 and col==4 or row==1 and col==5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=N:
for row in range(7):
    for col in range(7):
        if col==0 or col==6 or row==col:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=O:

for row in range(7):
    for col in range(7):
        if col==0 and row!=0 and row!=6 or col==6 and row!=0 and row!=6 or row==0 and col!=0 and col!=6 or row==6 and col!=0 and col!=6 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=P:

for row in range(7):
    for col in range(7):
        if col==0 or row==0 and col!=6 or row==3 and col!=6 or col==6 and row!=4 and row!=0 and row!=5 and row!=6 and row!=3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print:Q


for row in range(7):
    for col in range(7):
        if (col==0 and row!=0 and row!=5 and row!=6) or (row==0 and col!=0 and col!=6) or (col==6 and row!=0 and row!=4 and row!=5 and row!=6) or (row==5 and col!=0 and col!=6 and col!=5 ) or (row==3 and col==4)or (row==4 and col==5) or (row==5 and col==6) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()


#print=R:
for row in range(7):
    for col in range(7):
        if col==0 or (row==0 and col!=6) or (row==3 and col!=6) or (col==6 and row==1) or (col==6 and row==2) or (row==4 and col==3) or (row==5 and col==4) or (row==6 and col==5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=S:
for row in range(7):
    for col in range(7):
        if row==0 and col!=0 or (col==0 and row==1) or (col==0 and row==2)or (row==3 and col!=0) or(row==3 and col!=6) or(col==6 and row==4) or(col==6 and row==5) or (row==6 and col!=6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=V:

for row in range(7):
    for col in range(7):
        if col==0 and row==0 or col==1 and row==2 or col==2 and row==4 or col==3 and row==6 or col==4 and row==4 or col==2 and row==4 or col==5 and row==2 or col==6 and row==0 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=U:
for row in range(7):
    for col in range(7):
        if col==0 and row!=6 or col==6 and row!=6 or row==6 and col!=0 and col!=6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=W:

for row in range(7):
    for col in range(7):
        if col==0 or col==6 or (row==5 and col==2) or (row==4 and col==3) or (row==5 and col==4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=X:

for row in range(7):
    for col in range(7):
        if col==row or (col==6 and row==0) or (col==5 and row==1) or (col==4 and row==2) or (col==3 and row==3) or (col==4 and row==2) or (row==6 and col==0) or (row==5 and col==1) or (row==4 and col==2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=Y:

for row in range(7):
    for col in range(7):
        if col==3 and row!=0 and row!=1 and row!=2 or (row==0 and col==0) or(row==1 and col==1) or (row==2 and col==2) or (col==6 and row==0) or (col==5 and row==1) or (col==4 and row==2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
print()

#print=Z:

for row in range(7):
    for col in range(7):
        if row==0 or row==6 or (row==5 and col==1) or (row==4 and col==2) or (row==3 and col==3) or (col==5 and row==1) or (col==4 and row==2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


