# Введение в Pytest

- Создание виртуального окружения\
  **python -m venv venv**
- Активация виртуального окружения\
  **venv\Scripts\Activate.ps1**
- Обновление pip\
  pip install -u pip
- В проекте должен быть requirements.txt, в нем прописываем нужную версию pytest\
  **pytest==7.7...**
- Устанавливваем pip install -r requirements.txt\
  **Проверяем установку командой pytest**
- Добавляем в .gitignore папки venv/ и .idea/
- Форматор PyCharm\
  **ctrl + Alt + L**

#### Тесты только в папке "tests"

- Тестовый модуль всегда с префиксом "test"\
  **test_example.py**
- Код располагается в def

```python
def test_example2():
    pass 
```

- Запуск: **pytest**\
  Подробно: **pytest -v**

#### Состояния тестовой функции

- PASSED - успешно
- BROKEN - ошибка в коде
- FAILED - не успешно

### Параметризация

- test_super_module.pys

## Примеры

- assert - проверка гипотезы assert c==5 - проверь, что после сложения c=5

```python
def super_sum(a, b):
    return a + b
```