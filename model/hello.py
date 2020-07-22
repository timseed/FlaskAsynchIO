from controllers import app
from flask import Flask, render_template, url_for, copy_current_request_context


@app.route('/hello')
def hello():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('Hello.html')