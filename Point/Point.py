koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

import random
random.shuffle(koloda)

print("Поиграем в очко")
count = 0

while True:
    choise = input("Хотите взять карту? y/n\n")
    if choise == "y" or "н":
        current = koloda.pop()
        print("Вам попалась карта достоинством в %d очко." %current)
        count += current
        print("Ваш счет: %d очков." %count)
        if count > 21:
            print("У вас %d очков." %count)
            print("Извините, но вы проиграли :(")
            break
        if count == 21:
            print("У вас %d очков." %count)
            print("Поздравляю! Вы ВЫЙГРАЛИ")
            break
    elif choise == "n" or "т":
        print("Вы заакончили игру со счетом: %d очков" %count)
        break

print("Спасибо за игру!")