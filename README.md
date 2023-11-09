## Примеры кода из книги Python Concurrency with `asyncio` 

- [Asyncio и конкурентное программирование на Python](http://library.hazadus.ru/books/47/details/)
- [Конспект в Notion](https://www.notion.so/hazadus/asyncio-f580c8ef34b34318a33de02a40461834?pvs=4)

### Глава 1. Первое знакомство с `asyncio`

- Процессы и потоки в простом Python-приложении: [listing_1_2.py](listing_1_2.py)
- Создание многопоточного Python-приложения: [listing_1_3.py](listing_1_3.py)
- Создание нескольких процессов: [listing_1_4.py](listing_1_4.py)
- Генерирование последовательности Фибоначчи и его хронометраж: [listing_1_5.py](listing_1_5.py)
- Многопоточное вычисление последовательности чисел Фибоначчи: [listing_1_6.py](listing_1_6.py)
   - Многопроцессное вычисление последовательности чисел Фибоначчи _(нет в книге)_: [listing_1_6a.py](listing_1_6a.py) 
- Синхронное чтение кода состояния: [listing_1_7.py](listing_1_7.py)
   - Многопоточное чтение кода состояния: [listing_1_7a.py](listing_1_7a.py)

### Глава 2. Основы `asyncio`

- Выполнение сопрограммы: [listing_2_3.py](listing_2_3.py)
- Использование await для ожидания результата сопрограммы: [listing_2_4.py](listing_2_4.py)
- Первое применение sleep: [listing_2_5.py](listing_2_5.py)
- Повторно используемая сопрограмма delay: [util/delay_functions.py](util/delay_functions.py)
- Создание задачи: [listing_2_8.py](listing_2_8.py)
- Конкурентное выполнение нескольких задач: [listing_2_9.py](listing_2_9.py)
- Выполнение кода, пока другие операции работают в фоне: [listing_2_10.py](listing_2_10.py)
- Снятие задачи: [listing_2_11.py](listing_2_11.py)
- Задание тайм-аута для задачи с помощью `wait_for`: [listing_2_12.py](listing_2_12.py)
- Защита задачи от снятия: [listing_2_13.py](listing_2_13.py)
- Основы будущих объектов: [listing_2_14.py](listing_2_14.py)