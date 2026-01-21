from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "quizsecret"

questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Heart", "Brain", "Skin", "Liver"],
        "answer": "Skin"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["Alan Turing", "Bill Gates", "Steve Jobs", "Charles Babbage"],
        "answer": "Charles Babbage"
    },
    {
        "question": "How many continents are there in the world?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    }
]

@app.route("/")
def index():
    session["score"] = 0
    session["qno"] = 0
    session["feedback"] = ""
    session["correct_answer"] = ""
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    qno = session.get("qno", 0)

    # Handle answer submission
    if request.method == "POST":
        selected = request.form.get("option")
        correct = questions[qno]["answer"]

        if selected == correct:
            session["score"] += 1
            session["feedback"] = "Correct! ✅"
        else:
            session["feedback"] = "Incorrect ❌"
            session["correct_answer"] = correct

        session["show_feedback"] = True
        return render_template(
            "quiz.html",
            question=questions[qno],
            qno=qno + 1,
            feedback=session["feedback"],
            correct_answer=session.get("correct_answer", ""),
            show_feedback=True
        )

    # Move to next question
    if session.get("show_feedback"):
        session["show_feedback"] = False
        session["correct_answer"] = ""
        session["qno"] += 1
        qno = session["qno"]

    if qno >= len(questions):
        return redirect(url_for("result"))

    return render_template(
        "quiz.html",
        question=questions[qno],
        qno=qno + 1,
        show_feedback=False
    )

@app.route("/result")
def result():
    return render_template(
        "result.html",
        score=session.get("score"),
        total=len(questions)
    )

@app.route("/playagain")
def playagain():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
