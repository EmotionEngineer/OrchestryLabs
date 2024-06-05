from flask import Flask
import waitress

app = Flask(__name__)


@app.route('/')
def test():
    return "Test"


if __name__ == "__main__":
    waitress.serve(app, host='0.0.0.0', port=7777)
