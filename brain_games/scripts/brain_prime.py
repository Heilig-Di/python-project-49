#!/usr/bin/env python3
from brain_games.engine import give_results
from brain_games.games.prime import INSTRUCTION, generate_round


def main():
	give_results(generate_round, INSTRUCTION)


if __name__ == '__main__':
	main()
