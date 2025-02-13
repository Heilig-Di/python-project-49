import math

from brain_games.games.random_number import get_random_number

MESSAGE = 'Find the greatest common divisor of given numbers.'


def generate_question():
	first_num = get_random_number()
	second_num = get_random_number()
	correct_answer = math.gcd(first_num, second_num)
	question = f'{first_num} {second_num}'
	return question, str(correct_answer)
