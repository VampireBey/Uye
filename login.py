from telethon.sync import TelegramClient

api_id = 24926482
api_hash = '00bb872c6a01aa3666d84af7b7ed660a'
session_name = 'userbot'

with TelegramClient(session_name, api_id, api_hash) as client:
    print("Giriş yapılıyor...")
    client.send_message('me', '✅ Giriş başarılı! Üye çekme botu hazır.')
    print("Bot oturumu oluşturuldu.")
