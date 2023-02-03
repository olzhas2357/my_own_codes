def is_valid(n):
    if n <= 100 and n >= 1 and int(n) == n:
        return True
    else:
        return False
import random
ran_value = random.randint(0, 100)
print("Компьютер загадал число от 0 до 100 и у вас 10 попыток чтобы отгадать число."
      + "Если вы неправильно введите чисел, [ты проиграешь]")
n = int(input("Введите число: "))
for i in range(1, 11):
    if is_valid(n) == True:
        n = int(input())
        if n > ran_value:
            print("Много :)")
        elif n < ran_value:
            print("Мало :)")
        else:
            print(f"Ты угадал :) {i + 1} - ой попытка ")
        print(f"Вам осталось {10 - i - 1} попыток :-)")
    else:
        print("NO NO NO NO ERROR :(")
else:
    print(f"Вы исчерпали 10 попытокю Было загадона {ran_value} :(")