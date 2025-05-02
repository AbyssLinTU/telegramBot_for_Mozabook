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