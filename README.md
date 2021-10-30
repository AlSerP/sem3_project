## Скачать проект с репозитория

Клонирование репозитория:

```bash
$ git clone https://github.com/AlSerP/draumstafir.git
```

## Работа с *git*

Создание внутренней переменной origin с ссылкой на репозиторий

```bash
$ git remote add origin https://github.com/AlSerP/draumstafir.git
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

# Запуск проета

### Venv (виртуальная среда)

Создание Venv'а с имененм new_venv (имя любое). Необходимо для локального хранения библиотек, необходимых для проекта:

```bash
$ python3 -m venv new_venv
```

Вход в *venv*:

```bash
$ "new_venv/Scripts/activate"
```

Для выхода из виртуального окружения *venv* наберите:

```bash
(new_venv) $ "new_venv/Scripts/deactivate.bat"
```

Установка необходимых библиотек из файла *requirements.txt*

```bash
(new_venv) ~$ pip install -r requirements.txt
```

Необходимо создать и применить миграции для формирования базы данных:

```bash
(new_venv) ~$ python manage.py makemigrations 
(new_venv) ~$ python manage.py migrate 
```

Теперь можно запутить проект по адресу 127.0.0.1:8000/

```bash
(new_venv) ~$ python manage.py runserver
```
