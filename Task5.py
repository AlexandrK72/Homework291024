"""
Задача 5. Пропавшая карточка
Для настольной игры используются карточки с номерами от 1 до N. Одна
карточка потерялась. Напишите программу, которая поможет найти потерянную
карточку, если номера оставшихся известны. Найдите её, зная номера
оставшихся карточек.
Введите число карточек — N.
Затем введите N − 1 номера оставшихся карточек. Они могут быть введены в
любом порядке
"""
N = int(input("Введите количество карточек: ")) 
sum_num = 0
sum_n = (N * (N + 1))/2
for num in range(1,N):
    number_card = int(input("Введите номер карточки: "))
    sum_num += number_card
    x = sum_n - sum_num
print('Номер потерянной карточки:', int (x))