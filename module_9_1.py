def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для хранения результатов

    # Перебираем все функции
    for func in functions:
        # Применяем функцию к списку и записываем результат в словарь
        results[func.__name__] = func(int_list)

    return results  # Возвращаем словарь результатов


# Пример работы функции
print(apply_all_func([6, 20, 15, 9], max, min))  # {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
# {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
