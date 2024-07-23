from flask import Flask
import random

random_no = random.randint(0,9)
print(random_no)

app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def guess_no(guess):
    if guess > random_no:
        return '<h1 style="color:grey">Too high, try again!</h1>'\
                '<img src = "https://media.giphy.com/media/YLxD2fPjWPw6A/giphy.gif">'

    elif guess < random_no:
        return '<h1 style = "color:blue">It\'s too low, try again  </h1>'\
                '<img src = "https://media4.giphy.com/media/yJCm3rCR3SPaavovWn/giphy.gif?cid=6c09b952ffnmjvvzx3u3d5f3aubzfy6mupshggydkgmvqgzk&ep=v1_gifs_search&rid=giphy.gif&ct=g">'


    else:
        return '<h1 style = "color: brown"> You Found Me!!<h1>'\
               '<img src = "https://i.pinimg.com/originals/ab/a0/80/aba0809849ad3532eaa92a21efa84849.gif">'





if __name__ == "__main__":
    app.run(debug=True)