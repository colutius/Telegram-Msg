import os

os.getenv('message')
os.environ.get('message')
message = os.environ['message']

print(message)