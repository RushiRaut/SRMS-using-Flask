from flask import *

from src.connection import cursor

log_in = Blueprint ('log_in', __name__)
log_out = Blueprint ('log_out', __name__)


@log_in.route ('/', methods=['GET', 'POST'])
def login():
    msg = ''
    cursor.execute ('select * from student_classes')
    classes = cursor.fetchall ()
    columns = ["id", "class_name", "class_name_num", "section"]
    class_details = [dict (zip (columns, row)) for row in classes]
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor.execute ('SELECT * FROM auth_user WHERE username = % s AND password = % s', (username, password))
        account = cursor.fetchone ()
        if account:
            session['loggedin'] = True
            session['username'] = account[0]
            msg = 'Logged in successfully !'
            count = []
            cursor.execute('select count(*) from students')
            count.append(cursor.fetchone())
            cursor.execute ('select count(*) from subjects')
            count.append (cursor.fetchone())
            cursor.execute ('select count(*) from student_classes')
            count.append (cursor.fetchone())
            return render_template ('dashboard.html',row = count, msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template ('form.html',row = class_details, msg=msg)


@log_out.route ('/logout')
def logout():
    session.pop ('loggedin')
    session.pop ('username')
    return redirect (url_for ('login'))


