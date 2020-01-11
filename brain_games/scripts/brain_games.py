#!/usr/bin/env python3
from brain_games.cli import run


def greeting():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    print('')


def main():
    greeting()
    run()


if __name__ == '__main__':
    main()
