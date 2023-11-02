# Pets API
API проекта для ведения учёта питомцев(собак и кошек).

## Содержание
- [Описание](#описание)
- [Стек технологий](#стек-технологий)
- [Запуск проекта](#запуск-проекта)
- [Примеры запросов и ответов API](#примеры-запросов-и-ответов-api)
- [Автор проекта](#автор-проекта)

## Описание
Данное API позволяет добавлять питомцев в базу данных, а также получать информацию о них или, при необходимости, удалять из базы данных.

## Стек технологий
Python 3.11.5  
FastAPI 0.104.1  
SQLite 3.44.0  

## Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:OlejkaS/pets_api.git
```

```
cd pets_api/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейти в папку pets_app с файлом main.py:

```
cd pets_app/
```

Запустить проект:

```
uvicorn main:app
```

Перейти по адресу http://127.0.0.1:8000/docs для чтения документации и тестирования запросов.


## Примеры запросов и ответов API

### GET-запрос на получение информации о питомцах:
```
pets/
```
### Ответ от API:
```
{
  "count": 4,
  "items": [
    {
      "name": "Марс",
      "age": 1,
      "type": "dog",
      "id": 7,
      "created_at": "2023-11-02T00:34:24.680341"
    },
    {
      "name": "Барсик",
      "age": 12,
      "type": "dog",
      "id": 8,
      "created_at": "2023-11-02T00:38:38.939414"
    },
    {
      "name": "Пушок",
      "age": 13,
      "type": "cat",
      "id": 10,
      "created_at": "2023-11-02T01:13:11.787313"
    },
    {
      "name": "Фред",
      "age": 11,
      "type": "dog",
      "id": 11,
      "created_at": "2023-11-02T01:31:50.175700"
    }
  ]
}
```

### POST-запрос на добавление питомца:
```
pets/
```
```
{
  "name": "Шарик",
  "age": 11,
  "type": "dog"
}
```
### Ответ от API:
```
{
  "name": "Шарик",
  "age": 11,
  "type": "dog",
  "id": 12,
  "created_at": "2023-11-02T18:23:23.157184"
}
```

### DELETE-запрос на удаление питомцев:
```
pets/
```
```
{
  "ids": [
    1,
    3,
    11
  ]
}
```
### Ответ от API:
```
{
  "deleted": 1,
  "errors": [
    {
      "id": 1,
      "error": "Pet with the matching ID was not found."
    },
    {
      "id": 3,
      "error": "Pet with the matching ID was not found."
    }
  ]
}
```

## Автор проекта

- [Олег Силецкий](https://github.com/OlejkaS)
