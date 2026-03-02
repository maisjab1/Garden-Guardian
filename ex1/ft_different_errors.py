#!/usr/bin/env python3

def garden_operations() -> None:
    try:
        print("\nTesting ValueError...")
        a, b, c = [1, 2]
        print(a, b, c)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        print("\nTesting ZeroDivisionError...")
        print(10 / 0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("\nTesting FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        print("\nTesting KeyError...")
        plants = {"name": "apple", "color": "red"}
        print(plants["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    try:
        print("\nTesting multiple errors together...")
        open("missing.txt")
        print(10 / 0)
    except (FileNotFoundError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
