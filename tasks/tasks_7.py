#1. Функция лунного веса 
# Одним из заданий к главе 6 было создание цикла for для расчета вашего веса 
# на Луне в течение 15 лет. 
# Этот цикл можно оформить в виде функции. Создайте функцию, которая принимает 
# начальный вес и величину, на которую вес увеличивается каждый год. 
# Вызывать эту новую функцию нужно будет примерно так:

def moon_weight_fn (earth_weight, plus_weight): #определяем функцию, которая принимает начальный вес и величину, на которую вес увеличивается каждый год 
    year = 1 #год отсчета
    start_weight = earth_weight
    for year in range (1, 16): #зацикливается на кол-во повторов от 1 до 15 лет
        moon_weight = start_weight * plus_weight
        print ("Год %s. Вес %s" %(year, moon_weight)) #выводит год 1 и вес 10.725
        year = year + 1 #увеличиваем год на 1
        start_weight = start_weight + 1
moon_weight_fn (65, 0.165)

#2. Функция лунного веса и количество лет 
# Измените функцию из предыдущего задания так, чтобы с ее помощью можно было рассчитывать вес для 
# разного количества лет, например 5 или 20 лет.
# Пусть эта функция принимает три аргумента: начальный вес, прибавку веса в год и количество лет:

def moon_weight_fn1 (earth_weight, plus_weight, total_year): 
    year = 1 
    start_weight = earth_weight
    for year in range (1, total_year): 
        moon_weight = start_weight * plus_weight
        print ("Год %s. Вес %s" %(year, moon_weight)) 
        year = year + 1 
        start_weight = start_weight + 1
moon_weight_fn1 (65, 0.165, 20)

#3. Программа для лунного веса 
# Вместо простой функции, принимающей значения в виде аргументов, 
# можно написать мини-программу, которая будет запрашивать эти значения с помощью sys.stdin.readline(). 
# Тогда этой функции вообще не нужны аргументы:
#moon_weight()
#Функция должна запросить начальный вес, потом прибавку веса в год и количество лет. 
# Тогда работа с программой будет происходить примерно так:
#Введите ваш нынешний земной вес 45 
#Введите ежегодный прирост вашего веса 0.4
#Введите количество лет 12 Не забудьте импортировать модуль sys, прежде чем вводить код функции:

import sys
def moon_weight_fn2 ():
    print ("Введите ваш нынешний земной вес") 
    earth_weight = int(sys.stdin.readline())
    print ("Введите ежегодный прирост вашего веса")
    plus_weight = float(sys.stdin.readline())
    print ("Введите количество лет")
    total_year = int(sys.stdin.readline())
    year = 1 
    start_weight = earth_weight
    for year in range (1, total_year): 
        moon_weight = start_weight * plus_weight
        print ("Год %s. Вес %s" %(year, moon_weight)) 
        year = year + 1 
        start_weight = start_weight + 1
moon_weight_fn2 ()
