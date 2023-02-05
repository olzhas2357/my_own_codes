import random
random_value = random.randint(0, 100)
attempt = 0
print("Компьютер загадал число от 0 до 100 и у вас 10 попыток чтобы отгадать число")

for i in range(10):
    choice = int(input("Введите число: "))
    if choice > random_value:
        print("много :)")
    elif choice < random_value:
        print("мало :) ")
    else:
        print(f"Ты угадал :) {i+1} - ой попытка ")
    print(f"Вам осталось {10 - i - 1} попыток :-)")
else:
    print(f"Вы исчерпали 10 попытокю Было загадона {random_value} :(")