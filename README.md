# Автоматизированное тестирование Wikipedia для Android

![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![Appium](https://img.shields.io/badge/Appium-✓-green.svg)
![Allure](https://img.shields.io/badge/Allure-✓-orange.svg)
![Telegram Bot](https://img.shields.io/badge/Telegram_Bot-✓-blue.svg)

Фреймворк для автоматизированного тестирования мобильного приложения Wikipedia с параллельным запуском и интеграцией с Telegram-ботом.

## Возможности

- 🚀 **Параллельный запуск** тестов на нескольких устройствах
- 🤖 **Управление через Telegram-бота**:
  - Запуск тестов по расписанию
  - Запуск тестов с определенными маркерами
  - Полный прогон всех тестов
  - Отправка Allure-отчетов
- 📊 **Детальные отчеты** в Allure
- 📝 **Логирование**:
  - Информация об устройствах
  - Ход выполнения тестов
  - Данные сессий
- ⚙️ **Автоматическое управление** сервером Appium

# Установка

## Требования

- Python 3.10 (должен быть установлен как основная версия)
- Android SDK с настроенными переменными окружения
- Java JDK
- Node.js (для Appium)
- Подключенные Android-устройства/эмуляторы

## Настройка проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/wikipedia-android-tests.git
   cd wikipedia-android-tests
   ```

2. Установите необходимые пакеты:
   ```bash
   pip install allure pytest allure-pytest
   pip install -r requirements.txt
   ```
4. Установите Appium глобально:
   ```bash
   npm install -g appium
   ```

## Использование

### Запуск из терминала

1. Запуск тестов на нескольких устройствах:
   "pytest -n [количество_устройств]"
2. Просмотр Allure-отчета:
   "allure serve allure/"

### Управление через Telegram-бота

1. Запустите сервис бота:
   "python -m bot.main"
2. Команды для бота в Telegram:
   /run_tests - Запуск тестов вручную
   /stop_tests - Прерывание выполнения тестов
   /last_report - Получение полседнего Allure-отчета
   /markers - Просмотр доступных маркеров тестов
   /schedule_tests - Запуск тестов по расписанию
   /cancel_schedule - Удаление расписания
   /simulate_push - Имитация push-события из GitHub
   /help - Справка
3. После выполнения тестов бот отправит:
   Результаты выполнения
   Ссылку на Allure-отчет

4. Просмотр Allure-отчета:
   -Скачайте архив/папку отчета, полученного от бота
   -Перейдите в терминале в папку с отчетом
   -Выполните: "allure open ."

## Структура проекта
```bash
FullProject/
├── .venv/                  # Виртуальное окружение Python
├── allure/                 # Allure отчеты и результаты тестов
├── apk/                    # APK-файлы приложений для тестирования
├── bot/                    # Исходный код Telegram бота
├── config/                 # Конфигурационные файлы проекта
├── drivers/                # Метод создания драйвера
├── logs/                   # Логи тестов и сессий
├── pages/                  # Page Object Model (POM) страницы приложения
├── reports/                # Allure отчеты для бота
├── tests/                  # Тестовые сценарии
├── utils/                  # Вспомогательные утилиты и хелперы
├── .env                    # Переменные окружения
├── pytest.ini              # Конфигурация pytest
└── README.md               # Документация проекта
```
