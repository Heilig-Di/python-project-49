import random

from brain_games.games.random_number import get_random_number

MESSAGE = 'What is the result of the expression?'


def calcute():
	first_num = get_random_number()
	second_num = get_random_number()
	operators = {
		'+': lambda x, y: x + y,
		'-': lambda x, y: x - y,
		'*': lambda x, y: x * y
	}
	operator = random.choice(list(operators.keys()))
	return first_num, second_num, operator, operators


def generate_question():
	first_num, second_num, operator, operators = calcute()
	correct_answer = operators[operator](first_num, second_num)
	question = f'{first_num} {operator} {second_num}'
	return question, str(correct_answer)
