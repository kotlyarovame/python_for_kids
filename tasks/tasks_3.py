#1. Любимые вещи 
# Создайте список своих любимых развлечений и сохраните его в переменной games. 
# Теперь создайте список любимых лакомств, сохранив его в переменной foods. 
# Объедините два этих списка, сохранив результат в переменной favorites, 
# и напечатайте значение этой переменной. 

games = ['diablo2', 'borderlands', 'for honor' , 'mass effect']
foods = ['coffee', 'pizza', 'almond croissant', 'grechka']
favourites = [games, foods]
print (favourites)

# #2. Подсчет воинов 
# Есть 3 дома, на крыше каждого из которых прячутся по 25 ниндзя, 
# и есть 2 туннеля, в каждом из которых скрывается по 40 самураев. 
# Сколько всего воинов решили устроить заварушку? 
# (Ответ можно найти, введя в оболочке Python арифметическое выражение.)

print ((25*3) + (2*40))

#3. Приветствие 
# Создайте две переменные: пусть одна хранит ваше имя, а другая фамилию. 
# Теперь с помощью строки с метками %s напечатайте приветствие вроде такого: «Привет, Брандо Икетт!».

name = 'Denis'
surname = 'GRTV'
message = "Hello, %s %s!" 
print(message % (name, surname))