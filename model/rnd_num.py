from controllers import app
from controllers import socketio
from random import random
from flask import Flask, render_template, url_for, copy_current_request_context
from controllers.socketioapp import thread as gbl_thread, thread_stop_event
from time import sleep
from threading import Thread, Event

def randomNumberGenerator():
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """
    #infinite loop of magical random numbers
    print("Making random numbers")
    while not thread_stop_event.isSet():
        number = round(random()*10, 3)
        print(number)
        socketio.emit('newnumber', {'number': number}, namespace='/test')
        socketio.sleep(5)

def delayed_start():
    sleep(3)
    randomNumberGenerator()

@app.route('/')
def index():
    global gbl_thread
    if not gbl_thread.is_alive():
        print("Starting Thread from index")
        gbl_thread = socketio.start_background_task(delayed_start)

    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    global gbl_thread
    # need visibility of the global thread object
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not gbl_thread.isAlive():
        print("Starting Thread from connect")
        thread = socketio.start_background_task(randomNumberGenerator)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


