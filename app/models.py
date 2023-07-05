from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Workout(db.Model):
    __tablename__ = "workout"
    id = db.Column(db.Integer, primary_key=True)
    workout_name = db.Column(db.String(128), index=True, unique=True)
    instance = db.relationship('Workout_Instance', backref='workout', lazy=True)


class Workout_Instance(db.Model):
    __tablename__ = 'workout_instance'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    
    date = db.Column(db.Date, index=True)
    duration = db.Column(db.Interval, index=True)
    total_weight = db.Column(db.Integer, index=True)
    prs = db.Column(db.Integer, index=True)

    instance = db.relationship('Exercise_Set', backref='workout_instance', lazy=True)


class Exercise(db.Model):
    __tablename__ = "exercise"

    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(128), index=True, unique=True)


class Exercise_Set(db.Model):
    __tablename__ = "exercise_set"

    id = db.Column(db.Integer, primary_key=True)
    workout_instance_id = db.Column(db.Integer, db.ForeignKey('workout_instance.id'), nullable=False)

    set_number = db.Column(db.Integer, index=True)
    set_weight = db.Column(db.Integer, index=True)
    set_reps = db.Column(db.Integer, index=True)
    rest_timer = db.Column(db.Integer, index=True)
    set_notes = db.Column(db.String(128), index=True)