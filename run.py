from student_app import app,db
db.init_app(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000)