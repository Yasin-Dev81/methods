"""
((Direct Exchenge))
- connection
    * channel 1
        ~ consumer 1
        ~ consumer 2
    * channel 2
        ~ consumer 3
        ~ consumer 4

ex:
- connection
    * ch1
        ~ send message
    * ch2
        ~ get message

"""
import pika


# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch1 = connection.channel()

# defind or create queue
ch1.queue_declare(queue="hello")

# send message
ch1.basic_publish(
    exchange='', # Direct Exchenge
    routing_key='hello', # target queue
    body="Hello World" # message
)

connection.close()
