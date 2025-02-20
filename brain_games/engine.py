import prompt

from brain_games.cli import welcome_user
from brain_games.consts import (CONGRATULTIONS_MESSAGE, CORRECT_MESSAGE,
				ROUNDS, WRONG_MESSAGE)


def give_results(generate_round, INSTRUCTION):

	name = welcome_user()
	print(INSTRUCTION)

	for _ in range(ROUNDS):
		question, correct_answer = generate_round()
		print(f'Question: {question}')
		answer = prompt.string('Your answer: ').lower()

		if answer == correct_answer:
			print(CORRECT_MESSAGE)

		else:
			print(WRONG_MESSAGE.format(answer, name))
			return
	print(CONGRATULTIONS_MESSAGE.format(name))
