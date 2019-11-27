"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

question_dict = {
    "0": "Zero",
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",
    "Ты откуда?": "Я везде, не оборачивайся",
    "Знаешь Алису?": "Да, но мне больше синяя нравится.",
    "Ответ на главный вопрос жизни вселенной и всего": "42",
    "Где деньги?": "Спроси у Лебовски"
}


def ask_user():
    while True:
        try:
            question = input("Задай вопрос - ")
            if question in question_dict.keys():
                print(question_dict[question])
                continue
            else:
                print('Нет подходяшего вопроса, нет ответа')
                continue
        except KeyboardInterrupt:
            print()
            print('Пока!')
            break
        
if __name__ == "__main__":
    ask_user()
