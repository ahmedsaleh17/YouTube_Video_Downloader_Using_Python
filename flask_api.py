from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    return "Hello from home page"


if __name__ == "__main__":
    app.run()
