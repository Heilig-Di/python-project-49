import math

from brain_games.consts import INSTRUCTION_GCD
from brain_games.utils import get_random_number

INSTRUCTION = INSTRUCTION_GCD


def generate_round():
	first_num, second_num = get_random_number(), get_random_number()
	correct_answer = math.gcd(first_num, second_num)
	question = f'{first_num} {second_num}'
	return question, str(correct_answer)
