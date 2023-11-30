# Concurrency and Multiprocessing in Python

В этом репозитории пробую примеры из книг, а также делаю наброски кода по тематике concurrency and multiprocessing 
на Python.

Материалы для дальнейшей проработки:

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [aiostream](https://aiostream.readthedocs.io/en/stable/) – Generator-based operators for asynchronous iteration.

## Наброски

Попытки эффективно решить прикладные задачи с помощью `asyncio`.

- Асинхронный парсер RSS-лент на `asyncio` и `aiohttp`: [rssreader/rssreader.py](rssreader/rssreader.py)

## Примеры кода из книги Python Concurrency with `asyncio` 

- Материалы:
  - Книга [Asyncio и конкурентное программирование на Python](http://library.hazadus.ru/books/47/details/)
  - 🔒 [Конспект в Obsidian](https://github.com/hazadus/Hazadus-Vault/blob/main/Dev/Reading/asyncio.md)
- Дополнительные ссылки из книги, и не только:
  - [What kinds of global value mutation are thread-safe?](https://docs.python.org/3/faq/library.html#id17)
  - [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)
  - [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)
  - [wrk](https://github.com/wg/wrk) tool (`brew install wrk`)
  - [PEP 333 – Python Web Server Gateway Interface v1.0](https://peps.python.org/pep-0333/)
  - [uvicorn](https://www.uvicorn.org/)
  - [Starlette](https://www.starlette.io/): lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
  - [websockets](https://pypi.org/project/websockets/): An implementation of the WebSocket Protocol (RFC 6455 & 7692).
  - Книга [Release It! Second Edition](https://pragprog.com/titles/mnee2/release-it-second-edition/): паттерн 
    "Прерыватель".
  - [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  - [uvloop](https://github.com/MagicStack/uvloop): Ultra fast asyncio event loop. 

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
- Чат-сервер: [ch8/listing_8_13.py](ch8/listing_8_13.py)
- Клиент чат-сервера: [ch8/listing_8_14.py](ch8/listing_8_14.py)

### Глава 9. Веб-приложения

- Оконечная точка для возврата текущего времени: [ch9/listing_9_1.py](ch9/listing_9_1.py)
- Подключение к базе данных о товарах: [ch9/listing_9_2.py](ch9/listing_9_2.py)
- Получение конкретного товара: [ch9/listing_9_3.py](ch9/listing_9_3.py)
- Оконечная точка для создания товара: [ch9/listing_9_4.py](ch9/listing_9_4.py)
- Приложение Flask для выборки торговых марок: [ch9/listing_9_5.py](ch9/listing_9_5.py)
- WSGI-приложение: [ch9/listing_9_6.py](ch9/listing_9_6.py)
- Простое ASGI-приложение: [ch9/listing_9_7.py](ch9/listing_9_7.py)
- Оконечная точка `/brands` в приложении Starlette: [ch9/listing_9_8.py](ch9/listing_9_8.py)
- Оконечная точка типа WebSocket в Starlette: [ch9/listing_9_9.py](ch9/listing_9_9.py)
- Использование оконечной точки типа WebSocket: [ch9/listing_9_10.html](ch9/listing_9_10.html)
- Асинхронное представление Django: [ch9/async_views/async_api/views.py](ch9/async_views/async_api/views.py)

### Глава 10. Микросервисы

- Сервис наличия на складе: [ch10/listing_10_1.py](ch10/listing_10_1.py)
- Создание и уничтожение пула подключений к базе данных: [ch10/listing_10_4.py](ch10/listing_10_4.py)
- Сервис избранного: [ch10/listing_10_5.py](ch10/listing_10_5.py)
- Сервис корзины: [ch10/listing_10_6.py](ch10/listing_10_6.py)
- Сервис товаров: [ch10/listing_10_7.py](ch10/listing_10_7.py)
- Сервис backend-for-frontend для товаров: [ch10/listing_10_8.py](ch10/listing_10_8.py)
- Сопрограмма `retry`: [ch10/listing_10_9.py](ch10/listing_10_9.py)
- Тестирование сопрограммы `retry`: [ch10/listing_10_10.py](ch10/listing_10_10.py)

### Глава 11. Синхронизация

- Попытка создать состояние гонки: [ch11/listing_11_1.py](ch11/listing_11_1.py)
- Состояние гонки в однопоточной программе: [ch11/listing_11_2.py](ch11/listing_11_2.py)
- Состояние гонки с участием словарей: [ch11/listing_11_3.py](ch11/listing_11_3.py)
- Использование блокировки asyncio: [ch11/listing_11_4.py](ch11/listing_11_4.py)
- Использование блокировок с целью избежать состояния гонки: [ch11/listing_11_5.py](ch11/listing_11_5.py)
- Использование семафоров: [ch11/listing_11_6.py](ch11/listing_11_6.py)
- Ограничение числа запросов к API с помощью семафора: [ch11/listing_11_7.py](ch11/listing_11_7.py)
- Освобождений больше, чем захватов: [ch11/listing_11_8.py](ch11/listing_11_8.py)
- Ограниченные семафоры: [ch11/listing_11_9.py](ch11/listing_11_9.py)
- Операции с событиями: [ch11/listing_11_10.py](ch11/listing_11_10.py)
- API загрузки файла на сервер: [ch11/listing_11_11.py](ch11/listing_11_11.py)
- Использование разработанного API в сервере загрузки файлов: [ch11/listing_11_12.py](ch11/listing_11_12.py)
- Исполнитель не поспевает за событиями: [ch11/listing_11_13.py](ch11/listing_11_13.py)
- Иллюстрация условий: [ch11/listing_11_14.py](ch11/listing_11_14.py)

### Глава 12. Асинхронные очереди

- Очередь в супермаркете: [ch12/listing_12_1.py](ch12/listing_12_1.py)
- Использование методов-сопрограмм очереди: [ch12/listing_12_2.py](ch12/listing_12_2.py)
- Использование очередей в веб-приложении: [ch12/listing_12_3.py](ch12/listing_12_3.py)
- Робот с очередью: [ch12/listing_12_4.py](ch12/listing_12_4.py)
- Очередь с приоритетами, содержащая кортежи: [ch12/listing_12_5.py](ch12/listing_12_5.py)
- Очередь с приоритетами, содержащая экземпляры класса данных: [ch12/listing_12_6.py](ch12/listing_12_6.py)
- LIFO-очередь: [ch12/listing_12_10.py](ch12/listing_12_10.py)

### Глава 13. Управление подпроцессами

- Выполнение простой команды в подпроцессе: [ch13/listing_13_1.py](ch13/listing_13_1.py)
- Завершение подпроцесса: [ch13/listing_13_2.py](ch13/listing_13_2.py)
- Демонстрация читателя стандартного вывода: [ch13/listing_13_3.py](ch13/listing_13_3.py)
- Порождение большого объема вывода: [ch13/listing_13_4.py](ch13/listing_13_4.py)
- Взаимоблокировка при использовании канала: [ch13/listing_13_5.py](ch13/listing_13_5.py)
- Использование `communicate`: [ch13/listing_13_6.py](ch13/listing_13_6.py)
- Конкурентное шифрование текста: [ch13/listing_13_7.py](ch13/listing_13_7.py)
- Подпроцессы и семафор: [ch13/listing_13_8.py](ch13/listing_13_8.py)
- Копирование данных, введенных пользователем: [ch13/listing_13_9.py](ch13/listing_13_9.py)
- Использование `communicate` со стандартным вводом: [ch13/listing_13_10.py](ch13/listing_13_10.py)
- Приложение `echo`: [ch13/listing_13_11.py](ch13/listing_13_11.py)
- Запуск приложения `echo` в подпроцессе: [ch13/listing_13_12.py](ch13/listing_13_12.py)
- Более сложная программа `echo`: [ch13/listing_13_13.py](ch13/listing_13_13.py)
- Разделение чтения вывода и записи ввода: [ch13/listing_13_14.py](ch13/listing_13_14.py)

### Глава 14. Продвинутое использование `asyncio`

- Класс исполнителя задач: [ch14/listing_14_1.py](ch14/listing_14_1.py)
- Сервер с контекстными переменными: [ch14/listing_14_2.py](ch14/listing_14_2.py)
- Принудительный запуск итерации цикла событий: [ch14/listing_14_3.py](ch14/listing_14_3.py)
- Использование `uvloop` в качестве цикла событий: [ch14/listing_14_4.py](ch14/listing_14_4.py)
