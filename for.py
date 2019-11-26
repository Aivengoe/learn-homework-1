"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school = [
    {'school_class': '4a', 'scores': [5,4,2,5,2]},
    {'school_class': '4b', 'scores': [3,2,4,5,2]},
    {'school_class': '4v', 'scores': [4,3,3,5,2]},
    {'school_class': '5a', 'scores': [3,4,4,5,2]},
    {'school_class': '5b', 'scores': [3,5,5,5,2]},
    {'school_class': '6a', 'scores': [2,2,5,5,2]},
    {'school_class': '7a', 'scores': [3,4,2,5,2]}
]

def mean_scores_school(school, request_scores):
    mean_scores = 0
    class_mean_scores = []
    for scholl_class in school:
        mean_scores_class = round(sum(scholl_class['scores']) / len(scholl_class['scores']), 0)
        class_mean_scores.append({'class': scholl_class['school_class'], 'mean scores': mean_scores_class})
        mean_scores += mean_scores_class
    
    mean_scores = round(mean_scores / len(school), 0)
    
    if request_scores == 'Школа':
        print(f'Средняя оценка в школе: {mean_scores}')
    elif request_scores == 'Классы':
        for class_scores in class_mean_scores:
            print(f'Класс: {class_scores["class"]}, Средняя оценка: {class_scores["mean scores"]}')
    else:
        print('Неверный запрос. Введите "Школа" или "Классы"')

def main():

    mean_scores_school(school, 'Школа')

    mean_scores_school(school, 'Классы')
    
if __name__ == "__main__":
    main()
