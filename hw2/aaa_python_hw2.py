from collections import namedtuple, defaultdict
import csv


def read_file(filename: str = 'Corp_Summary.csv',
              sep: str = ';') -> list:
    """
    Функция, которая читает файл о компании и сохраняет необходимую информацию
    о сотрудниках: департамент, отдел и зарплату
    :param filename: название файла, содержащего информацию о компании,
    по умолчанию задан
    :param sep: разделитель в csv файле, по умолчанию ';'
    :return: список, состоящий из именованных кортежей Person с атрибутами
    department, team, salary
    """
    Person = namedtuple('Person', 'department team salary')
    info = []

    with open(filename, 'r', newline='') as file:
        filereader = csv.reader(file, delimiter=sep)
        next(filereader)
        for person_info in filereader:
            person = Person(person_info[1], person_info[2],
                            int(person_info[-1]))
            info.append(person)
    return info


def print_department_structure_info(info: list) -> None:
    """
    Функция, которая по обработанной из первоначального файла информации
    собирает информацию о департаментах и их отделах и выводит ее
    :param info: список, состоящий из именованных кортежей Person с
    атрибутами department, team, salary
    :return: словарь с ключами department и значениями teams - список
    всех входящих в департамент отделов
    """
    departments = defaultdict(set)
    for person in info:
        departments[person.department].add(person.team)

    for department, teams in departments.items():
        print('Департамент: ', department)
        print('Отделы: ', ', '.join(teams))
        print('***')


def create_salary_stats_info(info: list) -> dict:
    """
    Функция, которая по обработанной из первоначального файла информации
    собирает статистику о зарплатах и возвращает ее
    :param info: список, состоящий из именованных кортежей Person
    с атрибутами department, team, salary
    :return: словарь из словарей с ключами department и значениями counter,
    min, max, sum
    """
    salary_stats = defaultdict(lambda: defaultdict(int))

    for person in info:
        salary_stats[person.department]['people_num'] += 1
        salary_stats[person.department]['min_salary'] = (
            person.salary
            if salary_stats[person.department]['min_salary'] == 0
            else min(person.salary,
                     salary_stats[person.department]['min_salary'])
            )
        salary_stats[person.department]['max_salary'] = max(
            person.salary,
            salary_stats[person.department]['max_salary']
            )
        salary_stats[person.department]['sum_salary'] += person.salary
    # добавление ключа со средним значением и удаление суммы зарплат
    for department in salary_stats:
        salary_stats[department]['avg_salary'] = (
            salary_stats[department]['sum_salary'] /
            salary_stats[department]['people_num']
            )
        salary_stats[department].pop('sum_salary')

    return salary_stats


def print_salary_stats(info: list) -> None:
    """
    Функция, которая выводит статистику о зарплате
    :param info: список, состоящий из именованных кортежей Person с атрибутами
    department, team, salary
    :return: None
    """
    salary_stats = create_salary_stats_info(info)
    fieldnames_line = (
        '{:<12}\t{:<20}\t{:<15}\t{:<15}\t{:<15}'.format('Отдел',
                                                        'Количество людей',
                                                        'Min зарплата',
                                                        'Max зарплата',
                                                        'Avg зарплата')
        )

    pattern_for_row = '{department:<12}\t{people_num:<20}\
\t{min_salary:<15}\t{max_salary:<15}\t{avg_salary:<15}'

    print('Статистика о зароботной плате сотрудников '
          'с группировкой по департаментам.', fieldnames_line,
          '-' * 85, sep='\n')

    for department, department_stats in salary_stats.items():
        print(pattern_for_row.format(
            department=department, **department_stats
            )
        )


def save_salary_stats(info: list,
                      filename: str = 'company_stats.csv') -> None:
    """
    Функция, которая сохраняет статистику о зарплате в файл filename
    :param info: список, состоящий из именованных кортежей Person
    с атрибутами department, team, salary
    :param filename: название файла для сохранения статистики по зарплатам,
    по умолчанию company_stats.csv
    :return: None
    """
    salary_stats = create_salary_stats_info(info)
    with open(filename, 'w', newline='') as file:
        fieldnames = ['department', 'people_num', 'min_salary',
                      'max_salary', 'avg_salary']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for department, salary_stats in salary_stats.items():
            row_dict = {'department': department}
            row_dict.update(salary_stats)
            writer.writerow(row_dict)
    print('Статистика о зарплатах сотрудников по департаментам'
          ' сохранена в файл {}'.format(filename))


def end_of_work() -> bool:
    """
    Функция для предложения выйти из программы или вернутся в меню
    с доступными опциями
    :return: bool - хотим выйти из программы или нет
    """
    options = {'0': True,
               '1': False
               }
    print('Для завершения программы введите {}, '
          'для возвращения в меню с выбором опций введите {}'.format(*options))
    option = input()
    while options.get(option) is None:
        print('Введена некорректная опция, выберите {}/{}'.format(
                *options
                ))
        option = input()
    return options.get(option)


def menu() -> None:
    """
    Главное меню программы с доступными опциями, в самом начале происходит
    чтение файла, файл считывается единожды.
    :return: None
    """
    info = read_file()
    options = {'1': print_department_structure_info,
               '2': print_salary_stats,
               '3': save_salary_stats}
    print(
        '''Доступные опции для просмотра информации о компании:
        1. Просмотр структуры компании по департаментам и отделам;
        2. Просмотр статистики о зарплатах по департаментам;
        3. Сохранение статистики о зарплатах по департаментам в файл.'''
    )
    program_is_closed = False
    while not program_is_closed:
        print('Введите {}/{}/{} для выбора нужной опции.'.format(*options))
        option = input()
        try:
            options.get(option)(info)
            program_is_closed = end_of_work()
        except TypeError:
            print('Введена некорректная опция, выберите {}/{}/{}'.format(
                *options
                ))

    print('Программа завершена.')


if __name__ == '__main__':
    menu()
