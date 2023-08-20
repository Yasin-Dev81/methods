import pika


# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch = connection.channel()

# defind or create queue
ch.exchange_declare(exchange='hi_dady', exchange_type='topic')

messages = {
    'error.warning.important': "IMPORTANT message",
    'info.debug.notimportant': "NOTIMPORTANT message",
}

for k, v in messages.items():
    ch.basic_publish(exchange='hi_dady', routing_key=k, body=v)

connection.close()
