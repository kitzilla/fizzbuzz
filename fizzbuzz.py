#!/usr/bin/env python3

# Written by Go Sato for Netacea application


def fizz_buzz(n: int) -> str:
    output = ""
    if n % 3 == 0:
        output += "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    return output or str(n)


if __name__ == "__main__":
    for i in range(1, 101):
        print(fizz_buzz(i))
