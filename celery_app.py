from celery import Celery

# Set RabbitMQ as the broker and use 'rpc' as the result backend
app = Celery('tasks', 
             broker='amqp://guest@localhost//',
             backend='rpc://')

@app.task
def add(x, y):
    return x + y
