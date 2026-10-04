#!/usr/bin/python3
# this is a cli calculator
# it performs basic addition, subtraction, multiplication and division
# has verbose and debug modes
# every thing is done in the command lines

import argparse
import sys



USAGE = """
    acalc is a command line calculator

    function: uses arguments to perform calculations

"""

def add(x: float, y: float, is_verbose: bool) -> float:
    if is_verbose:
        print(f"{x} + {y} = {x + y}")
    return x + y
    

def subtract(x: float, y: float, is_verbose: bool) -> float:
    if is_verbose:
        print(f"{x} + {y} = {x + y}")
    return x - y

def divide(x: float, y: float, is_verbose: bool) -> float:
    try:
        answer = x / y
        if is_verbose:
                print(f"{x} + {y} = {answer}")
        return answer
    except ZeroDivisionError:
        print(f"{"\33[32m"}Division by zero is undefined")
        sys.exit(1)
 
def multiply(x: float, y: float, is_verbose: bool) -> float:
    if is_verbose:
        print(f"{x} + {y} = {x * y}")
    return x * y

def process_args():
    parser = argparse.ArgumentParser(usage=USAGE)

    # grouping arithmetic
    math_group = parser.add_argument_group("math operations")
    math_group.add_argument("-a", "--add", nargs=2 , type=float , help="Add two numbers")
    math_group.add_argument("-s", "--subtract", nargs=2 , type=float , help="subtract two numbers")
    math_group.add_argument("-d", "--divide", nargs=2 , type=float , help="divide two numbers")
    math_group.add_argument("-m", "--multiply",  nargs=2 , type=float , help="multiply two numbers")

    # special functions
    special_group = parser.add_argument_group("special operations")
    special_group.add_argument("--verbose",action='store_true', help="show operation details")

    return parser.parse_args()

def process_args2():
    # making the process mutually exclusive 
    parser = argparse.ArgumentParser(usage=USAGE)

    
    # grouping arithmetic
    math_group = parser.add_argument_group("math operations")
    exclusive = math_group.add_mutually_exclusive_group(required=True)

    exclusive.add_argument("-a", "--add", nargs=2 , type=float , help="Add two numbers")
    exclusive.add_argument("-s", "--subtract", nargs=2 , type=float , help="Add two numbers")
    exclusive.add_argument("-d", "--divide", nargs=2 , type=float , help="Add two numbers")
    exclusive.add_argument("-m", "--multiply",  nargs=2 , type=float , help="Add two numbers")

    # special functions
    special_group = parser.add_argument_group("special operations")
    special_group.add_argument("--verbose",action='store_true', help="show operation details")

    return parser.parse_args()


def main():
    args = process_args2()
    result = 0

    if args.add:
        x, y = args.add
        result = add(x, y, args.verbose)

    if args.subtract:
        x, y = args.subtract
        result = subtract(x, y, args.verbose)

    if args.divide:
        x, y = args.substract
        result = divide(x, y, args.verbose)

    if args.multiply:
        x, y = args.substract
        result = multiply(x, y, args.verbose)

    print(f"final result = {result}")

    return 0

if __name__ == "__main__":
    sys.exit(main())