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


def main():
    print(f"Менеджер задач v{APP_VERSION}")
    add_task("Изучить git branch")
    add_task("Сделать лабораторную работу №3")
    add_task("Отправить отчёт преподавателю")
    complete_task(1)
    for task in list_tasks():
        print(format_task(task))


if __name__ == "__main__":
    main()
