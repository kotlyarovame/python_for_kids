def action (hand) : #определяем функцию action (действие) - создаем "черный ящик" функции
    print("%s your right hand" %hand) #вывести надпись подстановкой аргумента функции, с помощью шаблонизатора - наполняем черный ящик функции
action ("Wave") #вызвать действие со значением аргумента wave (махать) - активируем функцию и содержимое "черного ящика"

def testfunc (dessert, coffee): #определяем функцию с двумя аргументами
    print("I like %s with %s" % (dessert, coffee)) #вывести надпись с подстановкой аргументов функции, с помощью шаблонизатора
testfunc ("waffles", "latte") #вызваем функцию со значениями аргументов waffle и coffee

beer1 = "red ale" #задаем переменную
beer2 = "oatmeal stout" #задаем переменную
def offer (sort1, sort2): #определяем функцию с двумя аргументами
    print ("May I have one %s and one %s" % (sort1, sort2)) #вывести надпись с подстановкой аргументов функции, с помощью шаблонизатора
offer (beer1, beer2) #вызываем функцию с использованием переменных beer1 и beer2 в аргументах sort1 и sort2

def money (official, non_official, spending): #определяем функцию с тремя аргументами
    return official + non_official - spending #возвращаем результат вычислений между аргументами функции
free_money = money (21000, 7100, 7500) #записываем в переменную вызов функции со значениями аргументов функции
print (free_money) #выводим переменную
#или
print (money (21000, 7100, 7500)) #вместо строчек 17 и 18 - можно вызвать функцию так

def example_1 (): #определяем функцию без аргументов
    digit1 = 1 #определяем переменные в области видимости этой функции
    digit2 = 2
    digit3 = 3
    return digit1 + digit2 + digit3 #возвращаем результат вычислений между переменными в области видимости этой функции
print (example_1 ()) #вызываем функцию и записываем результат вычислений

#ВНЕЗАПНО:
print (example_1) #выводит номер ячейки памяти, в которую записана функция

anthr_digit = 4 #определяем переменную в области видимости этой функции
def example_2 (): #определяем функцию без аргументов
    digit1 = 1 #определяем переменные в области видимости этой функции
    digit2 = 2 
    digit3 = 3
    return digit1 + digit2 + digit3 + anthr_digit
print (example_2 ())

def spaceship_building (cans):  #определяем функцию
    total_cans = 0 #определяем переменную для изначального количества банок
    for week in range (1, 51): #задаём цикл на 52 недели
        total_cans = total_cans + cans #переопределяем переменную как перемнная + аргумент
        print ("Неделя %s. Банок %s" % (week, total_cans)) #выводим номер недели и количество накопленных банок 
spaceship_building (10) #вызываем функцию с количеством банок 10 в неделю

import time
print (time.asctime())

import sys
#print (sys.stdin.readline())

def silly_age_joke(): #определяем функцию
    print ("Сколько вам лет?") #вывести строку
    age = int(sys.stdin.readline()) #запросить возраст у пользователя
    if age >= 10 and age <=13: #если возраст больше или равен 10, или, меньше или равен 13
        print ('13 + 49 + 84 + 155 + 97: что получится? Головная боль!') #вывести шутку
    else: #доп.условие
        print('Что-что?') #вывести эту строку
silly_age_joke () #вызов функции без аргумента