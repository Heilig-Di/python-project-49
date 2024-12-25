#!/usr/bin/env python3

import random

import prompt


def welcome_user():
	name = prompt.string('May I have your name? ')
	print('Hello, ', name, '!')
	return name


def main():
	print('Welcome to the Brain Games!')

	name = welcome_user()
	print('Answer "yes" if the number is even, otherwise answer "no".')
	correct = 0

	while correct < 3:
		number = random.randint(1, 100)

		def check_even(number):
			if number % 2 == 0:
				return 'even'

			else:
				return 'not even'

		result = check_even(number)
		answer = input(f'Question: {number}\nYour answer: ').lower()

		if ((answer == 'yes' and result == 'even') or
				(answer == 'no' and result == 'not even')):
			print('Correct!')
			correct += 1

		else:
			print(f"'{answer}' is wrong answer :(\nLet's try again, {name}!")
			correct = 0

	print(f'Congratulations, {name}!')

	if __name__ == '__main':
		main()
