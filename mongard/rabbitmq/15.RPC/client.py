import pika
import uuid


class Sender:
    def __init__(self) -> None:
        # create connection
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        # create channel
        self.ch = self.connection.channel()
        # defind or create queue
        self.sender_queue = self.ch.queue_declare(queue='', exclusive=True)
        self.sender_queue_name = self.sender_queue.method.queue
        # get response message from queue
        self.ch.basic_consume(
            queue=self.sender_queue_name,
            on_message_callback=self.on_response
        )

    # send message to server
    def call(self, n):
        """\
        یه عدد سمت سرور میفرسته
        """
        self.response = None
        # set correlation id
        self.corr_id = str(uuid.uuid4())
        # send with direct exchange
        self.ch.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.sender_queue_name,
                correlation_id=self.corr_id
            ),
            body=str(n)
        )

        while self.response==None:
            self.connection.process_data_events()

        return self.response

    def on_response(self, ch, method, properties, body):
        if self.corr_id==properties.correlation_id:
            self.response = body
        return self.response


send = Sender()

response = send.call(30)
print(response)
