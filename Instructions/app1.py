import sqlite3 as sql
from flask import Flask, jsonify
from itertools import chain
from datetime import datetime



#################################################
# Database Setup
#################################################
# conn = sqlite3.connect('titanic.sqlite')
# But should ideally be done at each stage

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/names")
def names():
    with sql.connect("titanic.sqlite") as con:
        cur = con.cursor()
        cur.execute("select name from Passenger")
        rows = cur.fetchall()
        rows = list(chain.from_iterable(rows))
    con.close()
    return jsonify(rows)


@app.route("/api/v1.0/passengers")
def passengers():
    with sql.connect("titanic.sqlite") as con:
        cur = con.cursor()
        cur.execute("select name, age, sex from Passenger")
        rows = cur.fetchall()
        # rows = list(chain.from_iterable(rows))
    con.close()
    passengers = {}
    for name, age, sex in rows:
        passengers[name] = {"age":age, "sex":sex}

    start =  datetime.now()
    print("'Zenni, Mr Philip' is {} years old".format(passengers["Zenni, Mr Philip"]["age"]))
    end =  datetime.now()
    print("Time is {}".format(end-start))

    return jsonify(passengers)


if __name__ == '__main__':
    app.run(debug=True)
