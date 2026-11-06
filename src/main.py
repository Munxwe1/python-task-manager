"""Консольный менеджер задач."""

APP_VERSION = "1.0"

tasks = []


def add_task(title):
    """Добавляет новую задачу и возвращает её."""
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": new_id, "title": title, "done": False}
    tasks.append(task)
    return task


def list_tasks():
    """Возвращает список всех задач."""
    return list(tasks)


def complete_task(task_id):
    """Отмечает задачу выполненной. Возвращает True, если задача найдена."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def format_task(task):
    """Возвращает строку для вывода задачи на экран."""
    mark = "x" if task["done"] else " "
    return f"[{mark}] {task['id']}. {task['title']}"


MENU = """
===== МЕНЕДЖЕР ЗАДАЧ =====
1 - Добавить задачу
2 - Показать задачи
3 - Отметить задачу выполненной
0 - Выход
"""


def show_tasks():
    """Красиво выводит список задач."""
    if not tasks:
        print("Список задач пуст.")
        return
    print("-" * 30)
    for task in list_tasks():
        print(format_task(task))
    print("-" * 30)
    done = sum(1 for t in tasks if t["done"])
    print(f"Выполнено: {done} из {len(tasks)}")


def main():
    print(f"Менеджер задач v{APP_VERSION}")
    while True:
        print(MENU)
        choice = input("Выберите пункт меню: ").strip()
        if choice == "1":
            title = input("Название задачи: ")
            task = add_task(title)
            print(f"Добавлена задача №{task['id']}")
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            task_id = int(input("Номер задачи: "))
            if complete_task(task_id):
                print("Задача отмечена выполненной.")
            else:
                print("Задача не найдена.")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестный пункт меню.")


if __name__ == "__main__":
    main()
