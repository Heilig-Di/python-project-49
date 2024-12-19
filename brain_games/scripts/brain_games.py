from brain_games.cli import welcome_user


def greet():
	__name__ = 'Welcome to the Brain Games!'
	print(__name__)

	if __name__ == '__main__':
		return main()


def main():
	welcome_user()


if __name__ == '__main__':
	main()
