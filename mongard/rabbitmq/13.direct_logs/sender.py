import pika


# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch = connection.channel()

# defind or create queue
ch.exchange_declare(exchange='direct_logs', exchange_type='direct')

messages = {
    'info': "INFO message",
    'error': "ERROR message",
    'warning': "WARNINIG message"
}

for k, v in messages.items():
    ch.basic_publish(exchange='direct_logs', routing_key=k, body=v)

connection.close()
