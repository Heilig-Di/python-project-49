#!/usr/bin/env python3
import math
import random

from brain_games.games.game_logic import play


def main():
	message = 'Answer "yes" if given number is prime. Otherwise answer "no".'

	def check_prime(num):
		if num < 2:
			return False
		for i in range(2, int(math.sqrt(num) + 1)):
			if num % i == 0:
				return False
		return True

	def run_game():
		num = random.randint(1, 100)
		question = num
		correct_answer = 'yes' if check_prime(num) else 'no'

		return question, correct_answer 

	play(run_game, message)


if __name__ == '__main__':
	main()
