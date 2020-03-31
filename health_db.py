from flask import Flask, jsonify, request

db = []

app = Flask(__name__)


def add_patient_name_db(name, id, age):
    new_patient = {"name": name,
                   "id": id,
                   "age": age,
                   "test": []}
    db.append(new_patient)
    print("db is {}".format(db))
    return True
