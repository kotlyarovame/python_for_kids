# Модуль черепашки
1. **Модуль** - способ подключения полезного кода к другой программе, и в числе прочего модули обычно содержат функции, к которым можно обращаться (библиотеки).

2. **import turtle** - для использования модуля его нужно импортировать этой командой

3. **pen** - создаёт пространство для черепашки

### Консольные команды: 

```python
import turtle #импорт библиотеки

t = turtle.Pen() # вызов функции

t.forward(кол-во пикселей) или t.forward(кол-во пикселей) # двежение вперед или назад на указанное кол-вопикселей

t.left(кол-во градусов) или t.right(кол-во градусов) # поворот налево или направо на указанное кол-во градусов

t.reset() или  t.clear() # возвращает стрелку в центр, очищает пространство

t.up() # поднимает черепаху, можно перемещаться по листу, не оставляя следа

t.down() # опускает черепаху
```