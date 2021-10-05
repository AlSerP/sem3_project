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
