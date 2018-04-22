import select
import socket
import online_constants


class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server_socket.bind((online_constants.IP, online_constants.PORT))
            self.server_socket.listen(online_constants.QUEUE_LEN)
            self.open_client_sockets = []
            self.send_sockets = []
            self.rlist = []
            self.wlist = []
            self.xlist = []
            self.client_data = dict()
        except socket.error as err:
            print online_constants.ERR2 + str(err)
            self.server_socket.close()

    def update(self):
        self.rlist, self.wlist, self.xlist = select.select([self.server_socket]
                                                           + self.open_client_sockets,
                                                           self.send_sockets, self.open_client_sockets)

        for current_socket in self.send_sockets:
            for client_id, client_data in self.client_data.iteritems():
                current_socket.send(client_id + ":" + client_data + "#")  # 1:abc#2:def
            current_socket.send('-')

        for current_socket in self.rlist:
            # check for new connection
            if current_socket is self.server_socket:
                client_socket, client_address = current_socket.accept()
                self.open_client_sockets.append(client_socket)
            else:
                # receive data
                data = ''
                last_char = ''
                while last_char != '-':
                    last_char = current_socket.recv(online_constants.READ_SIZE)
                    print last_char
                    data += last_char

                print data
                self.client_data[data.split(':')[0]] = data.split(':')[1]
                self.send_sockets.append(current_socket)


        '''
        except socket.error as err:
            print ERR1 + str(err)

        finally:
            rlist[1].close()
            rlist[2].close()
        '''


def main():
    s = Server()
    end_loop = False
    while not end_loop:

        try:
            s.update()
        except socket.error as err:
            print online_constants.ERR1 + str(err)
            for sock in s.rlist:
                sock.close()
            for sock in s.wlist:
                sock.close()
            for sock in s.xlist:
                sock.close()
            end_loop = True

    for sock in s.rlist:
        s.rlist.remove(sock)
        sock.close()
    for sock in s.wlist:
        s.wlist.remove(sock)
        sock.close()
    for sock in s.xlist:
        s.xlist.remove(sock)
        sock.close()
    s.server_socket.close()


if __name__ == '__main__':
    main()
