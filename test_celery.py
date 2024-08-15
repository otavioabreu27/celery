from celery_app import add

# Test calling the task synchronously
result = add(4, 6)
print(f'Synchronous result: {result}')

# Test calling the task asynchronously
result = add.delay(4, 6)
print(f'Asynchronous result: {result.get()}')

