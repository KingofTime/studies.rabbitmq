import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue
channel.queue_declare(queue="hello")

# Create Exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World' )

print(" [x] Sent 'Hello World!'")
connection.close()