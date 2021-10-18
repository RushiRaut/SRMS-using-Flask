from flask import *

from src import subject
from src.connection import cursor, db

result = Blueprint ('result', __name__)


@result.route ('/view_result', methods=['GET', 'POST'])
def view_result():
    cursor.execute ('select class_name from student_classes')
    classes = cursor.fetchall ()
    columns = ['class_name']
    class_details = [dict (zip (columns, row)) for row in classes]
    cursor.execute ('select * from students')
    students = cursor.fetchall ()
    columns = ["id", "student_name", "roll_no", "student_gender", "student_mobile", "student_class_name"]
    student_details = [dict (zip (columns, row)) for row in students]
    return render_template ('add_result.html', row1=student_details, rows=class_details)


@result.route ('/view_result1', methods=['GET', 'POST'])
def view_result1():
    class_name = request.form['class_name']
    cursor.execute ('select class_name from student_classes')
    classes = cursor.fetchall ()
    columns = ['class_name']
    class_details = [dict (zip (columns, row)) for row in classes]
    cursor.execute ('select * from result where student_class_name = %s', (class_name,))
    students = cursor.fetchall ()
    columns = ["student_name", "roll_no", "student_class_name", "subject_name", "marks"]
    student_details = [dict (zip (columns, row)) for row in students]
    return render_template ('add_result.html', row1=student_details, rows=class_details)


@result.route ('/add_result/<roll_no>/<class_name>', methods=['GET', 'POST'])
def add_result(roll_no, class_name):
    cursor.execute ("select * from subjects where class_name = %s", (class_name,))
    subject_found = cursor.fetchall ()
    columns = ["id", "subject_name", "subject_code", "class_name"]
    subject_details = [dict (zip (columns, row)) for row in subject_found]
    cursor.execute ('select * from students where roll_no =%s', (roll_no,))
    students = cursor.fetchone ()
    columns = ["id", "student_name", "roll_no", "student_gender", "student_mobile", "student_class_name"]
    student_details = dict (zip (columns, students))
    return render_template ('add_result1.html', rows=subject_details, row2=student_details)


@result.route ('/post_add_result', methods=['GET', 'POST'])
def post_add_result():
    roll_no = request.form['roll_number']
    student_name = request.form['student_name']
    class_name = request.form['student_class_name']
    cursor.execute ('select subject_name from subjects where class_name = %s', (class_name,))
    subjects = cursor.fetchall ()
    subjects = [sub[0] for sub in subjects]
    for subject_name in subjects:
        marks = request.form[subject_name]
        cursor.execute ('select * from result where roll_no = %s and subject_name = %s', (roll_no, subject_name))
        details = cursor.fetchone ()
        if details:
            cursor.execute ('update result set marks = %s', (marks,))
            db.commit ()
        else:
            cursor.execute ('insert into result values(%s,%s,%s,%s,%s)',
                            (roll_no, student_name, class_name, subject_name, marks))
            db.commit ()
    cursor.execute ('select * from result')
    student = cursor.fetchall ()
    columns = ["roll_no", "student_name", "student_class_name", "subject_name", "marks"]
    student_result = [dict (zip (columns, row)) for row in student]
    return render_template ('add_result1.html', row2=student_result)


@result.route ('/view/<roll_no>', methods=['GET', 'POST'])
def view(roll_no):
    cursor.execute ('select * from result where roll_no =%s', (roll_no,))
    student = cursor.fetchall ()
    columns = ["roll_no", "student_name", "student_class_name", "subject_name", "marks"]
    student_result = [dict (zip (columns, row)) for row in student]
    cursor.execute ('select * from students where roll_no =%s', (roll_no,))
    students = cursor.fetchone ()
    columns = ["id", "student_name", "roll_no", "student_gender", "student_mobile", "student_class_name"]
    student_details1 = dict (zip (columns, students))
    return render_template ('view_result.html', row2=student_result,row = student_details1)


@result.route ('/view_res', methods=['GET','POST'])
def view_res():
    class_details = []
    if request.method.lower () == 'post' and request.form['roll_no']:
        roll_no = request.form['roll_no']
        class_name = request.form['class_name']
        cursor.execute ('select * from result where roll_no =%s and class_name =%s', (roll_no, class_name))
        student = cursor.fetchall ()
        if student:
            columns = ["roll_no", "student_name", "student_class_name", "subject_name", "marks"]
            student_result = [dict (zip (columns, row)) for row in student]
            cursor.execute ('select * from students where roll_no =%s', (roll_no,))
            students = cursor.fetchone ()
            columns = ["id", "student_name", "roll_no", "student_gender", "student_mobile", "student_class_name"]
            student_details = dict (zip (columns, students))
            return render_template ('view_result_student.html', row2=student_result,row = student_details)
    else:
        cursor.execute ('select * from student_classes')
        classes = cursor.fetchall ()
        columns = ["id", "class_name", "class_name_num", "section"]
        class_details = [dict (zip (columns, row)) for row in classes]
        msg = 'Student not found'
        return render_template ('form.html', row=class_details, msg=msg)
    return render_template ('form.html',row = class_details)