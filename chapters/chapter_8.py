class Things: #создаем класс "предметы"
    pass #указываем, что мы его опишем позже
class Inanimate(Things): #создаем подкласс "неодушевленные"
    pass #указываем, что мы его опишем позже
class Animate(Things): #создаем подкласс "одушевленные"
    pass #указываем, что мы его опишем позже
class Writing_desk(Inanimate): #создаем подкласс "конторка"
    pass #указываем, что мы его опишем позже
class Animals(Animate): #создаем подкласс "животные"
    def breathe(self): #определяем функцию класса "животные" - дыхание
        print ("дышит")
    def move (self): #определяем функцию класса "животные" - движение
        print ("двигается")
    def eat_food (self): #определяем функцию класса "животные" - поедание еды
        print ("ест")
class Birds(Animals): #определяем подкласс "птицы"
    def fly (self): #определяем функцию класса "животные" - способность летать
        print ("летит")
class Ravens(Birds): #определяем подкласс "ворон"
    def keep_patience(self): #определяем функцию класса "животные" - терпение
        print ("терпит")

yakov = Ravens() #определяем переменную "Яков", привязываем ее к подклассу "ворон"
yakov.fly() #даем Якову команду лететь 
yakov.breathe() #даем Якову команду дышать

diaval = Ravens() #определяем переменную "Диаваль", привязываем ее к подклассу "ворон"
diaval.move() #даем Диавалю комаду двигаться 



import turtle

rafael = turtle.Pen() 
donatello = turtle.Pen()
michelangelo = turtle.Pen()

rafael.forward(100)
rafael.right (50)
rafael.forward (60)

donatello.left (90)
donatello.forward (100)

michelangelo.left (180)
michelangelo.forward (50)

rafael = turtle.Pen()
rafael.forward (50)



