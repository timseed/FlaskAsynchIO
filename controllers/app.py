
# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
import os

__author__ = 'slynn'
template_dir = os.path.abspath('./templates')
print(f"setting template_dir to {template_dir}")
app = Flask(__name__,template_folder=template_dir)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['ENV'] = 'Development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_DEBUG'] = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
