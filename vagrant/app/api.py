import json
import os

from flask import Blueprint, redirect, render_template, request
from flask_httpauth import HTTPBasicAuth

from __init__ import db
from models import Students

fl_app = Blueprint("app", __name__)
auth = HTTPBasicAuth()


filled = False


@auth.verify_password
def verify_password(username, password):
    user = os.environ.get("WEB_ADMIN")
    passw = os.environ.get("WEB_PASS")
    if username == user and password == passw:
        return username


@fl_app.route("/")
def home():
    return render_template("home.html")


@fl_app.route("/hello")
@auth.login_required
def hello():
    name = ""
    return render_template("hello.html", name=name)


@fl_app.route("/marks")
def marks():
    return render_template("marks.html")


@fl_app.route("/marks/tia")
def marks_tia():
    result = get_marks()
    colnames_headers = ["ID number", "Mark"]
    colnames = ["id_number", "mark_tia"]
    return render_template(
        "marks_tia.html",
        colnames=colnames,
        data=result,
        colnames_headers=colnames_headers,
    )


@fl_app.route("/marks/sist")
def marks_sist():
    result = get_marks()
    colnames_headers = ["ID number", "Mark"]
    colnames = ["id_number", "mark_sist"]
    return render_template(
        "marks_sist.html",
        colnames=colnames,
        data=result,
        colnames_headers=colnames_headers,
    )


@fl_app.route("/marks/mining")
def marks_mining():
    result = get_marks()
    colnames_headers = ["ID number", "Mark"]
    colnames = ["id_number", "mark_mining"]
    return render_template(
        "marks_mining.html",
        colnames=colnames,
        data=result,
        colnames_headers=colnames_headers,
    )


def get_marks():
    people = db.query(Students).all()
    result = []
    for person in people:
        result.append(person._dump())
    return result


@fl_app.route("/admin")
@auth.login_required
def admin():
    return render_template("admin.html")


@fl_app.route("/teacher")
@auth.login_required
def teacher():
    return render_template("teacher.html")


#
@fl_app.route("/teacher/add")
@auth.login_required
def teacher_add():
    return render_template("teacher_add.html")


# get marks of every student
@fl_app.route("/teacher/marks")
@auth.login_required
def teacher_marks():
    result = get_marks()
    colnames_headers = [
        "ID number",
        "First name",
        "Last name",
        "Gender",
        "Email",
        "Phone",
        "TIA mark",
        "Sistemas mark",
        "Mining mark",
    ]
    colnames = [
        "id_number",
        "first_name",
        "last_name",
        "gender",
        "email",
        "phone",
        "mark_tia",
        "mark_sist",
        "mark_mining",
    ]
    return render_template(
        "marks_teacher.html",
        colnames=colnames,
        data=result,
        colnames_headers=colnames_headers,
    )


# insert into database
@fl_app.route("/teacher/add/post", methods=["GET", "POST"])
@auth.login_required
def teacher_add_post():
    if request.method == "POST":
        id_number = request.form["id_number"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        gender = request.form["gender"]
        email = request.form["email"]
        phone = request.form["phone"]
        mark_tia = request.form["mark_tia"]
        mark_sist = request.form["mark_sist"]
        mark_mining = request.form["mark_mining"]
        try:
            new_student = Students(
                id_number=id_number,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                email=email,
                phone=phone,
                mark_tia=mark_tia,
                mark_sist=mark_sist,
                mark_mining=mark_mining,
            )
            db.add(new_student)
            print("ok")
            return render_template("teacher_add_ok.html", id=id_number)
        except:
            print("fail")
            return render_template("teacher_add_fail.html", id=id_number)
    return redirect("/")


# add bulk data
@fl_app.route("/add_data", methods=["GET"])
def add_data_btn():
    global filled
    if not filled:
        filled = True
        with open("/app/MOCK_DATA_MARKS.json") as json_file:
            mock_data = json.load(json_file)
            for student in mock_data:
                id_number = student.get("id_number")
                first_name = student.get("first_name")
                last_name = student.get("last_name")
                gender = student.get("gender")
                email = student.get("email")
                phone = student.get("phone")
                mark_tia = student.get("mark_tia")
                mark_sist = student.get("mark_sist")
                mark_mining = student.get("mark_mining")
                new_student = Students(
                    id_number=id_number,
                    first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    email=email,
                    phone=phone,
                    mark_tia=mark_tia,
                    mark_sist=mark_sist,
                    mark_mining=mark_mining,
                )
                db.add(new_student)
    return redirect("/", code=302)
