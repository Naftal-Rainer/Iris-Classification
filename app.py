from flask import Flask, render_template, request
import model

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/sub', methods=['POST'])
def sub():
    if request.method == 'POST':
        sepal_length = request.form['sepal_l']
        sepal_width = request.form['sepal_w']
        petal_length = request.form['petal_l']
        petal_width = request.form['petal_w']
        return render_template('index.html', species = model.predictor(sepal_length, sepal_width, petal_length, petal_width))



if __name__ == '__main__':
    app.run(debug=True)