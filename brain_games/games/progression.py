import random

MESSAGE = 'What number is missing in the progression?'


def generate_question():
	start = random.randint(1, 100)
	difference = random.randint(1, 11)
	length = random.randint(5, 11)

	hidden_i = random.randint(1, length - 2)
	progression = [
		str(start + i * difference) if i != hidden_i
		else '..' for i in range(length)
	]
	question = ' '.join(progression)
	correct_answer = start + hidden_i * difference
	return question, str(correct_answer)
