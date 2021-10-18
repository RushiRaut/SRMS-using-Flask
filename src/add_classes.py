from src.connection import cursor, db
from flask import *

add_classes = Blueprint ('add_classes', __name__)
manage_classes = Blueprint ('manage_classes', __name__)
delete = Blueprint ('delete1', __name__)
edit = Blueprint ('pre_edit1', __name__)
edit_class1 = Blueprint ('edit_class', __name__)


@add_classes.route ('/add_class', methods=['GET', 'POST'])
def add_class():
    msg = ''
    if request.method == 'POST' and 'class_name' in request.form and request.form['class_name'] and request.form[
        'class_id']:
        class_name = request.form['class_name']
        cursor.execute ('select * from student_classes where class_name = %s', (class_name,))
        class_found = cursor.fetchone ()
        if class_found:
            msg = 'class allready exixts'
        else:
            classid = request.form['class_id']
            classnamenum = request.form['class_name_num']
            section = request.form['section']
            cursor.execute ('insert into student_classes values (%s,%s,%s,%s)',
                            (classid, class_name, classnamenum, section))
            db.commit ()
            msg = 'Class added successfully'
            cursor.execute ('select * from student_classes')
            classes = cursor.fetchall ()
            columns = ["id", "class_name", "class_name_num", "section"]
            class_details = [dict (zip (columns, row)) for row in classes]
            return render_template ('add_classes.html', rows=class_details)
    else:
        msg = 'please fill the form'
    return render_template ('add_classes.html', msg=msg)


@add_classes.route ('/manage_class', methods=['GET', 'POST'])
def manage_class():
    msg = ''
    cursor.execute ('select * from student_classes')
    classes = cursor.fetchall ()
    columns = ["id", "class_name", "class_name_num", "section"]
    class_details = [dict (zip (columns, row)) for row in classes]
    return render_template ('manage_classes.html', rows=class_details)


@add_classes.route ('/delete1/<id>', methods=['GET'])
def delete1(id):
    cursor.execute ('delete from student_classes where  id = %s', (id,))
    db.commit ()
    cursor.execute ('select * from student_classes')
    classes = cursor.fetchall ()
    columns = ["id", "class_name", "class_name_num", "section"]
    class_details = [dict (zip (columns, row)) for row in classes]
    return render_template ('manage_classes.html', rows=class_details)


@add_classes.route ('/pre_edit1/<id>', methods=['GET', 'POST'])
def pre_edit1(id):
    cursor.execute ('select * from student_classes where id = %s', (id,))
    classes = cursor.fetchone ()
    columns = ["class_id", "class_name", "class_name_num", "section"]
    class_details = dict (zip (columns, classes))
    return render_template ('edit_class.html', row=class_details)


@add_classes.route ('/edit_class', methods=['POST', 'GET'])
def edit_class():
    if request.method == 'POST' and 'class_name' in request.form and request.form['class_name'] and request.form[
        'class_id']:
        class_name = request.form['class_name']
        classid = request.form['class_id']
        classnamenum = request.form['class_name_num']
        section = request.form['section']
        cursor.execute (f"update student_classes set class_name='{class_name}',"
                        f"class_name_numric='{classnamenum}', section='{section}' where id = {classid}")
        db.commit ()

    cursor.execute ('select * from student_classes')
    classes = cursor.fetchall ()
    columns = ["id", "class_name", "class_name_num", "section"]
    class_details = [dict (zip (columns, row)) for row in classes]
    return render_template ('manage_classes.html', rows=class_details)
