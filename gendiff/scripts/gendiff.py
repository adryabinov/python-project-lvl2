#!/usr/bin/env python
from gendiff.parse_input import parse_input


def main():
    args = parse_input()
    print(args.first_file)


if __name__ == '__main__':
    main()
