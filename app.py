from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/page2')
def secondpage():
    return "page2"

if __name__ == '__main__':
    app.run(host='10.100.58.236')
