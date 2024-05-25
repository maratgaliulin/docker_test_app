import time

counter = 0  # счетчик повторений

with open('output.log', 'a') as f:  # открываем файл для добавления текста
    while True:
        counter += 1
        log_message = f"Приложение работает супер!!!!! Повторение №{counter}\n"
        print(log_message)  # вывод в стандартный вывод (stdout)
        f.write(log_message)  # запись в файл
        time.sleep(1)  # ожидание 1 секундысд
