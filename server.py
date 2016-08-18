from flask import Flask

app = Flask('myapp')

@app.route('/')
def home():
    return 'hello world'

app.run()
