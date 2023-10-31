import socket

def send_msg(sock, msg):
    total_b = 0
    total_bb = len(msg)
    while total_b < total_bb:
        sent_len = sock.send(msg[total_b:])
        if sent_len == 0:
            raise RuntimeError("socket connection broken")
        total_b += sent_len

def recv_msg(sock, chu=1024):
    while True:
        received_chu = sock.recv(chu)
        if len(received_chu) == 0:
            break
        yield received_chu

def main():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('127.0.0.1', 80))
    request_t = 'GET / HTTP/1.1\r\n\r\n'
    request_b = request_t.encode('ASCII')
    send_msg(clientsocket, request_b)
    received_bytes = b''.join(recv_msg(clientsocket))
    received_text = received_bytes.decode('ASCII')
    print(received_text)
    clientsocket.close()

if __name__ == '__main__':
    main()
