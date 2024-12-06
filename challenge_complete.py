from flask import Flask, render_template, request, flash
import sqlite3
from datetime import datetime

app=Flask("__name__")
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route("/")
def home():
    db = sqlite3.connect("database/student_marks.db")
    db.row_factory = sqlite3.Row
    studentData = db.execute("SELECT * From students").fetchall()
    
    return render_template('index.html', logged_in=True, students=studentData)

@app.route("/marks")
def marks():
    db = sqlite3.connect("database/student_marks.db")
    db.row_factory = sqlite3.Row
    markData = db.execute("SELECT * From marks").fetchall()
    
    return render_template('marks.html', logged_in=True, marks=markData)

@app.route("/student/<id>")
def student(id):
    db = sqlite3.connect("database/student_marks.db")
    db.row_factory = sqlite3.Row
    studentData = db.execute(f"SELECT * FROM students WHERE id={id}").fetchone()

    markData = db.execute(f"SELECT * FROM marks WHERE student_id={id}").fetchall()

    html = f"""
            The student information is<br>
            Firstname: {studentData['firstname']}<br>
            Lastname: {studentData['lastname']}<br>
            DOB: {studentData['dob']}<br>
    """
    for result in markData:
        html += f"Mark for {result['subject']} is {result['mark']} <br>"

    return html

def convert_date_format(date_str):
    # Split the input date into components
    year, month, day = date_str.split("-")
    # Rearrange and join them in the desired format
    return f"{day}/{month}/{year}"


@app.route("/add", methods=("GET", "POST"))
def AddStudent():

    #Did the user post data?
    if request.method == "POST":

        #Get the values from the form
        firstname = request.form['firstname']
        lastname  = request.form['lastname']
        dob       = convert_date_format(request.form['dob'])



        # Connect to the database
        db = sqlite3.connect("database/student_marks.db")
        cursor = db.cursor()

        # Check if the student already exists
        cursor.execute("SELECT * FROM Students WHERE firstname = ? AND lastname = ? AND dob = ?", 
                       (firstname, lastname, dob))
        existing_student = cursor.fetchone()

        if existing_student:
            # Student exists, show a message
            flash(f"Student {firstname} {lastname} with DOB {dob} already exists.", "danger")
        else:
            # Student doesn't exist, insert the new record
            cursor.execute("INSERT INTO Students('firstname', 'lastname', 'dob') VALUES (?, ?, ?)",
                           (firstname, lastname, dob))
            db.commit()
            flash(f"Student {firstname} {lastname} added successfully.", "success")
        
        db.close()

    return render_template("add.html")

app.run(debug=True, port=5001)

