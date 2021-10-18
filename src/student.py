from flask import *
from src.connection import cursor, db


add_student = Blueprint ('add_student', __name__)
manage_student = Blueprint('manage_student', __name__)
delete_student = Blueprint('delete_student',__name__)
edit = Blueprint('pre_edit',__name__)


@add_student.route ('/add_student1', methods=['GET', 'POST'])
def add_student1():
    class_details = {}
    msg = 'Please Fill the Form'
    if request.method.lower() == 'post' and 'student_name' in request.form and request.form['roll_no']:
        id = request.form['id']
        roll_no = request.form['roll_no']
        cursor.execute ("select * from students where roll_no =%s", (roll_no,))
        student_found = cursor.fetchone ()
        if student_found:
            msg = 'Student roll number allready exixt'
        else:
            student_name = request.form['student_name']
            student_gender = request.form['student_Gender']
            student_mobile = request.form['student_mobile']
            student_class_name = request.form['student_class_name']
            cursor.execute('insert into students values (%s,%s,%s,%s,%s,%s)',
                            (id, student_name, roll_no, student_gender, student_mobile, student_class_name))
            db.commit ()
            msg = 'Student Created Successfully'
            cursor.execute ('select * from students')
            students = cursor.fetchall ()
            columns = ["id", "student_name", "roll_no", "student_gender", "student_mobile", "student_class_name"]
            student_details = [dict (zip (columns, row)) for row in students]
            return render_template ('add_student.html', rows=student_details)
    cursor.execute("select class_name from student_classes")
    class_found = cursor.fetchall()
    columns = ["class_name"]
    class_details = [dict(zip(columns, row)) for row in class_found]
    return render_template ('add_student.html', row=class_details,msg = msg)


@manage_student.route('/manage_students', methods=['GET', 'POST'])
def manage_students():
    msg = ''
    cursor.execute('select * from students')
    students = cursor.fetchall()
    columns = ["id", "student_name", "roll_no", "student_gender", "student_mobile", "student_class_name"]
    student_details = [dict(zip(columns, row)) for row in students]
    return render_template('manage_student.html', rows=student_details)

@delete_student.route('/delete_student/<id>',methods = ['GET','POST'])
def delete1(id):
    cursor.execute('delete from students where  id = %s', (id,))
    db.commit()
    cursor.execute ('select * from students')
    students = cursor.fetchall ()
    columns = ["id", "student_name", "roll_no", "student_gender", "student_mobile", "student_class_name"]
    student_details = [dict (zip (columns, row)) for row in students]
    return render_template ('manage_student.html', rows=student_details)

@add_student.route('/pre_edit/<id>',methods=['GET','POST'])
def pre_edit(id):
    cursor.execute ('select * from students where id = %s', (id,))
    student = cursor.fetchone ()
    columns = ["id", "student_name", "roll_no", "student_gender", "student_mobile", "student_class_name"]
    student_details = dict (zip (columns, student))
    cursor.execute ("select class_name from student_classes")
    class_found = cursor.fetchall ()
    columns = ["class_name"]
    class_details = [dict (zip (columns, row)) for row in class_found]
    return render_template ('edit_student.html', row=student_details, row1=class_details)


@add_student.route('/edit_student', methods=['POST','GET'])
def edit_student():
    if request.method == 'POST' and 'student_name' in request.form and request.form['roll_no']:
        id = request.form['id']
        roll_no = request.form['roll_no']
        student_name = request.form['student_name']
        student_gender = request.form['student_Gender']
        student_mobile = request.form['student_mobile']
        student_class_name = request.form['student_class_name']
        cursor.execute ('update students set id =%s ,student_name = %s,roll_no=%s, student_gender=%s,'
                        'student_mobile=%s,student_class_name=%s where id = %s',
                        (id, student_name, roll_no, student_gender, student_mobile, student_class_name, id))
        db.commit ()
    cursor.execute ('select * from students')
    students = cursor.fetchall ()
    columns = ["id", "student_name", "roll_no", "student_gender", "student_mobile", "student_class_name"]
    student_details = [dict (zip (columns, row)) for row in students]
    return render_template ('manage_student.html', rows=student_details)