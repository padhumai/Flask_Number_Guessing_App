from flask import Flask, render_template, request, session, redirect, url_for
import random
import mysql.connector

app = Flask(__name__)
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="number_guessing_game"
)
cursor=con.cursor()

print("Database Connected")
app.secret_key = "numbergame123"


def generate_number():
    if session["difficulty"] == "Easy":
        return random.randint(1, 20)
    elif session["difficulty"] == "Medium":
        return random.randint(1, 50)
    else:
        return random.randint(1, 100)


@app.route("/", methods=["GET", "POST"])
def home():
    if "player_name" not in session:
        session["player_name"] = ""

    if "difficulty" not in session:
        session["difficulty"] = "Hard"

    if "secret_number" not in session:
        session["secret_number"] = generate_number()

    if "attempts" not in session:
        session["attempts"] = 0

    if "score" not in session:
        session["score"] = 100

    message = ""

    if request.method == "POST":
        if "player_name" in request.form:
            session["player_name"] = request.form["player_name"]

        if "difficulty" in request.form:
            session["difficulty"] = request.form["difficulty"]
            session["secret_number"] = generate_number()
            session["attempts"] = 0
            session["score"] = 100

        elif "guess" in request.form:

            guess = int(request.form["guess"])

            if session["attempts"] < 5:

                session["attempts"] += 1

                if guess < session["secret_number"]:
                    message = "Too Low!"

                elif guess > session["secret_number"]:
                    message = "Too High!"

                else:
                    message = "Congratulations! You Won!"
                    session["score"] = 100 - ((session["attempts"] - 1) * 10)
                    cursor.execute(
                    "INSERT INTO game_results(player_name, difficulty, attempts, score, result) VALUES(%s,%s,%s,%s,%s)",
                    (session["player_name"], session["difficulty"], session["attempts"], session["score"], "Win")
                     )
                    con.commit()

            if session["attempts"] == 5 and guess != session["secret_number"]:
                message = f"Game Over! Correct Number is {session['secret_number']}"
                cursor.execute(
                "INSERT INTO game_results(player_name, difficulty, attempts, score, result) VALUES(%s,%s,%s,%s,%s)",
                (session["player_name"], session["difficulty"], session["attempts"], 0, "Lose")
                )

                con.commit()

    remaining = 5 - session["attempts"]

    return render_template(
        "index.html",
        message=message,
        attempts=session["attempts"],
        remaining=remaining,
        score=session["score"],
        difficulty=session["difficulty"]
    )


@app.route("/play_again")
def play_again():
    session["secret_number"] = generate_number()
    session["attempts"] = 0
    session["score"] = 100
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)