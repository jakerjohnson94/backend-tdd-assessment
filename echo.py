#!/usr/bin/env python2
# -*- coding: utf-8 -*-
__author__ = 'Jake Johnson'
import argparse

# usage: echo.py [-h] [-u] [-l] [-t] text

# Perform transformation on input text.

# positional arguments:
#     text         text to be manipulated

# optional arguments:
#     -h, --help   show this help message and exit
#     -u, --upper  convert text to uppercase
#     -l, --lower  convert text to lowercase
#     -t, --title  convert text to titlecase


def create_parser():
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    return parser


def main():
    args = create_parser().parse_args()
    text = args.text
    if args.upper and args.lower and args.title:
        text = text.upper().lower().capitalize()
    elif args.upper:
        text = text.upper()
    elif args.lower:
        text = text.lower()
    elif args.title:
        text = text.capitalize()
    elif not args.upper and not args.lower and not args.title:
        text = args.text
    return text


if __name__ == '__main__':
    print(main())
