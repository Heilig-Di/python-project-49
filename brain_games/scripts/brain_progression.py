#!/usr/bin/env python3
from brain_games.games.game_logic import play
from brain_games.games.progression import MESSAGE, generate_question


def main():
        play(generate_question, MESSAGE)


if __name__ == '__main__':
        main()
