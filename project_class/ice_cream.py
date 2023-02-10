import random
k = [{"type": "шоколадное", "cost":"500"},
     {"type": "Ягодное" ,"cost": "400"},
     {"type": "Ванильное", "cost": "450"},
     {"type": "Со вкусом кофе", "cost": "420"},
     {"type": "Крем-брюле", "cost": "480"},
     {"type": "Oреховое", "cost": "510"}]
print("Hello! MCflurry")
name = input("what's your name?")
for i in range(len(k)):
    print(k[i]["type"])
print("Choose one of these ice creams :)")
m = input()
n = int(input())
l = []
for i in range(len(k)):
    if m == k[i]["type"]:
        ind = i
        if n >= int(k[ind]["cost"]):
            print("Bon appetit")
            break
        elif n < 400:
            print("I don`t have enough money")
        else:
            print(f"Сhoose another ice cream {name}")
            for j in range(len(k)):
                if n >= int(k[j]["cost"]):
                    l.append(k[j]["type"])
            print(l)
            p = input()
            for type in l:
                if p == type:
                    print("Bon appetit")
