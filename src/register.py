from flask import *
from src.connection import cursor, db

reg = Blueprint('reg', __name__)


@reg.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if ((request.method == 'POST' and 'username' in request.form and 'password' in request.form) and
            (request.form['username'] and request.form['password'])):
        username = request.form['username']
        password = request.form['password']
        cursor.execute('select * from auth_user where username = %s', (username,))
        user = cursor.fetchone()
        if user:
            msg = "user allready exist"
        else:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            cursor.execute('insert into auth_user values (%s,%s,%s,%s,%s)',
                           (username, password, first_name, last_name, email))
            db.commit()
            msg = 'user created successfully'
    else:
        msg = 'please fill the form'
    return render_template('register.html', msg=msg)
