## Примеры кода из книги Python Concurrency with `asyncio` 

- [Asyncio и конкурентное программирование на Python](http://library.hazadus.ru/books/47/details/)
- [Конспект в Notion](https://www.notion.so/hazadus/asyncio-f580c8ef34b34318a33de02a40461834?pvs=4)

### Глава 1. Первое знакомство с `asyncio`

- Процессы и потоки в простом Python-приложении: [ch1/listing_1_2.py](ch1/listing_1_2.py)
- Создание многопоточного Python-приложения: [ch1/listing_1_3.py](ch1/listing_1_3.py)
- Создание нескольких процессов: [ch1/listing_1_4.py](ch1/listing_1_4.py)
- Генерирование последовательности Фибоначчи и его хронометраж: [ch1/listing_1_5.py](ch1/listing_1_5.py)
- Многопоточное вычисление последовательности чисел Фибоначчи: [ch1/listing_1_6.py](ch1/listing_1_6.py)
   - Многопроцессное вычисление последовательности чисел Фибоначчи _(нет в книге)_: [ch1/listing_1_6a.py](ch1/listing_1_6a.py) 
- Синхронное чтение кода состояния: [ch1/listing_1_7.py](ch1/listing_1_7.py)
   - Многопоточное чтение кода состояния: [ch1/listing_1_7a.py](ch1/listing_1_7a.py)

### Глава 2. Основы `asyncio`

- Выполнение сопрограммы: [ch2/listing_2_3.py](ch2/listing_2_3.py)
- Использование await для ожидания результата сопрограммы: [ch2/listing_2_4.py](ch2/listing_2_4.py)
- Первое применение sleep: [ch2/listing_2_5.py](ch2/listing_2_5.py)
- Повторно используемая сопрограмма delay: [util/delay_functions.py](util/delay_functions.py)
- Создание задачи: [ch2/listing_2_8.py](ch2/listing_2_8.py)
- Конкурентное выполнение нескольких задач: [ch2/listing_2_9.py](ch2/listing_2_9.py)
- Выполнение кода, пока другие операции работают в фоне: [ch2/listing_2_10.py](ch2/listing_2_10.py)
- Снятие задачи: [ch2/listing_2_11.py](ch2/listing_2_11.py)
- Задание тайм-аута для задачи с помощью `wait_for`: [ch2/listing_2_12.py](ch2/listing_2_12.py)
- Защита задачи от снятия: [ch2/listing_2_13.py](ch2/listing_2_13.py)
- Основы будущих объектов: [ch2/listing_2_14.py](ch2/listing_2_14.py)
- Ожидание будущего объекта: [ch2/listing_2_15.py](ch2/listing_2_15.py)
- Декоратор для хронометража сопрограмм: [util/async_timer.py](util/async_timer.py)
- Хронометраж двух конкурентных задач с помощью декоратора: [ch2/listing_2_17.py](ch2/listing_2_17.py)
- Попытка конкурентного выполнения счетного кода: [ch2/listing_2_18.py](ch2/listing_2_18.py)
- Счетный код и длительная задача: [ch2/listing_2_19.py](ch2/listing_2_19.py)
- Неправильное использование блокирующего API как сопрограммы: [ch2/listing_2_20.py](ch2/listing_2_20.py)
- Создание цикла событий вручную: [ch2/listing_2_21.py](ch2/listing_2_21.py)
- Получение доступа к циклу событий: [ch2/listing_2_22.py](ch2/listing_2_22.py)
- Выполнение счетного кода в отладочном режиме: [ch2/listing_2_23.py](ch2/listing_2_23.py)

### Глава 3. Первое приложение `asyncio`

- Запуск сервера и прослушивание порта для подключения: [ch3/listing_3_1.py](ch3/listing_3_1.py)
- Чтение данных из сокета: [ch3/listing_3_2.py](ch3/listing_3_2.py)
- Подключение нескольких клиентов: [ch3/listing_3_3.py](ch3/listing_3_3.py)
- Первая попытка создать неблокирующий сервер: [ch3/listing_3_5.py](ch3/listing_3_5.py)
- Перехват и игнорирование ошибок блокирующего ввода-вывода: [ch3/listing_3_6.py](ch3/listing_3_6.py)
- Использование селектора для построения неблокирующего сервера: [ch3/listing_3_7.py](ch3/listing_3_7.py) – 
  _полнофункциональный  эхо-сервер, поддерживающий нескольких клиентов. У него нет проблем с блокированием, поскольку 
  чтение или запись производятся только тогда, когда имеются данные. Он почти не потребляет процессорного времени, 
  так как мы пользуемся эффективной системой уведомления о событиях, которая реализована внутри операционной системы._
- Построение асинхронного эхо-сервера: [ch3/listing_3_8.py](ch3/listing_3_8.py)
- Добавление обработчика сигнала, снимающего все задачи: [ch3/listing_3_9.py](ch3/listing_3_9.py)
- Корректная остановка: [ch3/listing_3_10.py](ch3/listing_3_10.py)

### Глава 3. Конкурентные веб-запросы

- Асинхронный контекстный менеджер, ожидающий подключения клиента: [ch4/listing_4_1.py](ch4/listing_4_1.py)
- Отправка веб-запроса с помощью `aiohttp`: [ch4/listing_4_2.py](ch4/listing_4_2.py)
- Задание тайм-аутов в `aiohttp`: [ch4/listing_4_3.py](ch4/listing_4_3.py)
- Неправильное использование спискового включения для создания и ожидания задач: [ch4/listing_4_4.py](ch4/listing_4_4.py)
- Использование спискового включения для конкурентного выполнения задач: [ch4/listing_4_5.py](ch4/listing_4_5.py)
- Конкурентное выполнение запросов с помощью `gather`: [ch4/listing_4_6.py](ch4/listing_4_6.py)
- Обработка исключений при использовании `gather`: [ch4/listing_4_6a.py](ch4/listing_4_6a.py)
- Использование `as_completed`: [ch4/listing_4_8.py](ch4/listing_4_8.py)
- Тайм-ауты в сочетании с `as_completed`: [ch4/listing_4_9.py](ch4/listing_4_9.py)
- Изучение поведения `wait` по умолчанию: [ch4/listing_4_10.py](ch4/listing_4_10.py)
- Обработка исключений при использовании `wait`: [ch4/listing_4_11.py](ch4/listing_4_11.py)
- Отмена работающих запросов при возникновении исключения: [ch4/listing_4_12.py](ch4/listing_4_12.py)
- Обработка запросов по мере завершения: [ch4/listing_4_13.py](ch4/listing_4_13.py)
- Обработка всех результатов по мере поступления: [ch4/listing_4_14.py](ch4/listing_4_14.py)
- Использование тайм-аутов в `wait`: [ch4/listing_4_15.py](ch4/listing_4_15.py)

### Глава 3. Неблокирующие драйверы баз данных

Запуск БД: `docker compose up -d`

В терминале контейнера, подключение к БД: `psql -U postgres -h localhost -p 5432`

- Подключение к базе данных Postgres от имени пользователя по умолчанию: [ch5/listing_5_1.py](ch5/listing_5_1.py)
