from flask import redirect, render_template, url_for
from app import create_app

app = create_app()

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error = error, ide = '404')

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html', error = error, ide = '500')


@app.route('/')
def index():
    return redirect(url_for('auth.login'))