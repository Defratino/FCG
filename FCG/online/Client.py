import socket
import online_constants


class Client:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def _update(self, data):
        self.socket.send(data)
        data = ''
        last_char = ''
        while last_char != '-':
            last_char = self.socket.recv(online_constants.READ_SIZE)
            data += last_char

        print data


def main():
    c = Client('127.0.0.1', online_constants.PORT)
    c._update('1:hi-')
    c.socket.close()


if __name__ == '__main__':
    main()