from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Read the IP of Redis through an ENV Var or assign 'redis' by default
REDIS_SERVICE_HOST = os.environ.get('REDIS_SERVICE_HOST','redis')
print(REDIS_SERVICE_HOST)
redis = Redis(host=REDIS_SERVICE_HOST, db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = """<h3>Hello World!</h3><br>
            Here I am having fun with Docker and Kubernetes. AWEEEESSSSOOOOOOME!!<br><br>
            <b>Visits:</b> {visits}<br><br>
            Request served by server: {hostname}
            """.format(visits=visits, hostname=socket.gethostname())
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
