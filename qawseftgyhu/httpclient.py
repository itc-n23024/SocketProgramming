import socket

def send_msg(sock, msg):
    total_sent_len = 0
    total_msg_len = lem(msg)
    while total_sent_len < total_msg_len:
        sent_len = sock.send(msg[total_sent_len:])
        if sent_len == 0:
            raise RuntimeError('socket connection broken')
        total_sent_len += sent_len

def recv_msg(sock, chunk_len=1024):
    while True:
        received_chunk = sock.recv(chunk_len)
        if len(received_chunk) == 0:
            break
        yield received_chunk

def main():
    client_socket = socket.socket(socket_AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    request_text = 'GET / HTTP/1.1\r\n\r\n'
    request_bytes = request_text.encode('UTF-8')
    send_msg(client_socket, request_bytes)
    received_bytes = b''.join(recv_msg(client_socket))
    received_text = rceived_bytes.decode('UTF-8')
    print(received_text)
    client_socket.close()

if __name__ == '__main__':
    main()
