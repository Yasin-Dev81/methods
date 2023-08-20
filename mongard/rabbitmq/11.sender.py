"""
((Fanout Exchenge))
- باید بجای صف، اسچنج بسازیم
- به هر صفی که فعال باشه ارسال میشه
- اگه صفی فعال نباشه پیام جایی ارسال نمیشه

"""
import pika


# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create channel
ch = connection.channel()

# create exchange
ch.exchange_declare(exchange='logs', exchange_type='fanout')

# send message
ch.basic_publish(exchange='logs', routing_key='', body='Hello World')

connection.close()
