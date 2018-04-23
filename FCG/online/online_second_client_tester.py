import online_constants
import PlayerClient


def main():
    pc = PlayerClient.PlayerClient('127.0.0.1', online_constants.PORT, 1)
    pc.start()


if __name__ == '__main__':
    main()