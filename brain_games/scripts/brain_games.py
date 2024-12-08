def greet(__name__):
    print(__name__)
    __name__ = 'Welcome to the Brain Games!'

    if __name__ == '__main__':
       main()

import prompt
name = prompt.string('May I have your name? ')
print('Hello, ' + name'!')
