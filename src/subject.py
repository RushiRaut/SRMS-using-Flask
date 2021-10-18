from flask import *
from src.connection import cursor, db

add_subject = Blueprint ('add_subject', __name__)

@add_subject.route ('/add_subjects', methods=['GET', 'POST'])
def add_subjects():
    msg = 'please add subjects'
    if request.method == 'POST' and request.form['subject_code']:
        id = request.form['id']
        subject_code = request.form['subject_code']
        cursor.execute ('select * from subjects where subject_code = %s', (subject_code,))
        subject_found = cursor.fetchone ()
        if subject_found:
            msg = 'subject all ready exist'
        else:
            subject_name = request.form['subject_name']
            class_name = request.form['student_class_name']
            cursor.execute ('insert into subjects values(%s,%s,%s,%s)', (id, subject_name, subject_code, class_name))
            db.commit ()
            msg = 'subject added successfully'
            cursor.execute ('select * from subjects')
            subjects = cursor.fetchall ()
            columns = ["id", "subject_name", "subject_code", "class_name"]
            subject_details = [dict (zip (columns, row)) for row in subjects]
            return render_template ('add_subject.html', row=subject_details)
    cursor.execute ("select class_name from student_classes")
    class_found = cursor.fetchall ()
    columns = ["class_name"]
    class_details = [dict (zip (columns, row)) for row in class_found]
    return render_template ('add_subject.html', rows=class_details)


@add_subject.route ('/manage_subjects', methods=['GET', 'POST'])
def manage_subject():
    cursor.execute ('select * from subjects')
    subjects = cursor.fetchall ()
    columns = ["id", "subject_name", "subject_code", "class_name"]
    subject_details = [dict (zip (columns, row)) for row in subjects]
    return render_template ('manage_subject.html', row=subject_details)


@add_subject.route ('/delete/<id>')
def delete(id):
    cursor.execute ('delete from subjects where  id = %s', (id,))
    db.commit ()
    cursor.execute ('select * from subjects')
    subjects = cursor.fetchall ()
    columns = ["id", "subject_name", "subject_code", "class_name"]
    subject_details = [dict (zip (columns, row)) for row in subjects]
    return render_template ('manage_subject.html', row=subject_details)


@add_subject.route ('/pre_edit_sub/<id>', methods=['GET', 'POST'])
def pre_edit_sub(id):
    cursor.execute ('select * from subjects where id = %s', (id,))
    student = cursor.fetchone ()
    columns = ["id", "subject_name", "subject_code", "class_name"]
    subject_details = dict (zip (columns, student))
    cursor.execute ("select class_name from student_classes")
    class_found = cursor.fetchall()
    columns = ["class_name"]
    class_details = [dict (zip (columns, row)) for row in class_found]
    return render_template ('edit_subject.html', row=subject_details, row1=class_details)


@add_subject.route ('/edit_subject', methods=['GET', 'POST'])
def edit_subject():
    if request.method == 'POST' and request.form['subject_code']:
        id = request.form['id']
        subject_code = request.form['subject_code']
        subject_name = request.form['subject_name']
        class_name = request.form['student_class_name']
        cursor.execute ('update subjects set subject_name = %s,subject_code=%s, class_name=%s where id = %s',
                        ( subject_name, subject_code, class_name,id))
        db.commit ()
        msg = 'subject added successfully'
        cursor.execute ('select * from subjects')
        subjects = cursor.fetchall ()
        columns = ["id", "subject_name", "subject_code", "class_name"]
        subject_details = [dict (zip (columns, row)) for row in subjects]
        return render_template ('add_subject.html', row=subject_details)
