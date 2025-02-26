import math

from brain_games.consts import INSTRUCTION_PRIME
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def is_prime(num):
	if num < 2:
		return False
	for i in range(2, int(math.sqrt(num) + 1)):
		if num % i == 0:
			return False
	return True


def generate_question_and_correct_answer():
	question = get_random_number()
	correct_answer = 'yes' if is_prime(question) else 'no'
	return str(question), correct_answer


def run_prime_game():
        INSTRUCTION = INSTRUCTION_PRIME
        run_game(generate_question_and_correct_answer, INSTRUCTION)
