"""Консольный менеджер задач."""

APP_VERSION = "1.1"

tasks = []


def validate_title(title):
    """Проверяет название задачи и возвращает его без лишних пробелов."""
    if not isinstance(title, str):
        raise ValueError("Название задачи должно быть строкой")
    title = title.strip()
    if not title:
        raise ValueError("Название задачи не может быть пустым")
    if len(title) > 100:
        raise ValueError("Название задачи длиннее 100 символов")
    return title


def add_task(title):
    """Добавляет новую задачу и возвращает её."""
    title = validate_title(title)
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


def delete_task(task_id):
    """Удаляет задачу по номеру. Возвращает True, если задача была удалена."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False


def search_tasks(text):
    """Ищет задачи, в названии которых есть указанный текст."""
    text = text.lower()
    return [t for t in tasks if text in t["title"].lower()]


def filter_tasks(done):
    """Возвращает выполненные (done=True) или невыполненные задачи."""
    return [t for t in tasks if t["done"] == done]


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
    delete_task(3)
    try:
        add_task("   ")
    except ValueError as error:
        print(f"Ошибка: {error}")
    for task in list_tasks():
        print(format_task(task))
    print("Поиск по слову 'git':")
    for task in search_tasks("git"):
        print(format_task(task))
    print("Невыполненные задачи:")
    for task in filter_tasks(False):
        print(format_task(task))


if __name__ == "__main__":
    main()
