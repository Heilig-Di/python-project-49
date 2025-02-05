from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet

greet()
name = welcome_user()


def play(run_game, message):
	correct = 0
	print(message)

	while correct < 3:

		question, correct_answer = run_game()
		print(f'Question: {question}')
		answer = input('Your answer: ').lower()

		if answer == correct_answer:
			print('Correct!')
			correct += 1

		else:
			print(f"'{answer}' is wrong answer :(\nLet's try again, {name}!")
			return False

	print(f'Congratulations, {name}!')
	return True
