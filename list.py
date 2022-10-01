#Первая задача
print("Первая задача.")

a = int(input())
b = 0

while a != 0:
    a = int(input())
    b = b + a

print(b)
print()

#Вторая задача
print("Вторая задача.")
print()

fruits = ['яблоки','апельсины','бананы']

fruits.append('виноград')
fruits.append('манго')
fruits.remove('апельсины')

print(fruits)
print()

#Третья задача
print("Третья задача.")
print()

print("Управление покупками")
print()
user_product = []
n = int(input("Введите количесвто продуктов, которое вы собираетесь внести: "))
n = n - 1
i = 0

while i <= n:
    string = "Внесите продукт №" + str(i + 1) + ": "
    user_product.append(input(string))
    i += 1

print()
print("Внесенные товары: ")
for el in user_product:
    print(el)