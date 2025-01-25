from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet

greet()
name = welcome_user()


def play(run_game, message):
	correct = 0
	print(message)

	while correct < 3:

		question, correct_answer = run_game()
		answer = input(f'Question: {question}\nYour answer: ').lower()

		if answer == correct_answer:
			print('Correct!')
			correct += 1

		else:
			print(f"'{answer}' is wrong answer :(\nLet's try again, {name}!")
			correct = 0

	print(f'Congratulations, {name}!')
