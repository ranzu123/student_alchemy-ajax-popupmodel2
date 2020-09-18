import flask, json
from flask import render_template,request,redirect,jsonify
from student_app import app,db
from student_app.models import Student

@app.route('/')
@app.route('/list')
def list():
    return  render_template('list.html', students=Student.query.all())


@app.route('/add')
def add_get():
    return render_template('add.html')


@app.route('/add', methods=["POST"])
def add_post():
    data = request.json
    student = Student(**data)
    db.session.add(student)
    db.session.flush()
    db.session.commit()
    print(student.id_)
    resp_data = {"id_":student.id_,
                "name":student.name,
                "grade":student.grade,
                "faculty":student.faculty,
                "section":student.section,
                "roll_no":student.roll_no,
                "age":student.age,
                "gender":student.gender,
                "address":student.address,
                "parent_name":student.parent_name}

    return jsonify({"msg": "Add Successfully", "status":200, "data":resp_data})
    
        

@app.route('/edit/<id_>')
def edit_get(id_):
    student = Student.query.filter_by(id_=id_).first()
    print(student.section)
    print(student.gender)
    return render_template('edit.html',
                            section=student.section,
                            gender=student.gender, 
                            id_ = id_)



@app.route('/student/detail/<id_>')
def detail_get(id_):
    student = Student.query.filter_by(id_=id_).first()
    print(student.section)
    print(student.gender)
    return jsonify({"id_":id_,
                    "name":student.name,
                    "grade":student.grade, 
                    "faculty":student.faculty,
                    "section": student.section, 
                    "roll_no": student.roll_no, 
                    "age": student.age,
                    "gender": student.gender, 
                    "address":student.address, 
                    "parent_name": student.parent_name})



@app.route('/edit', methods=["POST"])
def edit_post():
    data = request.json
    print("data",request.json)
    db.session.query(Student).filter_by(id_=data["id_"]).update(data)
    db.session.commit()
    return jsonify({"msg": "Edit Successfully", "status":200})


@app.route('/delete/<id_>')
def delete_get(id_):
    
    student = Student.query.filter_by(id_=id_).delete()
    db.session.commit()
    return jsonify({"msg": "Delete Successfully", "status":200})
