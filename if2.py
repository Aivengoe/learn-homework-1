"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def  string_comparison(first_string, second_string):
    if (type(first_string) is not str) or (type(second_string) is not str):
        return(0)
    elif first_string == second_string:
        return(1)
    elif (first_string != second_string) and (len(first_string) > len(second_string)):
        return(2)
    elif (first_string != second_string) and (second_string == "learn"):
        return(3)


def main():
    print(string_comparison(1, 2))
    print(string_comparison(1, "learn"))
    print(string_comparison("Monty Python", "Monty Python"))
    print(string_comparison("Monty Python3", "Monty Python"))
    print(string_comparison("Monty", "learn"))

    
if __name__ == "__main__":
    main()
