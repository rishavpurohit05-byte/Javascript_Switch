from flask import Flask, render_template, request

app = Flask(__name__)

def ai_response(question):
    q = question.lower()

    if "ai" in q:
        return "Artificial Intelligence is the simulation of human intelligence in machines."

    elif "machine learning" in q:
        return "Machine Learning is a subset of AI that allows systems to learn from data."

    elif "python" in q:
        return "Python is a popular programming language used in AI, web development, and data science."

    elif "flask" in q:
        return "Flask is a lightweight Python web framework."

    elif "exam" in q or "study" in q:
        return "Make a timetable, revise daily, and practice previous year questions."
    
    elif "exam stress" in q:
        return "Take breaks, sleep well, and revise smartly."
    
    else:
        return "Sorry, I am still learning. Please ask a basic study-related question."

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = ai_response(question)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
