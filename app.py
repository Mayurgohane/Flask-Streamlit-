from flask import Flask, request

app = Flask(__name__)

@app.route('/greet')
def greet():
    return 'Hiii Mayur'


if __name__ == '__main__':
    app.run()

