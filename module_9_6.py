
def all_variants(text):
    n = len(text)  # Длина строки
    # Внешний цикл отвечает за начальную позицию
    for start in range(n):
        # Внутренний цикл отвечает за конечную позицию
        for end in range(start + 1, n + 1):
            yield text[start:end]  # Возвращаем подпоследовательность от start до end

# Пример вызова функции и итерации по генератору
a = all_variants("abc")
for i in a:
    print(i)
