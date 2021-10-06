## Скачать проект с репозитория

Клонирование репозитория:

```bash
$ git clone https://github.com/AlSerP/sem3_project.git
```

## Работа с *git*

Создание внутренней переменной origin с ссылкой на репозиторий

```bash
$ git remote add origin https://github.com/AlSerP/sem3_project.git
```

Загрузить изменения с репозитория с текущей ветки:

```bash
$ git pull
```

Создать новую ветку new_branch и переключиться на нее:

```bash
$ git checkout -b new_branch
```

Переключиться на существующую ветку old_branch:

```bash
$ git checkout old_branch
```

Добавить файлы с изменениями:

```bash
$ git add file1 file2 folder/
```

Сделать коммит (сохранение) с его "Кратким описанием":

```bash
$ git commit -m "Test commit"
```

Проверить состояние файлов (какие измененные файлы не сохранены):

```bash
$ git pull
```

Отправить изменения на репозиторий origin на ветку branch:

```bash
$ git push origin branch
```

## Venv (виртуальная среда)

Создание Venv'а необходимо для локального хранения библиотек, необходимых для проекта:

```bash
$ python3 -m venv new_venv
```

Если получаем ошибку:
*"The virtual environment was not created successfully because ensurepip is not available... "*

Нужно дополнительно установить:

```bash
sudo apt-get install python3-venv
```

Вход в *venv*:

```bash
new_venv/Scripts> activate
```

Для выхода из виртуального окружения *venv* наберите:

```bash
new_venv/Scripts> deactivate.bat
```


## Запуск проекта

Установка библиотек

```bash
(new_venv) ~$ pip install -r requirements.txt
```

Запуск проета

```bash
(new_venv) ~$ python manage.py runserver
```
