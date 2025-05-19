from flask import Flask, render_template, request
import redis
import threading
from pubsub import redis_subscribe


app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    r.publish('chatroom', message)
    return '', 204

if __name__ == '__main__':
    threading.Thread(target=redis_subscribe, daemon=True).start()
    app.run(debug=True, use_reloader=False)

