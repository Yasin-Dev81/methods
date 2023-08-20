import pika

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch = connection.channel()

# defind or create queue
ch.exchange_declare(exchange='hi_dady', exchange_type='topic')

# defind or create queue
# ساخت صف با اسم رندوم
my_queue = ch.queue_declare(queue="", exclusive=True)
queue_name = my_queue.method.queue

# connect queue to exchange
binding_key = "#.notimportant"
ch.queue_bind(exchange='hi_dady', queue=queue_name, routing_key=binding_key)


def callback(ch, method, properties, body):
    print(f"Received {method.routing_key}: {body}")

ch.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True # remove message after get this
)

ch.start_consuming()
