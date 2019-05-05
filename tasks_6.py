#1. Цикл с приветом 
# Как вы считаете, что делает эта программа? 
# Сперва придумайте вариант ответа, а потом запустите код и проверьте, угадали ли вы.
for x in range(0, 20):  # цикл от 0 до 19
    print('привет %s' % x) # номер переменной
    if x < 9: # если х меньше 9  
        break # остановиться

#2. Четные числа 
# Создайте цикл, который печатает четные числа до тех пор, пока не выведет ваш возраст. 
# Если ваш возраст — нечетное число, создайте цикл, который печатает нечетные числа до 
# совпадения с возрастом. 
# Программа должна выводить на экран нечто подобное: 2 4 6 8 10 12 14

x = 1
while x < 25:
    x = x + 2
    print (x)

#3. Пять любимых ингредиентов 
# Создайте список с пятью разными ингредиентами для бутерброда:

ingredients = ['bread', 'mayo', 'chren', 'chiken', 'holopenyo']

#Теперь создайте цикл, который печатает список ингредиентов с нумерацией

num = 1 #с чего начать нумерацию
for i in ingredients: #для позиций списка
    print (num, i) #вывести номер и позицию
    num = num + 1 #увеличить номер на 1
 
#4. Ваш лунный вес 
# Если бы вы сейчас были на Луне, ваш вес составил бы 16,5 процентов от земного. 
# Чтобы узнать, сколько это, умножьте свой земной вес на 0,165. 
# Если бы каждый год в течение следующих 15 лет вы прибавляли по 
# одному килограмму веса, каким бы оказался ваш лунный вес в каждый из 
# ежегодных визитов на Луну вплоть до 15-го года? Напишите программу, которая 
# с помощью цикла for печатает на экране ваш лунный вес в каждом году.

weight = 65*0.165 #определяем текущий лунный вес
year = 1 #год отсчета
while year <= 15: # до тех пор, пока год меньше или равен 15 
    print (year, weight) #печатаем год и соответствующий вес
    weight = weight + 1 #увеличиваем вес на 1
    year = year + 1 #увеличиваем год на 1