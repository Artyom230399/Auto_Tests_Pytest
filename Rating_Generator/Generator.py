def rating_generator(a):
    if a == 0:
        result = "На экзамен не явился"
    elif 0 < a < 40:
        result = "Не сдал"
    elif 40 <= a < 60:
        result = 'Оценка - 3'
    elif 60 <= a < 80:
        result = "Оценка - 4"
    elif 80 <= a <= 100:
        result = "Оценка - 5"
    elif a < 0 or a > 100:
        result = "Невалидное значение"
    return result
