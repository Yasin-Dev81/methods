"""
((Direct Exchenge))
"""
import pika

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch2 = connection.channel()

# defind or create queue
ch2.queue_declare(queue="hello")


def callback(ch, method, properties, body):
    print(f"Received {body}")

ch2.basic_consume(
    queue="hello",
    on_message_callback=callback,
    auto_ack=True # remove message after get this
)

ch2.start_consuming()
