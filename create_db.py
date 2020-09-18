from student_app import app,db
from student_app.models import Student

with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()
  