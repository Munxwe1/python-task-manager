import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest  # noqa: E402

import main  # noqa: E402


def setup_function():
    main.tasks.clear()


def test_add_task():
    task = main.add_task("Купить хлеб")
    assert task["id"] == 1
    assert task["title"] == "Купить хлеб"
    assert task["done"] is False


def test_list_tasks():
    main.add_task("Первая")
    main.add_task("Вторая")
    assert len(main.list_tasks()) == 2


def test_complete_task():
    main.add_task("Задача")
    assert main.complete_task(1) is True
    assert main.list_tasks()[0]["done"] is True
    assert main.complete_task(99) is False


def test_delete_task():
    main.add_task("Удалить меня")
    assert main.delete_task(1) is True
    assert main.list_tasks() == []


def test_empty_title_is_rejected():
    with pytest.raises(ValueError):
        main.add_task("   ")


def test_search_tasks():
    main.add_task("Изучить git merge")
    main.add_task("Купить молоко")
    found = main.search_tasks("GIT")
    assert len(found) == 1
    assert found[0]["title"] == "Изучить git merge"


def test_filter_tasks():
    main.add_task("Первая")
    main.add_task("Вторая")
    main.complete_task(1)
    assert len(main.filter_tasks(True)) == 1
    assert len(main.filter_tasks(False)) == 1
