"""
((Fanout Exchenge))
- صف را در این مرحله میسازیم

- exclusive
    * حذف اطلاعات قدیمی
"""
import pika

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch = connection.channel()

# defind or create queue
ch.exchange_declare(exchange='logs', exchange_type='fanout')

# defind or create queue
# ساخت صف با اسم رندوم
my_queue = ch.queue_declare(queue="", exclusive=True)
queue_name = my_queue.method.queue

# وصل کردن اکسچنج به صف
ch.queue_bind(exchange='logs', queue=queue_name)


def callback(ch, method, properties, body):
    print(f"Received {body}")

ch.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True # remove message after get this
)

ch.start_consuming()
