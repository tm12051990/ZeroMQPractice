import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5555")
for i in range (3):
    message = f"Hello {i}"
    socket.send_string(message)
    print(f"Sent {message}")
    time.sleep(1)