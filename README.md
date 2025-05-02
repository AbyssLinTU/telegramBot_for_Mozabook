# Mozabook Teacher Assistant Bot

Telegram бот для обучения учителей работе с Mozabook.

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` и добавьте:
```
BOT_TOKEN=your_bot_token_here
ADMIN_IDS=123456789,987654321
```

4. Запустите бота:
```bash
python main.py
```

## Команды

- `/start` - Начать работу с ботом
- `/help` - Показать справку
- `/mozabook` - Основы работы с Mozabook

## Работа с Git

### Начальная настройка
```bash
# Установка Git (если еще не установлен)
# Скачайте с https://git-scm.com/downloads

# Настройка имени и email
git config --global user.name "Ваше Имя"
git config --global user.email "ваш.email@example.com"
```

### Основные команды
```bash
# Инициализация репозитория
git init

# Проверка статуса
git status

# Добавление файлов в индекс
git add .  # все файлы
git add file.py  # конкретный файл

# Создание коммита
git commit -m "Описание изменений"

# Просмотр истории коммитов
git log

# Создание новой ветки
git branch feature-name
git checkout feature-name
# или одной командой
git checkout -b feature-name

# Переключение между ветками
git checkout main
git checkout feature-name

# Слияние веток
git checkout main
git merge feature-name

# Удаление ветки
git branch -d feature-name
```

### Работа с удаленным репозиторием
```bash
# Добавление удаленного репозитория
git remote add origin https://github.com/AbyssLinTU/telegramBot_for_Mozabook.git

# Отправка изменений
git push origin main
git push origin feature-name

# Получение изменений
git pull origin main

# Клонирование репозитория
git clone https://github.com/AbyssLinTU/telegramBot_for_Mozabook.git
```

### Полезные команды
```bash
# Отмена изменений в файле
git checkout -- file.py

# Отмена индексации файла
git reset file.py

# Отмена последнего коммита
git reset --soft HEAD~1

# Создание тега
git tag v1.0.0
git push origin v1.0.0

# Просмотр изменений
git diff
git diff --staged
```

### .gitignore
Создайте файл `.gitignore` в корне проекта:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Environment variables
.env

# Logs
*.log
``` 