#!/usr/bin/env python3
import random

from brain_games.games.game_logic import play


def main():
	message = 'Find the greatest common divisor of given numbers.'

	def find_divisor(num):
		divisors = []
		for i in range(1, int(num / 2) + 1):
			if num % i == 0:
				divisors.append(i)
		return divisors

	def run_game():
		num_one = random.randint(1, 100)
		num_two = random.randint(1, 100)

		question = f'{num_one} {num_two}'
		divisor_num_one = find_divisor(num_one)
		divisor_num_two = find_divisor(num_two)
		result = max([num for num in divisor_num_one if num in divisor_num_two])
		correct_answer = str(result)

		return question, correct_answer 

	play(run_game, message)


if __name__ == '__main__':
	main()
