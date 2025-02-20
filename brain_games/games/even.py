from brain_games.consts import INSTRUCTION_EVEN
from brain_games.utils import get_random_number

INSTRUCTION = INSTRUCTION_EVEN


def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False


def generate_round():
	question = get_random_number()
	correct_answer = 'yes' if is_even(question) else 'no'
	return str(question), correct_answer
