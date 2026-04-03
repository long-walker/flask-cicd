from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Flask CI/CD! Version 2 - deployed by Jenkins!"


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
