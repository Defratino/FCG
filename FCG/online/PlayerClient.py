import pygame
import socket
import threading
import Client
import online_constants
import display_constants
import colors


class PlayerClient(threading.Thread):
    def __init__(self, ip, port, client_id):
        threading.Thread.__init__(self)
        self.client = Client.Client(ip, port, client_id)
        self.game_display = None
        self.clock = None

    def run(self):
        self.pygame_starter()
        self.input_client()

    def input_client(self):
        to_send = pygame.key.get_pressed()
        try:
            while to_send != online_constants.END_OF_COMMUNICATION:
                self.pygame_update()
                to_send = pygame.key.get_pressed()
                if to_send[pygame.K_x]:
                    self.client.update(online_constants.END_OF_COMMUNICATION)
                else:
                    self.client.update(str(to_send))
            self.client.socket.close()
        except socket.error:
            self.client.socket.close()

    def pygame_starter(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((display_constants.DISPLAY_WIDTH, display_constants.DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()

    def pygame_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.client.socket.close()
                pygame.quit()
                quit()

        self.game_display.fill(colors.BACKGROUND)
        '''
        Dear Daniel, 
        
        self.client.last_data is where all data from all players (including you) is stored, as a string.
        Typical one would look like this: 
        1:a#2:b#
        There are 2 clients (1 and 2 are their ids), 1 is saying a, and 2 is saying b.
        Players are separated with online_constants.PLAYER_SEPERATOR and the ids are separated from the data with 
        online_constants.ID_SEPERATOR.
        Currently, if you run the Server.py file and this file together you will see printed the keys you press, if you
        press x (the key), the server will disconnect and so will you.
        Take a look in the main() function in this file to see how to start a player.
        The data from the server is the pygame.key.get_pressed() of each player, use it to make other players move on 
        screen, because i don't wanna do it.
        Take a look at the code in this class to see what is being called where, and please don't fuck this up.
               
                Suck a fat one, 
                        
                                    Ely.
        '''
        dtime = self.clock.tick(display_constants.FPS)
        pygame.display.update()

    def _input_client(self):
        to_send = ''
        try:
            while to_send != online_constants.END_OF_COMMUNICATION:
                to_send = raw_input()
                self.client.update(to_send)
                print self.client.last_data
            self.client.socket.close()
        except socket.error:
            print 'Disconnected from server'
            self.client.socket.close()

    def _old_client(self):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', online_constants.END_OF_COMMUNICATION]
        for c in chars:
            self.client.update(c)
            print self.client.last_data

        self.client.socket.close()


def main():
    pc = PlayerClient('127.0.0.1', online_constants.PORT, 2)
    pc.start()

if __name__ == '__main__':
    main()