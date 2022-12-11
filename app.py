from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    count = redis.incr('hits')
    return 'Hello, Docker! <p> Hostname is: ' + socket.gethostname() + '<p> I have been seen {} times. \n'.format(count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
