"""
((Direct Exchenge))
- with: work queue

- Round-robin
    * روشی است که بروکر درخواست‌ها را بین دریافت کنندگان پخش میکند

- Durability
    * داخل هارد هم اطلاعات رو مینویسه
    * اگه سرور کرش کرد اطلاعاتمون از بین نمیره
    * فقط برای چنل بکار میره
    * پیغام‌ها سیو نمیشه

- Delivery mode
    * نوع انتقال پیغام‌ها را مشخص میکند
    * ذخیره در رم-1/هارد-2

"""
import pika


# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch1 = connection.channel()

# defind or create queue
ch1.queue_declare(queue="first", durable=True)

# send message
ch1.basic_publish(
    exchange='', # Direct Exchenge
    routing_key='first', # target queue
    body="--- Hello World", # message
    properties=pika.BasicProperties(
        delivery_mode=2,
        headers={'name': 'yasin'}
    )
)

connection.close()
