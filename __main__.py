from controllers import socketio
from controllers.app import app

"""
Project to demonstration Async IO in flask/Web
"""
if __name__ == "__main__":
    from model.rnd_num import *
    from model.hello import *

    socketio.run(app, host="127.0.0.1", port=5000)
