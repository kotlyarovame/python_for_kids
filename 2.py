#месседж с переносом строки 
message = '''Что едят на полдник динозавры? \n-Тирекс-Кекс!'''
print(message)

#шаблонизация - описываю шаблон и подставляю переменную чз %
myscore = 1000
message = "Moй счет %s очков"
print (message % myscore)

joke_text = '%s: приспособление для поиска мебели в темноте' 
bodypart1 = 'Коленка' 
bodypart2 = 'Лодыжка' 
print(joke_text % bodypart1) 
print(joke_text % bodypart2) 

zero = 0
nums = 'Что сказало число %s числу %s? Славный поясок!' %(zero, 8)
print(nums)

#экранирование одинарной кавычки
single_quote_str = '"Тут что-то не так, не будь я д\'Артаньян", — подумал он"'
print (single_quote_str)

#умножение строк
print(10 * 'слякоть')
print(10 * ' ')

#список из чисел и строк вперемежку
numbers_and_strings = [7, 'раз', 'отпей', 1, 'раз', 'отъешь'] 
print(numbers_and_strings)

#список из списков
books = ['война и мир', 'преступление и наказание', 'мастер и маргарита']
hobbies = ['вязание', 'спорт', 'алкоголизм']
#объединение двух списков в один
waist_my_time = [books, hobbies]
print(waist_my_time)

#список
wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона','крыло летучей мыши', 'жир слизня', 'перхоть змеи'] 
#замена элемента списка
wizard_list [2] = 'слизь улитки'
#добавляю элементы в конец списка
wizard_list.append("медвежий коготь")
wizard_list.append ('болиголов')
wizard_list.append ('корень мандрагоры') 
wizard_list.append ("болотный газ")
#удаляю элементы 5,6,7 из списка
del wizard_list[5]
del wizard_list[6]
del wizard_list[7]
#вывод элементов списка со 2 по 5
print(wizard_list[2:5])
print(wizard_list)

#сложение списков
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
list3 = list1 + list2
print(list3)

#умножение списков
print(list1 * 5)

#кортеж
cortage = (0,1,2,3,4,5)
print (cortage[3])