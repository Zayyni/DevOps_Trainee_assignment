from flask import Flask,render_template
from flask_socketio import SocketIO
from threading import Thread
import time
import cpu_usage_moniter

app = Flask(__name__)
socketio=SocketIO(app)

def post_cpu_usage():
    while True:
        cpu_usage = cpu_usage_moniter.cpu_usage()
        socketio.emit('cpu_usage',{'usageData':cpu_usage})
        time.sleep(0.5)

@app.route('/')
def index():
    return render_template('moniter.html')


if __name__=="__main__":
    socketio.start_background_task(target=post_cpu_usage)

    socketio.run(app)