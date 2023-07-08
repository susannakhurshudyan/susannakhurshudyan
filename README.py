#homework7
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. 
# число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько
# слов, то они разделяются дефисами. Фразы отделяются друг от 
# друга пробелами. Стихотворение  Винни-Пух вбивает в программу 
# с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом 
# все в порядке и “Пам парам”, если с ритмом все не в порядке

def number_of_vowels(word):
    count = 0
    for i in word:
        if i in "аяуюоеёэиы":
            count+=1
    return count

words = input().split(' ')
result = "Парам пам-пам"

for index, phrase in enumerate(words):
    if index == 0:
        last_number = number_of_vowels(phrase)

    current_number = number_of_vowels(phrase)
    if current_number != last_number:
        result = "Пам парам"
        print(current_number)
        break
    last_number = current_number

print(result)

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов
# таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая 
# операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows+1):
        for y in range(1, num_columns+1):
            print(operation(x, y), end=" ")
        print('\n')

print_operation_table(lambda x, y: x * y)
