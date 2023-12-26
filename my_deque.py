import queue
import time

request_queue = queue.Queue()
id = 1


def generate_request():
    global id
    request_queue.put(f"Request {id}")
    id = id + 1


def process_request():
    if not request_queue.empty():
        request_queue.get()


while True:
    generate_request()
    process_request()
    time.sleep(1)
