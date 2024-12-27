def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result < 2:
            print("Составное")  # Обработка случая, когда результат меньше 2
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:  # Если не было найдено делителей
                print("Простое")

        return result  # Возвращаем оригинальный результат

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)

result = sum_three(1, 1, 1)
print(result)
