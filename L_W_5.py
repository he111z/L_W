import timeit
from datetime import timedelta
import matplotlib.pyplot as plt

print('Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить (смоделировать) границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.\n\nФункция: F(0) = F(1) = 3; F(n) = 233-F(n-1)-(n-2) (при n >23), F(n)=(n-2) * F(n-1) (при 1<n<=23)\n')
#рекурсивный подход
def f_rec(n):
    if n <= 1:
        return 3

    elif n <= 23:
        return (n - 2) * f_rec(n - 1)

    return 233 - f_rec(n - 1) - (n - 2)


#итерационный подход
def f_iter(n):
    if n <= 1:
        return 3
    prev = 3
    for i in range(2, n + 1):
        if i <= 23:
            current = (i - 2) * prev
        else:
            current = 233 - prev - (i - 2)
        prev = current
    return prev

# ф-ия приведения времени к нормальному формату
def format_duration_time(duration_time):
    #timeit.default_timer() возвращает время в формате с плавающей точкой - не очень удобно
    #воспользуемся встроенным классом таймдельта, чтоб конвертировать в милисекунды в целочисленном значении
    duration_td = timedelta(seconds=duration_time)

    #1 час = 3600 секунд
    hours = duration_td.seconds // 3600
    #поделим секуйны на 60 и возьмем остаток от деления получившегося числа на 60; получим минуты
    minutes = (duration_td.seconds // 60) % 60
    #возьмем остаток от деления на 60 - секунды
    seconds = duration_td.seconds % 60
    milliseconds = duration_td.microseconds

    # форматируем время, чтоб исключить 0 в часах, минутах и секундах, если их нет
    duration_formatted = ''
    if hours != 0:
        duration_formatted += f'{hours}:'
    if minutes != 0:
        duration_formatted += f'{minutes:02}:'
    if seconds != 0:
        duration_formatted += f'{seconds:02}:'
    duration_formatted += f'{milliseconds:003}'
    return duration_formatted

def test(vals):
    #время рекурсивного подхода
    time_list_rec = []
    #время итерационного подхода
    time_list_iter = []
    #значения рекурсивного подхода
    vals_rec = []
    #значения итерационного подхода
    vals_iter = []
    
    ns = range(1, vals+1)

    for n in ns: #замеряем время выполнения функции при разных значениях
        #рекурсия
        start_time = timeit.default_timer()
        f_val = f_rec(n)
        vals_rec.append(f_val)
        recursive_time = timeit.default_timer() - start_time
        recursive_time_formatted = format_duration_time(recursive_time)
        time_list_rec.append(recursive_time_formatted)
        #итерации
        start_time = timeit.default_timer()
        f_val = f_iter(n)
        vals_iter.append(f_val)
        iterative_time = timeit.default_timer() - start_time
        iterative_time_formatted = format_duration_time(iterative_time)
        time_list_iter.append(iterative_time_formatted)

    desc = 'n   \tВремя (рек), мс   \tВремя (итер), мс   \tЗначения (рек)   \tЗначения (итер)'
    print(desc)
    print('_'*(len(desc)+18))
    for i in range(1, len(ns)):
        print(f'{ns[i]}\t{time_list_rec[i]}\t\t\t{time_list_iter[i]}\t\t\t{vals_rec[i]}'f'\t\t\t{vals_iter[i]}')
    #рисуем рафик
    plt.plot(ns, time_list_rec, label='Рекурсивно')
    plt.plot(ns, time_list_iter, label='Итерационно')
    #метка для оси х
    plt.xlabel('n')
    #метка для оси y
    plt.ylabel('Время (мс)')
    plt.title('Сравнение рекурсивного и итерационного подхода')
    plt.legend()
    plt.show()

N=int(input('Введите n: '))
if __name__ == '__main__':
    test(N)
