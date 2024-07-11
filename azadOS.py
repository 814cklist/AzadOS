from flask import Flask, render_template
from flask_htmx import HTMX
app = Flask(__name__)
htmx = HTMX(app)

# ROUTES

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    # Make the first ever user to visit the site go to this page
    return render_template('signup.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route("/habits")
def habits():
    return render_template('habits.html')

@app.route("/routines")
def routines():
    return render_template('routines.html')

@app.route("/weight")
def weighttracking():
    return render_template('weight.html')

@app.route("/gripstrength")
def gripstrength():
    return render_template('gripstrength.html')

@app.route("/meditation")
def meditation():
    return render_template('meditation.html')

@app.route("/journaling")
def journaling():
    return render_template('journaling.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')

@app.route("/todos")
def todos():
    return render_template('todos.html')

@app.route("/workouthistory")
def workouthistory():
    return render_template('workouthistory.html')

@app.route("/newworkout")
def newworkout():
    return render_template('newworkout.html')



if __name__ == '__main__':
    app.run(debug=True)