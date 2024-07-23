from flask import Flask
app = Flask(__name__)



@app.route("/")
def hello_world():
    return '<h1 style="text-align:center">Hello, World!<h1>'\
            '<p> This is looking too Funny<p>'\
            '<img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm5mcTNlOHFkcDFzejVqOHN1MHFuM25oYjFjeHc4Y3M0NG4wMXJpaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AlGXp8qmlIZwuiDk2L/giphy.webp">'





@app.route("/bye")


def bye():
    return "bye!"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello there {name}, and your are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)