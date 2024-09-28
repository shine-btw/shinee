import random
from nt import remove

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить предмет
        5. Удалить ученика
        6. Удалить оценку
        7. Вывод информации по всем оценкам для определенного ученика 
        8. Вывод среднего балла по каждому предмету по определенному ученику
        9. Редактирование ученика
        10.Редактирование предмета
        11.Редакторивание оценки
        12. Добавление нового ученика в класс
        13. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()


    elif command == 4:

        print('4. Удалить предмет ')
        name = input("Введите название предмета которого нужно удалить: ")
        if name in classes:
            del students_marks[student][name]
            print("Предмет удален" )
            print(f'Список предметов {students_marks[student].keys()}')
        else:
            print('Предмета нет в списке')

    elif command == 5 :
        print('5. Удалить ученика ')
        name = input("Введите имя ученика которого нужно удалить: ")
        if name in students:
            students.remove(name)
            print("Ученик удален")
            print(f'Список учеников {students}')
        else:
            print("Ученика нет в списке")

    elif command == 6:
        print('6. Удалить оценку: ')
        name = input("Введите имя ученика у которого нужно удалить: ")
        class_ = input("Введите предмет по которому нужно удалить оценку у ученика: ")
        print(f'''{name}
            Оценки по: {class_} {students_marks[student][class_]}''')
        mark = int(input("Введите оценку которую нужно удалить: "))
        if name in students_marks.keys() and class_ in students_marks[student].keys():
            if mark in students_marks[student][class_]:
             students_marks[student][class_].remove(mark)
             print("Оценка удалена")
             print(f'''{name}
            {students_marks[student]}''')
            else:
                     print("Оценки в списке нет")



    elif command == 7:
        print("7. Вывод информации по всем оценкам для определенного ученика  ")
        name = input("Введите имя ученика: ")
        if name in students:
         print(f'''{name}
          Все оценки: {students_marks[student]}''')
        else:
            print("Ученика не существует")

    elif command == 8:
        print("8. Вывод среднего балла по каждому предмету по определенному ученику")
        student = input("Введите имя ученика: ")
        for class_ in classes:
            if student in students_marks.keys():
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'Средний балл ученика {student} '
                  f'по предмету "{class_}" - {marks_sum // marks_count}')
            else:
                print("Некорректно введены данные")


    elif command == 9:
        print("9. Редактирование ученика:")
        student = input("Введите имя ученика: ")
        newStudent = input("Введите новое имя ученика: ")
        if student in students_marks.keys():
            students_marks[newStudent] = students_marks[student]
            del students_marks[student]


            print(f'Имя {student} изменен на {newStudent}')
            print(f'''{newStudent}
                        {students_marks[newStudent]}''')
        else:
            print("Неправильное имя ученика")

    elif command == 10:
        print("10.Редактирование предмета ")
        class_ = input("Введите предмет для редактирования: ")
        classNew = input("Введите новое имя для предмета: ")
        if class_ in students_marks[student]:
            students_marks[student][classNew] = students_marks[student][class_]
            del students_marks[student][class_]
            print(f"Навзание предмета {class_} изменен на {classNew}")
        else:
            print("Название предмета введена не правильно")

    elif command == 11:
        print("11. Редакторивание оценки: ")
        student = input("Введите имя ученика у которого нужно изменить оценку: ")
        class_ = input("Введите название предмета: ")
        print(f'''{student}
             Оценки по: {class_} {students_marks[student][class_]}''')
        mark = int(input("Введите оценку которую нужно изменить: "))
        newMark = int(input("Введите новую оценку: "))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                students_marks[student][class_].append(newMark)


                print(f"Оценка {student} по предмету {class_} изменена с {mark} на {newMark}")
                print(f'''{student}
                     Оценки по: {class_} {students_marks[student][class_]}''')
            else:
                print("Такой оценки нет")

    elif command == 12:
        print("12. Добавление нового ученика в класс")
        newStudent = input("Введите имя нового ученика: ")
        if newStudent not in students_marks:
            students.append(newStudent)
            print(f"В класс добавлен новый ученик {newStudent}")

        else:
            print("Такой ученик уже есть в списке")



    elif command == 13:
        print('12. Выход из программы')
        break