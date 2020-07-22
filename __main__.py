# Start with a basic flask app webpage.
#from controllers import socketio




if __name__ == '__main__':

    from model.rnd_num import *
    socketio.run(app,host='0.0.0.0', port=8080)
