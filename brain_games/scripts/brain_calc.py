#!/usr/bin/env python3
import random

from brain_games.games.game_logic import play


def main():
	message = 'What is the result of the expression?'

	def calculator():
		number_one = random.randint(1, 100)
		number_two = random.randint(1, 100)
		operators = ['+', '-', '*']
		operator = random.choice(operators)
		question = (f'{number_one} {operator} {number_two}')
		result = str(eval(f'{number_one} {operator} {number_two}'))
		return question, result

	def run_game():
		question, result = calculator()
		correct_answer = result
		return question, correct_answer

	play(run_game, message)


if __name__ == '__main__':
	main()
