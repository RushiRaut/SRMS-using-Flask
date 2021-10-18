from flask import *

from src.add_classes import add_classes, manage_classes, delete
from src.log_in import log_in, log_out
from src.register import reg
from src.result import result
from src.student import add_student, manage_student, delete_student
from src.subject import add_subject

app = Flask (__name__)
app.secret_key = 'super secret key'

app.register_blueprint (log_in)
app.register_blueprint (log_out)
app.register_blueprint (reg)
app.register_blueprint (add_classes)
app.register_blueprint (manage_classes)
app.register_blueprint (delete)
app.register_blueprint (add_student)
app.register_blueprint(manage_student)
app.register_blueprint(delete_student)
app.register_blueprint(add_subject)
app.register_blueprint(result)

@app.route ('/dashboard')
def dashboard():
    return render_template ('dashboard.html')


app.run (debug=True)
