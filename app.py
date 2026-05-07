from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/5050-foods')
def foods():
    return render_template('5050-foods.html')

@app.route('/cavelux')
def cavelux():
    return render_template('cavelux.html')

@app.route('/vital-fitness')
def fitness():
    return render_template('vital-fitness.html')

if __name__ == "__main__":
    app.run()