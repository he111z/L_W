# Лабораторная работа №1
Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.

Натуральные числа. Выводит на экран четные числа, содержащие нечетное количество цифр, превышающее К.

Список используемых цифр выводится отдельно прописью.

# Лабораторная работа №2
Написать программу, которая читая файл, распознает, преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Распознование делать через регулярные выражения. В вариантах, где есть параметр К, К заменяется на любое число.

Натуральные числа. Выводит на экран четные числа, содержащие нечетное количество цифр, превышающее К.

Список используемых цифр выводится отдельно прописью.

# Лабораторная работа №3
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Каждая из матриц B,C,D,E делится диагоналями на 4 области. Для тестирования использовать не случайное заполнение, а целенаправленное. Каждая из матриц B,C,D,E делится диагоналями на 4 области.

Для простоты все индексы в подматрицах относительные. Библиотечными методами пользоваться нельзя.

Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 1 больше, чем сумма чисел в нечетных строках в области 3, то поменять в Е симметрично области 1 и 3 местами, иначе В и С поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: A*F– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.

# Лабораторная работа №4
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение, а целенаправленное.

Для простоты все индексы в подматрицах относительные. 

По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.

Программа должна использовать функции библиотек numpy  и mathplotlib

Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество чисел, больших К в четных столбцах больше, чем сумма чисел в нечетных строках, то поменять местами С и Е симметрично, иначе В и С поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * FТ, иначе вычисляется выражение (AТ +G обр.-F обр.-1)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.

# Лабораторная работа №5
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить (смоделировать) границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.

F(0) = F(1) = 3; F(n) = 233-F(n-1)-(n-2) (при n >23), F(n)=(n-2) * F(n-1) (при 1<n<=23)

# Лабораторная работа №6
Вывести все четные натуральные числа до n, крайняя левая цифра которых не превышает 5.
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения. (В данной работе доп. условие такое: число не должо содержать нулей)

# Лабораторная работа №7
Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию. 
В программе должны быть реализованы минимум один класс, три атрибута, два метода.

# Лабораторная работа №8
Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона tkinter. В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.

# Лабораторная работа №11
Игра "Найди пару".
