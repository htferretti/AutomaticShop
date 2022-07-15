#made by @htferretti

#here are your products, follow this sitaxe:
#productX = {"product": "PRODUCT'S  NAME", "price": PRODUCT'S  PRICE , "description": "PRODUCT'S  DESCRIPTION"}
blackCoffee = {"product": "Black Coffee", "price": 3 , "description": "Simple black coffee."}
espresso = {"product": "Espresso", "price": 4 , "description": "Espresso."}
mocha = {"product": "Mocha", "price": 5 , "description": "Coffe + Chocolate!"}
matcha = {"product": "Matcha", "price": 8 , "description": "Milk + Tea!"}

#then add your product inside the []
menu = [blackCoffee, espresso, mocha, matcha]

#mesages, edit them as you want
welcome = "Welcome to Henrique's Café!"
goodbye = "Thank you for comming to Henrique's Café!"
errorMsg = "WRITE A VALID NUMBER"

#here is the code, don't touch :D
def home():
    total = 0
    print('')
    print(welcome)
    print("Enter with the product code:\n")

    order(total)

def order(total):
    num = 0
    while num < len(menu):
        print(str(num) + " " + menu[num]['product'] + "   " + str(menu[num]['price']) + "$" + "     " + menu[num]['description'])
        num = num + 1

    print("\nWrite " + str(num) + " to cancel order.")

    if total != 0:
        print("Write " + str(num + 1) + " to finish order.")
        print("\nTotal: " + str(total) + "$")

    inputOrder = input("\n")
    try:
        int(inputOrder)
        if int(inputOrder) < 0 or int(inputOrder) > (num + 1):
            print(errorMsg)
            order(total)
        else:
            add(inputOrder, total, num)
    except:
        print(errorMsg)
        order(total)

def add(inputOrder, total, num):
    if inputOrder == str(num):
        print("Order canceled.")
    elif total != 0 and inputOrder == str(num + 1):
        print(goodbye)
    else:
        total = total + menu[int(inputOrder)]['price']
        order(total)
home()