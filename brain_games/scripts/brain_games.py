<<<<<<< HEAD
def greet():
    print(__name__)
    __name__ = 'Welcome to the Brain Games!'

    if __name__ == '__main__':
       return main()
=======
from brain_games.cli import welcome_user


def main():
    welcome_user()


if __name__ == '__main__':
    main()
>>>>>>> c88d48a57f630dd7276e73d08e66d988ada97333
