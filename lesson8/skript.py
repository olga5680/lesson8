from data_create import name_data, surname_data, phone_data, address_data
import os

def get_path(mpath: str) -> os.path:
    return os.path.join(os.getcwd(), mpath)


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Попробуйте ещё раз выбрать правильную команду')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
        # print(*data_first, sep='')

    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Вы выбрали файл 1.")
        print("Какую именно запись по счету Вы хотите изменить или скопировать?")
        number_journal = int(input('Введите номер записи: '))

        print("Куда вы хотите скопировать эту запись? (1 или 2)")
        destination_file = int(input('Введите номер файла: '))

        while destination_file != 1 and destination_file != 2:
            print('Ты дурак?! Даю тебе последний шанс')
            destination_file = int(input('Введите номер файла: '))

        if destination_file == 1:
            data_first.append(data_first[number_journal-1])
            print("Запись успешно скопирована в файл 1.")
        else:
            data_second.append(data_first[number_journal-1])
            print("Запись успешно скопирована в файл 2.")
    else:
        print("Вы выбрали файл 2.")
        print("Какую именно запись по счету Вы хотите изменить или скопировать?")
        number_journal = int(input('Введите номер записи: '))

        print("Куда вы хотите скопировать эту запись? (1 или 2)")
        destination_file = int(input('Введите номер файла: '))

        while destination_file != 1 and destination_file != 2:
            print('Ты дурак?! Даю тебе последний шанс')
            destination_file = int(input('Введите номер файла: '))

        if destination_file == 1:
            data_first.append(data_second[number_journal-1])
            print("Запись успешно скопирована в файл 1.")
        else:
            data_second.append(data_second[number_journal-1])
            print("Запись успешно скопирована в файл 2.")

def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        # ТУТ НАПИСАТЬ КОД
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        # ТУТ НАПИСАТЬ КОД