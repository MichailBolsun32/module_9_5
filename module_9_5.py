# Задача "Range - это просто":
# Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.
# Наследования достаточно, класс оставьте пустым при помощи оператора pass.

class StepValueError(ValueError):
    pass

# Создайте класс Iterator, который обладает следующими свойствами:
# Атрибуты объекта:
#
#     start - целое число с которого начинается итерация.
#     stop - целое число на котором заканчивается итерация.
#     step - шаг с которой совершается итерация.
#     pointer - указывает на текущее число в итерации (изначально start)
#
# Методы:
#
#     __init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага.
#     В этом методе в первую очередь проверяется step на равенство 0.
#     Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')
#     __iter__ - метод сбрасывающий значение pointer на start и возвращающий сам объект итератора.
#     __next__ - метод увеличивающий атрибут pointer на step.
#     В зависимости от знака атрибута step итерация завершиться либо когда pointer станет больше stop,
#     либо меньше stop. Учтите это при описании метода.

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        if start > stop and step > 0: # исключение на iter5 = Iterator(10, 1)
            raise StepValueError('не верно указаны параметры итерации')

        self.step = step
        self.start = start
        self.stop = stop
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        current = self.pointer
        if self.step > 0:
            if current > self.stop:
                raise StopIteration()
        else:
            if current < self.stop:
                raise StopIteration()

        self.pointer += self.step
        return current


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError:
    print('не верно указаны параметры итерации')

