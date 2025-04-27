import yaml
from pyrogram import Client, filters

with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

with open('source_channels.txt', 'r', encoding='utf-8') as f:
    source_channels = [line.strip() for line in f if line.strip()]

with open('send_channels.txt', 'r', encoding='utf-8') as f:
    send_channels = [line.strip() for line in f if line.strip()]

app = Client(
    "my_session",
    api_id=config['api_id'],
    api_hash=config['api_hash']
)

@app.on_message(filters.channel)
async def handler(client, message):
    chat_id = str(message.chat.id)
    chat_username = message.chat.username

    if chat_id in source_channels or (chat_username and chat_username in source_channels):
        text = message.text or ""
        print(f"[INFO] Получено сообщение из канала {chat_id or chat_username}: {text}")

        if config['require_text']:
            if config['required_text'] not in text:
                print("[INFO] Сообщение не содержит обязательный текст, пропущено.")
                return

        if config['copy_fragment']:
            prefix = config['fragment_prefix']
            max_len = config['fragment_max_length']
            idx = text.find(prefix)
            if idx != -1:
                fragment = text[idx:]
                fragment = fragment.split()[0][:max_len]
                for target in send_channels:
                    await client.send_message(target, fragment)
                    print(f"[SUCCESS] Фрагмент отправлен в {target}: {fragment}")
                return
            else:
                print("[INFO] Сообщение не содержит нужного фрагмента, пропущено.")
                return

        for target in send_channels:
            await client.send_message(target, text)
            print(f"[SUCCESS] Сообщение отправлено в {target}.")

app.run()