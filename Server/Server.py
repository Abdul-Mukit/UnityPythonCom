import time
import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

for i in range(10):
    #  Do some 'work'
    time.sleep(1)

    output = [i, i+1, i+2, i+3, i+4, i+5]
    output = ",".join(str(e) for e in output)

    #  Wait for next request from client
    t1 = time.time()
    message = socket.recv()
    print("Received request: %s" % message)

    #  Send reply back to client
    socket.send_string(output)
    t2 = time.time()
    # print(f"FPS for comm: {1 / (t2 - t1)}")