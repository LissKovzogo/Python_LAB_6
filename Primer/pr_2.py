#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date

def get_worker():
    name = input("Фамилия и инициалы: ")
    post = input("Должность: ")
    year = int(input("Год поступления: "))
    return {
        "name": name,
        "post": post,
        "year": year,
    }

def display_workers(staff):
    if staff:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} |'.format(
                "№",
                "ФИО",
                "Должность",
                "Год"
            )
        )
        print(line)

        for idx, worker in enumerate(staff,1):
            print(
                '| {:^4} | {:^30} | {:^20} |'.format(
                    idx,
                    worker.get("name",''),
                    worker.get("post",''),
                    worker.get("year",0)
                )
            )
        print(line)

    else:
        print("Список работников пуст.")

def select_worker(staff, period):
    today = date.today()

    result = []
    for employee in staff:
        if today.year - employee.get("year", today.year) >=period:
                result.append(employee)
    return result

def main():
    workers = []

    while True:

        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            worker = get_worker()
            workers.append(worker)

            if len(workers) > 1:
                workers.sort(key=lambda item: item.get("name",''))

        elif command == "list":

            display_workers(workers)

        elif command.startswith("select "):

            parts = command.split(" ", maxsplit=1)
            period = int(parts[1])

            selected = select_worker(workers, period)
            display_workers(selected)

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
