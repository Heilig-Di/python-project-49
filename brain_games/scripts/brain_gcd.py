#!/usr/bin/env python3
import random

from brain_games.games.game_logic import play


def main():
	message = 'Find the greatest common divisor of given numbers.'

	def find_divisor(num_one, num_two):
		while num_one != 0 and num_two != 0:
			if num_one > num_two:
				num_one = num_one % num_two
			else:
				num_two = num_two % num_one
		return num_one + num_two

	def run_game():
		num_one = random.randint(1, 100)
		num_two = random.randint(1, 100)

		question = f'{num_one} {num_two}'
		result = find_divisor(num_one, num_two)
		correct_answer = str(result)

		return question, correct_answer 

	play(run_game, message)


if __name__ == '__main__':
	main()
