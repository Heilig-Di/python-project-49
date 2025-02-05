#!/usr/bin/env python3
import random

from brain_games.games.game_logic import play


def main():
	message = 'Answer "yes" if the number is even, otherwise answer "no".'

	def check_even(number):
		return number % 2 == 0

	def run_game():
		number = random.randint(1, 100)
		question = str(number)
		correct_answer = 'yes' if check_even(number) else 'no'
		return question, correct_answer

	play(run_game, message)


if __name__ == '__main__':
	main()
