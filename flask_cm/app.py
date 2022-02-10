from flask import Flask, render_template, flash
from flask_codemirror import CodeMirror
from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField
import pycompile
# from gevent.pywsgi import WSGIServer

class MyForm(FlaskForm):
    source_code = CodeMirrorField(language='python', config={'lineNumbers': 'true'})
    submit = SubmitField('Submit')

# mandatory
CODEMIRROR_LANGUAGES = ['python', 'yaml', 'htmlembedded']
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret'
# optional
CODEMIRROR_THEME = '3024-day'
CODEMIRROR_ADDONS = (
        ('ADDON_DIR','ADDON_NAME'),
)
app = Flask(__name__)
app.config.from_object(__name__)
codemirror = CodeMirror(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = MyForm()
    result=""
    if form.validate_on_submit():
        text = form.source_code.data
        result = pycompile.main(text)
        print(result)
    return render_template('index.html', form=form, result=result)

def showCode():
    form = MyForm()

    if form.validate_on_submit():
        text = form.source_code.data
        code = pycompile.main(text)
        return code

    return "error"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # server = WSGIServer(('0.0.0.0',5000),app)
    # server.serve_forever()