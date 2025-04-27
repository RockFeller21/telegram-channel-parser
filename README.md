Telegram Channel parser.

A script for automatically copying messages from one or several Telegram channels to other channels, with options for text filtering and extracting specific message fragments.

Скрипт для автоматического копирования сообщений из одного или нескольких Telegram-каналов в другие каналы с возможностью фильтрации по тексту и выделения определённых фрагментов сообщений.

_---------------------------------------------------_
🇬🇧 - English

Features:
- Supports multiple source and target channels.
- Filters messages by required text.
- Copies only a specific message fragment by prefix.
- Simple configuration via YAML and text files.
- Logs all actions to the console.

Installation:
- Clone the repository or download the code archive.
- Install dependencies:
```
pip install -r req.txt
```
- Get your api_id and api_hash at my.telegram.org.
- Configure the files: 
    config.yaml — main settings
    source_channels.txt — list of source channels (one per line, ID or username)
    send_channels.txt — list of target channels (one per line, ID or username)

Run:
```
python main.py
```

How does it work? 
The script monitors new messages in the specified source channels.
If filtering is enabled (require_text: true), only messages containing the required text will be processed.
If fragment copying is enabled (copy_fragment: true), only the fragment starting with the specified prefix will be sent.
All actions are logged to the console.

_---------------------------------------------------_
🇷🇺 - Русский

Возможности:
- Поддержка нескольких исходных и целевых каналов.
- Фильтрация сообщений по обязательному тексту.
- Копирование только определённого фрагмента сообщения по префиксу.
- Простая настройка через конфиг и текстовые файлы.
- Логирование событий через print.

Установка:
- Склонируйте репозиторий или скачайте архив с кодом.
- Установите зависимости:
```
pip install -r req.txt
```
- Получите api_id и api_hash на my.telegram.org.
- Настройте файлы:
    config.yaml — основные настройки
    source_channels.txt — список исходных каналов (по одному в строке, ID или username)
    send_channels.txt — список целевых каналов (по одному в строке, ID или username)

Запуск:
```
python main.py
```

Как это работает?
Скрипт отслеживает новые сообщения в указанных исходных каналах.
Если включена фильтрация (require_text: true), сообщение будет обработано только если содержит указанный текст.
Если включено копирование фрагмента (copy_fragment: true), будет отправлен только фрагмент сообщения, начинающийся с заданного префикса.
Все действия логируются в консоль.