from flask import Flask, render_template

app = Flask(__name__)


# ROUTES

#add logic to always route user to this page on first visit to it after install (make the whole thing into a docker container for easy local/self hosting)
@app.route("/firstsetup")
def firstsetup():
    return render_template('firstsetup.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dashboard")
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