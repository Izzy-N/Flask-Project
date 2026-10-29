from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question', methods=["GET", "POST"])
def questionPage():

    if request.method == "POST":
        
        answer = request.form.get('answer')

        return render_template('response.html', answer=answer)

    return render_template('question.html')
#Remember to start with python -m venv venv, and on new ones pip install flask, then use flask run --debug