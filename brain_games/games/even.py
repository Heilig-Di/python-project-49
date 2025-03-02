from brain_games.consts import INSTRUCTION_EVEN
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def is_even(number):
    return number % 2 == 0


def generate_question_and_correct_answer():
    question = get_random_number()
    correct_answer = 'yes' if is_even(question) else 'no'
    return str(question), correct_answer


def run_even_game():
    run_game(generate_question_and_correct_answer, INSTRUCTION_EVEN)
