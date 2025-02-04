from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello Word!"

@app.route("/about")
def about():
    return "Pagina sobre!"

if __name__ == "__main__":
    app.run(debug=True)