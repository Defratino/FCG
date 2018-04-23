import socket
import online_constants


class Client:
    def __init__(self, ip, port, client_id):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))
        self.client_id = client_id
        self.last_data = ''

    def update(self, data):
        self.socket.send(str(self.client_id) + online_constants.ID_SEPERATOR + data + online_constants.END_OF_MESSAGE)
        received_data = ''
        last_char = ''
        while last_char != online_constants.END_OF_MESSAGE:
            last_char = self.socket.recv(online_constants.READ_SIZE)
            received_data += last_char

        self.last_data = received_data[:-1]


def main():
    c = Client('127.0.0.1', online_constants.PORT, 14)
    c.update('hi')
    c.socket.close()


if __name__ == '__main__':
    main()