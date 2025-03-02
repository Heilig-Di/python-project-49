import random

from brain_games.consts import INSTRUCTION_CALC
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def get_random_math_sign_and_result(first_num, second_num):
    return random.choice(
        [
            ("+", first_num + second_num),
            ("-", first_num - second_num),
            ("*", first_num * second_num),
        ]
    )


def generate_question_and_correct_answer():
    first_num, second_num = get_random_number(), get_random_number()
    sign, correct_answer = (
		get_random_math_sign_and_result(first_num, second_num))
    question = f"{first_num} {sign} {second_num}"
    return question, str(correct_answer)


def run_calc_game():
    run_game(generate_question_and_correct_answer, INSTRUCTION_CALC)
