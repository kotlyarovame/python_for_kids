#цикл for
#зацикиваю написание example 5 раз
for x in range (0, 5):
    print("example")

# будет считать количество example
for x in range(0, 3): 
    print('example %s' % x) 

# как бы работал этот код без функции for:
x = 0
print ("example %s" % x)
x = 1 
print ("example %s" % x)
x = 2
print ("example %s" % x)

# можно использовать ранее созданный список
languages = ["java script", "python", "php", "ruby"]
for z in languages:
    print(z)

#Для каждого значения из списка languages: 
#сохраняется значение в переменной z и выводится значение этой переменной на экран.
#Без цикла for нам бы пришлось написать что-то вроде такого:

languages = ["java script", "python", "php", "ruby"]
print (languages[0])
print (languages[1])
print (languages[2])
print (languages[3])

pinkyfluffysmthng = ["pinky", "fluffy", "something"]
for x in pinkyfluffysmthng:
    print (x)
    print (x)

pinkyfluffysmthng = ["1", "2", "3"]
for x in pinkyfluffysmthng:
    print (x)
    for y in pinkyfluffysmthng:
        print (y)

#грейды начислений считаются так:
found_coins = 20
magic_coins = 70 
stolen_coins = 3
coins = found_coins #приравниваем found_coins переменной coins (обуславливаем этой переменной, сколько у нас монет всего, чтобы не запутататься)
for week in range (1, 53): #цикл для недель от 1 до 52 
    coins = coins + magic_coins - stolen_coins
    print ("Неделя %s = %s" % (week, coins))

# цикл while
#step = 0
#while step < 10000: #для ступенек меньше кол-ва 10000
#    print (step)
#    if tired == True: #значение tired - неизвестно 
#        break #остановка кода
#    elif badweather == True: #значение badweather - неизвестно 
#        break #остановка кода
#    else: #если tired или badweather = False, то выполняется условие:
#        step = step + 1 

# цикл while выполняет следующие действия: 
# 1. Проверяет условие.
# 2. Выполняет код в блоке.
# 3. Повторяет все сначала.

#цикл с двумя условиями
x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print (x,y)




