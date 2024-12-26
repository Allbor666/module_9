from random import choice

# Задача 1: Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция для сравнения символов в строках
compare_result = list(map(lambda x, y: x == y, first, second))
print("Результат сравнения букв: ", compare_result)  # Вывод результата [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


# Задача 2: Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')
    return write_everything

# Пример использования записи в файл
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Задача 3: Класс MysticBall с методом __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Пример использования объекта MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')

# Печать значений, получаемых от вызовов объекта
print(first_ball())  # Случайный ответ: 'Да', 'Нет' или 'Наверное'
print(first_ball())  # Случайный ответ: 'Да', 'Нет' или 'Наверное'
print(first_ball())  # Случайный ответ: 'Да', 'Нет' или 'Наверное'
