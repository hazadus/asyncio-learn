## Примеры кода из книги Python Concurrency with `asyncio` 

- [Asyncio и конкурентное программирование на Python](http://library.hazadus.ru/books/47/details/)
- [Конспект в Notion](https://www.notion.so/hazadus/asyncio-f580c8ef34b34318a33de02a40461834?pvs=4)
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [aiostream](https://aiostream.readthedocs.io/en/stable/) – Generator-based operators for asynchronous iteration.
- [What kinds of global value mutation are thread-safe?](https://docs.python.org/3/faq/library.html#id17)
- [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)
- [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)

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

### Глава 4. Конкурентные веб-запросы

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

### Глава 5. Неблокирующие драйверы баз данных

Запуск БД: `docker compose up -d`

В терминале контейнера, подключение к БД:
- `psql -U postgres -h localhost -p 5432`
- `psql -d products -U postgres -h localhost -p 5432`

- Подключение к базе данных Postgres от имени пользователя по умолчанию: [ch5/listing_5_1.py](ch5/listing_5_1.py)
- Команды создания таблиц в схеме базы данных о товарах: [ch5/listing_5_2.py](ch5/listing_5_2.py)
- Использование сопрограммы `execute` для выполнения команд `CREATE`: [ch5/listing_5_3.py](ch5/listing_5_3.py)
- Вставка и выборка марок: [ch5/listing_5_4.py](ch5/listing_5_4.py)
- Вставка случайных марок: [ch5/listing_5_5.py](ch5/listing_5_5.py)
- Вставка случайных товаров и SKU: [ch5/listing_5_6.py](ch5/listing_5_6.py)
- Создание пула подключений и конкурентное выполнение запросов: [ch5/listing_5_7.py](ch5/listing_5_7.py)
- Синхронное и конкурентное выполнение запросов: [ch5/listing_5_8.py](ch5/listing_5_8.py)
- Создание транзакции: [ch5/listing_5_9.py](ch5/listing_5_9.py)
- Обработка ошибки в транзакции: [ch5/listing_5_10.py](ch5/listing_5_10.py)
- Вложенная транзакция: [ch5/listing_5_11.py](ch5/listing_5_11.py)
- Ручное управление транзакцией: [ch5/listing_5_12.py](ch5/listing_5_12.py)
- Простой асинхронный генератор: [ch5/listing_5_14.py](ch5/listing_5_14.py)
- Потоковая обработка результатов: [ch5/listing_5_15.py](ch5/listing_5_15.py)
- Перемещение по курсору и выборка записей: [ch5/listing_5_16.py](ch5/listing_5_16.py)
- Получение заданного числа элементов с помощью асинхронного генератора: [ch5/listing_5_17.py](ch5/listing_5_17.py)

### Глава 6. Счетные задачи

- Два параллельных процесса: [ch6/listing_6_1.py](ch6/listing_6_1.py)
- Создание пула процессов: [ch6/listing_6_2.py](ch6/listing_6_2.py)
- Асинхронное получение результатов от пула процессов: [ch6/listing_6_3.py](ch6/listing_6_3.py)
- Исполнители пула процессов: [ch6/listing_6_4.py](ch6/listing_6_4.py)
- Исполнитель пула процессов в сочетании с `asyncio.gather()`: [ch6/listing_6_5.py](ch6/listing_6_5.py)
- Исполнитель пула процессов в сочетании с `asyncio.as_completed()`: [ch6/listing_6_5a.py](ch6/listing_6_5a.py)
- Однопоточная модель MapReduce: [ch6/listing_6_6.py](ch6/listing_6_6.py)
- Подсчет частот слов в Google Books Ngram: [ch6/listing_6_7.py](ch6/listing_6_7.py)
- Распараллеливание с помощью MapReduce и пула процессов: [ch6/listing_6_8.py](ch6/listing_6_8.py)
- Распараллеливание операции `reduce`: [ch6/listing_6_9.py](ch6/listing_6_9.py)
- Разделяемые значения и массивы: [ch6/listing_6_10.py](ch6/listing_6_10.py)
- Параллельное инкрементирование разделяемого счетчика: [ch6/listing_6_11.py](ch6/listing_6_11.py)
- Захват и освобождение блокировки: [ch6/listing_6_12.py](ch6/listing_6_12.py)
- Инициализация пула процессов: [ch6/listing_6_13.py](ch6/listing_6_13.py)
- Наблюдение за ходом отображения: [ch6/listing_6_14.py](ch6/listing_6_14.py)
- Цикл событий в каждом процессе: [ch6/listing_6_15.py](ch6/listing_6_15.py)

### Глава 7. Решение проблем блокирования с помощью потоков

- Многопоточный эхо-сервер: [ch7/listing_7_1.py](ch7/listing_7_1.py)
- Создание подкласса `Thread` для чистой остановки: [ch7/listing_7_2.py](ch7/listing_7_2.py)
- Базовое использование `requests`: [ch7/listing_7_3.py](ch7/listing_7_3.py)
- Выполнение запросов с помощью пула потоков: [ch7/listing_7_4.py](ch7/listing_7_4.py)
- Использование исполнителя пула потоков совместно с `asyncio`: [ch7/listing_7_5.py](ch7/listing_7_5.py)
- Использование исполнителя по умолчанию: [ch7/listing_7_6.py](ch7/listing_7_6.py)
- Использование сопрограммы `to_thread`: [ch7/listing_7_7.py](ch7/listing_7_7.py)
- Печать информации о состоянии отправки запросов: [ch7/listing_7_8.py](ch7/listing_7_8.py)
- Блокировки и рекурсия: [ch7/listing_7_9.py](ch7/listing_7_9.py)
- Класс потокобезопасного списка: [ch7/listing_7_10.py](ch7/listing_7_10.py)
- Приложение «hello world» на Tkinter: [ch7/listing_7_12.py](ch7/listing_7_12.py)
- Класс нагрузочного тестирования: [ch7/listing_7_13.py](ch7/listing_7_13.py)
- TkInter GUI: [ch7/listing_7_14.py](ch7/listing_7_14.py)
- Приложение для нагрузочного тестирования: [ch7/listing_7_15.py](ch7/listing_7_15.py)
- Хеширование паролей с помощью алгоритма `scrypt`: [ch7/listing_7_16.py](ch7/listing_7_16.py)

### Глава 8. Потоки данных (streams)

- Выполнение HTTP-запроса с помощью транспортного механизма и протокола: [ch8/listing_8_1.py](ch8/listing_8_1.py)
- Использование протокола: [ch8/listing_8_2.py](ch8/listing_8_2.py)
- Отправка HTTP-запроса с помощью потоковых писателей и читателей: [ch8/listing_8_3.py](ch8/listing_8_3.py)
- Попытка выполнения задач в фоновом режиме: [ch8/listing_8_4.py](ch8/listing_8_4.py)
- Асинхронный читатель стандартного ввода: [ch8/listing_8_5.py](ch8/listing_8_5.py)
- Использование потоковых читателей для ввода данных: [ch8/listing_8_6.py](ch8/listing_8_6.py)
- Вспомогательные функции для вывода управляющих последовательностей: [ch8/listing_8_7.py](ch8/listing_8_7.py)
- Чтение из стандартного ввода по одному символу: [ch8/listing_8_8.py](ch8/listing_8_8.py)
- Хранилище сообщений: [ch8/listing_8_9.py](ch8/listing_8_9.py)
- Приложение для асинхронной задержки: [ch8/listing_8_10.py](ch8/listing_8_10.py)
- Асинхронный командный SQL-клиент: [ch8/listing_8_11.py](ch8/listing_8_11.py)
- Создание эхо-сервера с помощью серверных объектов: [ch8/listing_8_12.py](ch8/listing_8_12.py)
