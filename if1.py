"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def life(age):
    if age <= 0:
        return("Ох, где только теперь нет WiFI")
    elif age <= 7:
        return("Вы отбываете срок в детском саду")
    elif age <= 17:
        return("Вы учитесь в школе")
    elif age <= 23:
        return("Вы учитесь в вузе")
    elif age == 25:
        return("Если вы до этого не ходили на собеседования то пора начинать")    
    elif age > 25 :
        return("Вы свободны до конца своих дней, можете скоротать время и пойти на курсы по Python")

def main():
    age = int(input('Введите ваш возраст: '))
    you_life = life(age)              
    print(you_life)

if __name__ == "__main__":
    main()
