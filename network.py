import socket
import threading

ENCODING = 'utf-8'

class Receiver(threading.Thread):

    def __init__(self, my_host, my_port):
        threading.Thread.__init__(self, name="messenger_receiver")
        self.host = my_host
        self.port = my_port

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(10)
        while True:
            connection, client_address = sock.accept()
            try:
                full_message = ""
                while True:
                    data = connection.recv(16)
                    full_message = full_message + data.decode(ENCODING)
                    if not data:
                        print("{}: {}".format(client_address, full_message.strip()))
                        break
            finally:
                connection.shutdown(2)
                connection.close()

    def run(self):
        self.listen()


class Sender(threading.Thread):

    def __init__(self, other_host, other_port):
        threading.Thread.__init__(self, name="messenger_sender")
        self.host = other_host
        self.port = other_port

    def run(self):
        while True:
            message = input("")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            s.sendall(message.encode(ENCODING))
            s.shutdown(2)
            s.close()

def main():
    my_host = input("my host : ")
    my_port = int(input("my port : "))
    receiver = Receiver(my_host, my_port)
    other_host = input("other host : ")
    other_port = int(input("other port : "))
    sender = Sender(other_host, other_port)
    treads = [receiver.start(), sender.start()]


if __name__ == '__main__':
    main()
