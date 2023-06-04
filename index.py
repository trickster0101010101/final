from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    username = request.form['username']
    mail = request.form['mail']
    password = request.form['password']

    with open('users.txt', 'a') as file:
        file.write(f"Username: {username}\n")
        file.write(f"Mail: {mail}\n")
        file.write(f"Password: {password}\n")
        file.write("--------------------\n")

    return "Данные успешно отправлены и сохранены в файл 'users.txt'"

if __name__ == '__main__':
    app.run()
