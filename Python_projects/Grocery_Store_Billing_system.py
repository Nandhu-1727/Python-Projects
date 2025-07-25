print("---Welcome to the NK Fruit Shop---")
print()
fruits={'mango':100,'apple':100,'banana':20,'grapes':60,'dragon_fruit':200,'papaya':40,'orange':60}
basket={}
for i in fruits:
    print(i,"- :$",fruits[i])
print("------------------------------")
print("List of Fruits Do you want to Buy!!!")
while True:
    item=input("Enter the fruit do you like to buy(checkout to end): ").lower()
    if item=="checkout":
        break
    elif item in fruits:
        quan=int(input("Enter the Quantity :"))
        if item in basket:
            basket[item] += quan
        else:
            basket[item]=quan
    else:
        print("Enter the Valid Fruit name in List!!!")

print()
print("-----------------")

item_total=0
print(" Item    Quantity    Price ")
for i,qty in basket.items():
    price=fruits[i]
    total=price*qty
    item_total+=total
    print(i,"     ",qty,"   :  ",fruits.get(i))


gst=0.1*item_total
total_bill=gst+item_total
print("---------------------------")
print()
print("Item_Total : ",item_total)
print("GST : ",gst)
print("---------------------------")

print("Total_Bill : ",total_bill)


print("---------------------------")
print("Thanks for Visiting !!! Come Again !!!")





