#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date

def get_contact():
    name = input("Фамилия и инициалы?  ")
    number = input("Номер телефона? ")
    birth_date = list(map(int, input("Дата рождения (в формате XX.XX.XXXX)? ").split('.')))

    if number[0] == '+':
        number = '8' + number[2:]
    return {
        'name': name,
        'number': number,
        'date': birth_date,
    }

def display_contacts(contacts):
    if contacts:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 35,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^25} | {:^20} |'.format(
                "№", "ФИО", "Номер телефона", "Дата рождения"
            )
        )
        print(line)

        for idx, contact in enumerate(contacts,1):
            date_list = contact.get('date', [0, 0, 0])
            date_str = f"{date_list[0]}.{date_list[1]}.{date_list[2]}"

            print(
                '| {:>4} | {:<30} | {:<25} | {:<20} |'.format(
                    idx,
                    contact.get('name', ''),
                    contact.get('number', ''),
                    date_str
                )
            )
            print(line)

    else:
        print("Список пуст.")

def select_contact(contacts, num):
    result = []
    for contact in contacts:
        if contact.get('number') == num:
            result.append(contact)
    return result

def main():
    contacts = []

    while True:

        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            contact = get_contact()
            contacts.append(contact)

            if len(contacts) > 1:
                contacts.sort(key=lambda item: (item.get('date', [0, 0, 0])[2],
                                                item.get('date', [0, 0, 0])[1],
                                                item.get('date', [0, 0, 0])[0]))

        elif command == "list":

            display_contacts(contacts)

        elif command.startswith("select "):

            parts = command.split(" ", maxsplit=1)
            num = parts[1]

            selected = select_contact(contacts, num)
            display_contacts(selected)

        elif command == "help":
            print("Список команд:\n")
            print("add - добавить работника")
            print("list - вывести список работников")
            print("select <стаж> - запросить работников со стажем")
            print("help - отоброзить справку")
            print("exit - завершить работу с программой")

        else:
            print(f" Неизвестная команда {command}", file=sys.stderr)
            return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
