#day 15
#build a coffe machine

#3 hot drinks
from operator import index, indexOf


drinks = ['Turkish','Espresso','Latte']

levels = {"water":300,"milk":200,"coffee":120}
ingredients = {"Turkish":{"Water":50,"Milk":20,"Coffee":10}}
prices = {"Turkish":57,"Espresso":76,"Latte":55}

ordered_drink = input("What would you like to ask? ")
if(drinks[indexOf(ordered_drink,drinks)] == "Turkish"):
    print("Turkish")
    if(levels["water"] < ingredients["Turkish"]["Water"]):
        print("Not enough water")
    elif(levels["milk"] < ingredients["Turkish"]["Milk"]):
        print("Not enough milk")
    elif(levels["coffee"] < ingredients["Turkish"]["Coffee"]):
        print("Not enough coffee")
    else:
        print("Here is your Turkish")
        levels["water"] -= ingredients["Turkish"]["Water"]
        levels["milk"] -= ingredients["Turkish"]["Milk"]
        levels["coffee"] -= ingredients["Turkish"]["Coffee"]
        print(levels)
#if(drinks[ordered_drink] is )

print(ingredients["Turkish"]["Water"])
