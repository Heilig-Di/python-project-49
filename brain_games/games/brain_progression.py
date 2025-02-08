#!/usr/bin/env python3
import random

from brain_games.scripts.game_logic import play


def main():
	message = 'What number is missing in the progression?'

	def generator_progression():
		start = random.randint(1, 100)
		difference = random.randint(1, 11)
		length = random.randint(5, 11)

		progression = [start + num * difference for num in range(length)]
		return progression

	def hide_number(progression):
		hidden_i = random.randint(1, len(progression) - 2)
		hidden_number = progression[hidden_i]
		progression[hidden_i] = '..'
		return progression, hidden_number

	def run_game():
		progression = generator_progression()
		progression, hidden_number = hide_number(progression)
		question = ' '.join(map(str, progression))
		correct_answer = str(hidden_number)

		return question, correct_answer

	play(run_game, message)


if __name__ == '__main__':
	main()
