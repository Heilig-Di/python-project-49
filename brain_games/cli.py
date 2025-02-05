#!/usr/bin/env python3

import prompt


def main():
    print('Welcome to the Brain Games!')


if __name__ == '__main__':
    main()


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
