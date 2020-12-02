import socket
import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

c, adr = s.accept()

while True:
    from datetime import datetime
    now = datetime.now()
    current = now.strftime("%H:%M:%S")
    data = c.recv(BUFFER_SIZE)
    message = data.decode('utf-8')
    print ("Received [",current, "]: ", message)
    if message == "DONE":
        break