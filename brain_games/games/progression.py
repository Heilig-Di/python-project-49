from brain_games.consts import INSTRUCTION_PROGRESSION
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def generate_question_and_correct_answer():
	start = get_random_number()
	difference = get_random_number(1, 11)
	length = get_random_number(5, 11)

	hidden_i = get_random_number(1, length - 2)
	progression = [
		str(start + i * difference) if i != hidden_i
		else '..' for i in range(length)
	]
	question = ' '.join(progression)
	correct_answer = start + hidden_i * difference
	return question, str(correct_answer)


def run_progression_game():
        INSTRUCTION = INSTRUCTION_PROGRESSION
        run_game(generate_question_and_correct_answer, INSTRUCTION)
