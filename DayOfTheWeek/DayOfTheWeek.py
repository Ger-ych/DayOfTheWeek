#! Python
# Программа для определения дня недели по году, месяцу и числу

# подключение необходимой библиотеки
import sys

# принятие данных от пользователя
year = int(input("Введите год: "))
month = int(input("Введите месяц: "))
d = int(input("Введите число: "))

try:
    # проверка корректности введённых данных
    if(d > 31 or d < 0):
        sys.exit()

    if(month > 12 or month < 0):
        sys.exit()

    if(year < 0):
        sys.exit()

    if(year%4 == 0 and month == 2 and d > 29):
        sys.exit()

    if(year%4 > 0 and month == 2 and d > 28):
        sys.exit()


    if(month > 2): 
        m = month - 2

    if(month <= 2): 
        m = month + 10
        year = year - 1

    # обработка введённых данных
    c = int(year // 100)
    y = int(year - year // 100 * 100)

    AlmostTheAnswer = int(d + ((13*m - 1) // 5 ) + y + (y // 4 + c // 4 - 2*c + 777))

    Answer = AlmostTheAnswer % 7

    # вывод ответа
    print("\n", Answer, "\n")

    if(Answer == 1):
        print("Понедельник\n")
    elif(Answer == 2):
        print("Вторник\n")
    elif(Answer == 3):
        print("Среда\n")
    elif(Answer == 4):
        print("Четверг\n")
    elif(Answer == 5):
        print("Пятница\n")
    elif(Answer == 6):
        print("Суббота\n")
    elif(Answer == 7):
        print("Воскресенье\n")

except:
    print("Ошибка!", "\n")

