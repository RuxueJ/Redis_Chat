import redis

def redis_subscribe():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    pubsub = r.pubsub()
    pubsub.subscribe('chatroom')

    print("Subscribed to chatroom channel.Listening for messages...")

    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received message: {message['data']}")