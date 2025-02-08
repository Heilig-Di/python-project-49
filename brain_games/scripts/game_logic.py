import prompt

from brain_games.scripts.brain_games import greet

greet()


def welcome_user():
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
	return name


name = welcome_user()


def play(run_game, message):
	print(message)

	for _ in range(3):

		question, correct_answer = run_game()
		print(f'Question: {question}')
		answer = input('Your answer: ').lower()

		if answer == correct_answer:
			print('Correct!')

		else:
			print(f"'{answer}' is wrong answer :(\nLet's try again, {name}!")
			return False

	print(f'Congratulations, {name}!')
	return True
