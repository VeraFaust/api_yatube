# API для Yatube

## Описание:
В этом проекте реализован API для всех моделей приложения posts.  
Добавленое приложение api со всей логикой API.  
API доступно аутентифицированным пользователям.  
Аутентифицированный пользователь может изменять и удалять свой контент,  
а чужой может только читать.

## Технологии:
- Python;
- Django;
- Git;
- DRF;
- API;
- REST.

## Запуск проекта:
- Клонируйте репозиторий:
```
git clone https://github.com/VeraFaust/api_yatube.git
```

- Установите и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```

- Установите зависимости из файла requirements.txt:
```
py -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

- В папке с файлом manage.py запустите миграции:
```
py manage.py makemigrations
```
```
py manage.py migrate
```

- В папке с файлом manage.py создайте админа и запустите проект:
```
py manage.py createsuperuser
```
```
python manage.py runserver
```
Перейти по ссылке:

На сайт http://127.0.0.1:8000/  
В админ-зону http://127.0.0.1:8000/admin  
В api http://127.0.0.1:8000/api

Остановить работу:
```
Ctrl+C
```

## Примеры запросов:
- POST .../api/v1/posts/
```
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
}
```

Пример ответа:
```
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
```

- Пример POST-запроса с токеном Антона Чехова: отправляем новый комментарий к посту с id=14.  
POST .../api/v1/posts/14/comments/
```
{
    "text": "тест тест"
}
```

Пример ответа:
```
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
}
```

- Пример GET-запроса с токеном Антона Чехова: получаем информацию о группе.  
GET .../api/v1/groups/2/  
Пример ответа:
```
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
} 
```
## Автор:
Фауст Вера
