import prompt

from brain_games.consts import ROUNDS


def run_game(generate_question_and_correct_answer, INSTRUCTION):

    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    print(INSTRUCTION)

    for _ in range(ROUNDS):
        question, correct_answer = generate_question_and_correct_answer()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").lower()

        if answer == correct_answer:
            print("Correct!")

        else:
            print(f"'{answer}' is wrong answer :(\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
