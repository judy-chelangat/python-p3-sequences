#!/usr/bin/env python3

def print_fibonacci(length):
    fib_numbers=[0,1]
    for i in range(2,length):
       fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
       print(fib_numbers)

    pass