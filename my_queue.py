import queue
import time

request_queue = queue.Queue()
id = 1


def generate_request():
    global id
    if id <= 10:
        request_queue.put(f"Request {id}")
        id = id + 1
        print("add to queue")
        return True
    return False


def process_request():
    if not request_queue.empty():
        print(f"read from queue {request_queue.get()}")


while generate_request():
    process_request()
    time.sleep(1)
