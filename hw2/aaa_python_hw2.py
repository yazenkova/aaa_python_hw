def read_file(filename: str = 'Corp_Summary.csv',
              sep: str = ';', need_stats: bool = False) -> dict:
    """
    Функция, которая читает файл о компании и собирает нужную для
    программы статистику
    :param filename: название файла, содержащего информацию о компании,
    по умолчанию задан
    :param sep: разделитель в csv файле, по умолчанию ';'
    :param need_stats: False, если нужно собрать только названия и структуру
    департаментов, True, если собираем статистику о зарплатах сотрудников
    :return: словарь с необходимой информацией для вывода в программе
    """
    info = dict()
    with open(filename, 'r') as table:
        next(table)
        for line in table:
            person = line.split(sep)
            department = person[1]
            if need_stats:
                salary = int(person[-1])
                if department in info:
                    info[department]['counter'] += 1
                    info[department]['min'] = min(salary,
                                                  info[department]['min'])
                    info[department]['max'] = max(salary,
                                                  info[department]['max'])
                    info[department]['sum'] += salary
                else:
                    info[department] = dict()
                    info[department]['counter'] = 1
                    info[department]['min'] = salary
                    info[department]['max'] = salary
                    info[department]['sum'] = salary
            else:
                team = person[2]
                if department in info:
                    info[department] |= set([team])
                else:
                    info[department] = set([team])
        return info


def print_all_departments() -> None:
    """
    Функция для вывода списка департаментов с их отделами
    :return: None
    """
    departments_structure = read_file()
    print('--Структура компании--')
    for department, teams in departments_structure.items():
        print('Департамент: ', department)
        print('Отделы: ', ', '.join(teams))
        print('***')
    end_of_work()


def print_stats() -> None:
    """
    Функция для вывода информации о зарплатах сотрудников по департаментам
    :return: None
    """
    stats = read_file(need_stats=True)
    print('Статистика о зароботной плате сотрудников '
          'с группировкой по департаментам.')
    print("{:<12}\t{:<20}\t{:<15}\t{:<15}\t{:<15}".format(
        'Отдел',
        'Количество людей',
        'Min зарплата',
        'Max зарплата',
        'Avg зарплата'))
    print('-' * 85)
    for department, department_stats in stats.items():
        print("{:<12}\t{:<20}\t{:<15}\t{:<15}\t{:<15.3f}".format(
            department,
            department_stats['counter'],
            department_stats['min'],
            department_stats['max'],
            department_stats['sum'] / department_stats['counter']))
    end_of_work()


def save_stats(filename: str = 'company_stats.csv') -> None:
    """
    Функция для сохранения статистики о зарплатах сотрудников
    по департаментам в файл csv
    :param filename: имя файла, в который сохраняется информация
    о зарплатах сотрудников по департаментам
    :return: None
    """
    stats = read_file(need_stats=True)
    prepared_lines = ["{},{},{},{},{}".format(
        dep,
        stats[dep]['counter'],
        stats[dep]['min'],
        stats[dep]['max'],
        stats[dep]['sum'] / stats[dep]['counter'])
        for dep in stats.keys()]
    columns = 'department,people_num,min_salary,max_salary,avg_salary'
    prepared_lines.insert(0, columns)
    prepared_data = "\n".join(prepared_lines)
    with open(filename, "w") as file:
        file.write(prepared_data)
    print('Статистика о зарплатах сотрудников по департаментам'
          ' сохранена в файл {}'.format(filename))
    end_of_work()


def end_of_work() -> None:
    """
    Функция для предложения выйти из программы или вернутся в меню
    с доступными опциями
    :return: None
    """
    print('Для завершения программы введите 0, '
          'для возвращения в меню с выбором опций введите 1')
    option = input()
    while option not in ['0', '1']:
        print('Неправильный ввод, допустимы только значения 0/1. '
              'Выберете опцию еще раз.')
        option = input()
    if option == '1':
        menu()


def menu() -> None:
    """
    Главное меню программы с доступными опциями
    :return: None
    """
    options = ['1', '2', '3']
    print(
        '''Доступные опции для просмотра информации о компании:
        1. Просмотр структуры компании по департаментам и отделам;
        2. Просмотр статистики о зарплатах по департаментам;
        3. Сохранение статистики о зарплатах по департаментам в файл.
        \nВведите {}/{}/{} для выбора нужной опции.'''.format(*options)
    )
    option = input()
    while option not in options:
        print('Введена некорректную опцию, допустимы только значения {}/{}/{}.'
              '\nВыберете опцию еще раз.'.format(*options))
        option = input()
    if option == '1':
        print_all_departments()
    elif option == '2':
        print_stats()
    elif option == '3':
        save_stats()
    return


if __name__ == '__main__':
    menu()
