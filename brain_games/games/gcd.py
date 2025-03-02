import math

from brain_games.consts import INSTRUCTION_GCD
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def generate_question_and_correct_answer():
    first_num, second_num = get_random_number(), get_random_number()
    correct_answer = math.gcd(first_num, second_num)
    question = f'{first_num} {second_num}'
    return question, str(correct_answer)


def run_gcd_game():
    run_game(generate_question_and_correct_answer, INSTRUCTION_GCD)
