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
    def find_food (self): #функция, вызывающая другие функции
        self.move() #вызываем функцию "move" через аргумент self (12 строка)
        print ("I find some food!")
        self.eat_food() #вызываем функцию "eat_food" через аргумент self (14 строка)
    def dance_a_jig (self):
        self.move()
        self.move()
        self.move()
        self.move()


class Ravens(Birds): #определяем подкласс "ворон"
    #def keep_patience (self): #определяем функцию класса "животные" - терпение
    #    print ("терпит")
    def __init__ (self, feathers): #функция инициализации, принимающая 2 аргумента
        self.raven_feathers = feathers #присваиваем значение аргумента feathers свойству объекта raven_feathers 

#yakov = Ravens() #определяем переменную "Яков", привязываем ее к подклассу "ворон"
#yakov.fly() #даем Якову команду лететь 
#yakov.breathe() #даем Якову команду дышать

#diaval = Ravens() #определяем переменную "Диаваль", привязываем ее к подклассу "ворон"
#diaval.move() #даем Диавалю комаду двигаться 

#yakov.find_food()
#diaval.dance_a_jig()

ozwald = Ravens(100)
print (ozwald.raven_feathers)
gertruda = Ravens(150)
print (gertruda.raven_feathers)




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



