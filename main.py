from logic import Game
from configparser import ConfigParser


def read_config(filename):
    config = ConfigParser()
    config.read(filename)
    return config['GAME_SETTINGS']


def main():
    config = read_config('settings.ini')
    min_number = int(config['MIN_NUMBER'])
    max_number = int(config['MAX_NUMBER'])
    max_attempts = int(config['MAX_ATTEMPTS'])
    starting_capital = int(config['STARTING_CAPITAL'])

    game = Game(min_number, max_number, max_attempts, starting_capital)
    game.start()


if __name__ == "__main__":
    main()
