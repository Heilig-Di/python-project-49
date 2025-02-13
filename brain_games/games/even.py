from brain_games.games.random_number import get_random_number

MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
	number = get_random_number()
	question = number
	even = number % 2 == 0
	correct_answer = 'yes' if even else 'no'
	return str(question), correct_answer
