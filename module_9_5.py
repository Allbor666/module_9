
# Класс исключения
class StepValueError(ValueError):
    pass

# Класс итератора
class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Изначально указатель на стартовое значение

    def __iter__(self):
        self.pointer = self.start  # Сброс указателя на старт
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration  # Конец итерации

        current_value = self.pointer  # Сохраняем текущее значение для возврата
        self.pointer += self.step  # Увеличиваем указатель на шаг
        return current_value

# Пример выполнения программы
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print('Шаг указан неверно:', e)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

print()  # Печатаем новую строку для отделения выводов

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
