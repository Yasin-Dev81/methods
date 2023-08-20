"""
((Direct Exchenge))
- with: work queue

- تا کار قبلی تمام نشده باشد پیام جدیدی ارسال نمیکند
ch.basic_qos(prefetch_count=1)
"""
import pika
import time


# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch = connection.channel()

# defind or create queue
ch.queue_declare(queue="hello", durable=True )

def callback(ch, method, properties, body):
    print(f"Received {body}")
    print("Headers:", properties.headrs)
    time.sleep(9)
    print('Done.')
    # ack --> 10
    ch.basic_ack(delivery_tag=method.delivery_tag) # remove message

# ارسال پیام‌ها بصورت یکی یکی باشد
ch.basic_qos(prefetch_count=1)

ch.basic_consume(
    queue="hello",
    on_message_callback=callback
)

ch.start_consuming()
