#!/usr/bin/env python3

def main():
    print('Welcome to the Brain Games!')

if __name__ == '__main__':
    main()

import prompt
def welcome_user():
	name = prompt.string('May I have your name? ')
	print('Hello, ', name, '!')
