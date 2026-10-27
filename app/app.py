from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from my GitOps demo</h1><p>Version: 3.1</p>"

@app.route("/health")
def health():
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)