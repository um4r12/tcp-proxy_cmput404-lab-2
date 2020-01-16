import socket, sys

def create_tcp_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except :
        print("Failed to create socket")
        sys.exit()
    return s
def send_data(serversocket, payload):
    try:
        serversocket.sendall(payload.encode())
    except:
        print("Send failed")
        sys.exit()
    print("Payload successfully sent.")

def main():
    try:
        host = "www.google.com"
        port = 80
        payload = "GET / HTTP/1.0\r\nHost:" + host + "\r\n\r\n"
        buffer_size = 4096

        s = create_tcp_socket()

        s.connect((host, port))

        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        full_data = b""

        while True:
            data = s.recv(buffer_size)
            
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

main()
