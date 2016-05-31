list = []

print("Welcome to shopping list")
add = input("Do you want to add something to your shopping list? (Yes/No) ")

while add == "Yes" or add == "yes" or add == "y" or add == "Y":
    item = input("Please enter an item: ")
    list.append(item)
    add = input("Do you want to add another item? (Yes/No) ")

if add == "No" or add == "no" or add == "N" or add == "n":
    print("This is your shopping list:")
    print(list)
    print("Thanks for visiting!")

else:
    print("Invalid input try again!")



