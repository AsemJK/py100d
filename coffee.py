#day 15
#build a coffe machine

#3 hot drinks
from operator import index, indexOf


drinks = ['TURKISH', 'ESPRESSO', 'LATTE']

levels = {"water":300,"milk":200,"coffee":120}
ingredients = {"TURKISH":{"Water":50,"Milk":20,"Coffee":10},
                "ESPRESSO":{"Water":25,"Milk":0,"Coffee":18},
                "LATTE":{"Water":25,"Milk":150,"Coffee":24}}
prices = {"TURKISH":57,"ESPRESSO":76,"LATTE":55}

while True:
    ordered_drink = input("What would you like to ask? ")
    if(ordered_drink == "report"):
        print(levels)
        continue
    elif(ordered_drink == "off"):
        terminate = True
        break

    ordered_drink = ordered_drink.upper()
    item_index = -1;
    item_index = drinks.index(ordered_drink)
    print('You ordered',drinks[item_index])

    if(item_index == -1):
        print("Not available")
    elif(drinks[item_index] == "TURKISH"):
        print("Turkish")
        if(levels["water"] < ingredients["TURKISH"]["Water"]):
            print("Not enough water")   
        elif(levels["milk"] < ingredients["TURKISH"]["Milk"]):
            print("Not enough milk")
        elif(levels["coffee"] < ingredients["TURKISH"]["Coffee"]):
            print("Not enough coffee")
        else:
            print("Here is your Turkish")
            print("Price is",prices["TURKISH"])
            levels["water"] -= ingredients["TURKISH"]["Water"]
            levels["milk"] -= ingredients["TURKISH"]["Milk"]
            levels["coffee"] -= ingredients["TURKISH"]["Coffee"]
            print(levels,"\n")
    elif(drinks[item_index] == "ESPRESSO"):
        print("Espresso")
        if(levels["water"] < ingredients["ESPRESSO"]["Water"]):
            print("Not enough water")
        elif(levels["milk"] < ingredients["ESPRESSO"]["Milk"]):
            print("Not enough milk")
        elif(levels["coffee"] < ingredients["ESPRESSO"]["Coffee"]):
            print("Not enough coffee")
        else:
            print("Here is your Espresso")
        levels["water"] -= ingredients["ESPRESSO"]["Water"]
        levels["milk"] -= ingredients["ESPRESSO"]["Milk"]
        levels["coffee"] -= ingredients["ESPRESSO"]["Coffee"]
        print(levels,"\n")
    elif(drinks[item_index] == "LATTE"):
        print("Latte")
        if(levels["water"] < ingredients["LATTE"]["Water"]):
            print("Not enough water")
        elif(levels["milk"] < ingredients["LATTE"]["Milk"]):
            print("Not enough milk")
        elif(levels["coffee"] < ingredients["LATTE"]["Coffee"]):
            print("Not enough coffee")
        else:
            print("Here is your Latte")
            print("Price is",prices["LATTE"])
        levels["water"] -= ingredients["LATTE"]["Water"]
        levels["milk"] -= ingredients["LATTE"]["Milk"]
        levels["coffee"] -= ingredients["LATTE"]["Coffee"]
        print(levels,"\n")  
    else:
        print("Not available")

