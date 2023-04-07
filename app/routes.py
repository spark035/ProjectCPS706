from flask import render_template
from app import app
from app.forms import EdgeInputForm

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Samuel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/edges', methods=['GET', 'POST'])
def edges():
    form = EdgeInputForm()
    return render_template('graphform.html', title='Add an edge', form=form)