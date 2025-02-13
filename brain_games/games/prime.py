import math

from brain_games.games.random_number import get_random_number

MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
	if num < 2:
		return False
	for i in range(2, int(math.sqrt(num) + 1)):
		if num % i == 0:
			return False
	return True


def generate_question():
	num = get_random_number()
	question = num
	correct_answer = 'yes' if is_prime(num) else 'no'
	return str(question), correct_answer
