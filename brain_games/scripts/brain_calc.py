#!/usr/bin/env python3
from brain_games.games.calc import MESSAGE, generate_question
from brain_games.games.game_logic import play


def main():
	play(generate_question, MESSAGE)


if __name__ == '__main__':
	main()
