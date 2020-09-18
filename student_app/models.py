# from sqlalchemy.dialects.postgresql.json import JSONB
from student_app import db


class Student(db.Model):
    __tablename__ = "students"

    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    grade = db.Column(db.Integer)
    faculty = db.Column(db.String(50))
    section = db.Column(db.String(50))
    roll_no = db.Column(db.Integer)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    address = db.Column(db.String(100))
    parent_name = db.Column(db.String(50))
    

    # def __init__ (self,name,grade,faculty,section,roll_no,age,gender,address,parent_name):
    # 	self.name = name
    # 	self.grade = grade
    # 	self.faculty = faculty
    # 	self.section = section
    #     self.roll_no = roll_no
    #     self.age = age
    #     self.gender = gender
    #     self.address = address
    #     self.parent_name = parent_name
