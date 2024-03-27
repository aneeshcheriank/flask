from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/<name>')
def sample(name):
    return f'Hi, {name}'

if __name__ == '__main__':
    app.run()