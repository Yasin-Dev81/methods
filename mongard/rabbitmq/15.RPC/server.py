import pika
import time


# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch = connection.channel()

# defind or create queue
ch.queue_declare(queue="rpc_queue")


def callback(ch, method, properties, body):
    print(f"Received {body}")
    time.sleep(5)
    n = int(body)
    n += 1
    print("Sending new n:", n)
    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(
            correlation_id=properties.correlation_id
        ),
        body=str(n)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)

# ارسال پیام‌ها بصورت یکی یکی باشد
ch.basic_qos(prefetch_count=1)

ch.basic_consume(
    queue="rpc_queue",
    on_message_callback=callback
)

ch.start_consuming()
