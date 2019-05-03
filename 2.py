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

#экранирование одинарной кавычки
single_quote_str = '"Тут что-то не так, не будь я д\'Артаньян", — подумал он"'
print (single_quote_str)