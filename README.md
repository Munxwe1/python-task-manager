# python-task-manager

Консольный менеджер задач на Python. Учебный проект для лабораторной работы №3
по работе с ветками Git.

## Возможности

- добавление задачи;
- просмотр списка задач;
- отметка задачи как выполненной.

## Структура проекта

```
python-task-manager/
├── src/
│   └── main.py          # код программы
├── tests/
│   └── test_main.py     # тесты pytest
├── README.md
├── requirements.txt
└── .gitignore
```

## Ветки репозитория

- `main` — стабильная версия программы;
- `feature/*` — разработка новых функций.

## Запуск

```
python src/main.py
```

## Тесты

```
pip install -r requirements.txt
python -m pytest
```
