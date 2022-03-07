from tkinter.tix import Form
from turtle import title
from flask import render_template, url_for, redirect, request
from application.templates.application import app, db
from application.models import Gym
from application.templates.application.forms import OrderGym, GymForm


@app.route('/', methods=['POST', 'GET'])
def index():
    form = OrderGym()
    totals = {
        "total": Gym.query.count(),
        "total_completed": Gym.query.filter_by(complete=True).count()
    }
    if form.order_with.data == "id":
        Gym = Gym.query.order_by(Gym.id.desc()).all()
    elif form.order_with.data == "complete":
        Gym = Gym.query.order_by(Gym.complete.desc()).all()
    elif form.order_with.data == "incomplete":
        Gym = Gym.query.order_by(Gym.complete).all()
    else:
        Gym = Gym.query.all()
    return render_template('index.html', title="GYM EXERCISE APP", gym=Gym, form=form, totals=totals)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = GymForm()
    if form.validate_on_submit():
        Gym = Gym(
            task = form.task.data,
            complete = False
        )
        db.session.add(Gym)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Add a new exercise", form=form)

@app.route('/complete/<int:id>')
def complete(id):
    gym = gym.query.get(id)
    gym.complete = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = GymForm()
    gym = gym.query.get(id)
    if form.validate_on_submit():
        gym.task = form.task.data
        db.session.commit()
        redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = gym.task
    return render_template('update.html', title="Update your exercises", form=form)

@app.route('/delete/<int:id>')
def delete(id):
    gym = gym.query.get(id)
    db.session.delete(gym)
    db.session.commit()
    return redirect(url_for('index', title= "Are you sure you want to delete this exercise?"))