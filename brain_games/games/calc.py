import random

from brain_games.consts import INSTRUCTION_CALC
from brain_games.utils import get_random_number

INSTRUCTION = INSTRUCTION_CALC


def get_random_math_sign_and_result(first_num, second_num):
	return random.choice([
		('+', first_num + second_num),
		('-', first_num - second_num),
		('*', first_num * second_num),

	])


def generate_round():
	first_num, second_num = get_random_number(), get_random_number()
	sign, result = get_random_math_sign_and_result(first_num, second_num)
	question = f'{first_num} {sign} {second_num}'
	correct_answer = result
	return question, str(correct_answer)
