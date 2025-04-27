
# Telegram Channel Parser

A script for automatically copying messages from one or several Telegram channels to other channels, with options for text filtering and extracting specific message fragments.

Скрипт для автоматического копирования сообщений из одного или нескольких Telegram-каналов в другие каналы с возможностью фильтрации по тексту и выделения определённых фрагментов сообщений.

---

## 🇬🇧 English

### Features
- **Supports multiple source and target channels**
- **Filters messages by required text**
- **Copies only a specific message fragment by prefix**
- **Simple configuration via YAML and text files**
- **Logs all actions to the console**

### Installation
1. Clone the repository or download the code archive.
2. Install dependencies:
   ```bash
   pip install -r req.txt
   ```
3. Get your `api_id` and `api_hash` at [my.telegram.org](https://my.telegram.org).
4. Configure the files:
   - `config.yaml` — main settings
   - `source_channels.txt` — list of source channels (one per line, ID or username)
   - `send_channels.txt` — list of target channels (one per line, ID or username)

### Run
```bash
python main.py
```

### How does it work?
- The script monitors new messages in the specified source channels.
- If filtering is enabled (`require_text: true`), only messages containing the required text will be processed.
- If fragment copying is enabled (`copy_fragment: true`), only the fragment starting with the specified prefix will be sent.
- All actions are logged to the console.

---

## 🇷🇺 Русский

### Возможности
- **Поддержка нескольких исходных и целевых каналов**
- **Фильтрация сообщений по обязательному тексту**
- **Копирование только определённого фрагмента сообщения по префиксу**
- **Простая настройка через конфиг и текстовые файлы**
- **Логирование событий через print**

### Установка
1. Склонируйте репозиторий или скачайте архив с кодом.
2. Установите зависимости:
   ```bash
   pip install -r req.txt
   ```
3. Получите `api_id` и `api_hash` на [my.telegram.org](https://my.telegram.org).
4. Настройте файлы:
   - `config.yaml` — основные настройки
   - `source_channels.txt` — список исходных каналов (по одному в строке, ID или username)
   - `send_channels.txt` — список целевых каналов (по одному в строке, ID или username)

### Запуск
```bash
python main.py
```

### Как это работает?
- Скрипт отслеживает новые сообщения в указанных исходных каналах.
- Если включена фильтрация (`require_text: true`), сообщение будет обработано только если содержит указанный текст.
- Если включено копирование фрагмента (`copy_fragment: true`), будет отправлен только фрагмент сообщения, начинающийся с заданного префикса.
- Все действия логируются в консоль.

## Лицензия

MIT
