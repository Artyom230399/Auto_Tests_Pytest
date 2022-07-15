def rating_generator(a):
    if a == 0:
        result = "На экзамен не явился"
        print(result)
    elif 0 < a < 40:
        result = "Не сдал"
        print(result)
    elif 40 <= a < 60:
        result = 'Оценка - 3'
        print(result)
    elif 60 <= a < 80:
        result = "Оценка - 4"
        print(result)
    elif 80 <= a <= 100:
        result = "Оценка - 5"
        print(result)
    elif a < 0 or a > 100:
        result = "Невалидное значение"
        print(result)
