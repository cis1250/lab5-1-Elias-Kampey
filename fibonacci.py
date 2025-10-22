#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_user_input():
  num = input("Enter a number of Fibonacci terms: ")

  while not num.isdigit() or int(num) <= 0:
        print("Please enter a positive integer.")
        num = input("Enter the number of Fibonacci terms: ")

  return int(num)

def generate_fibonacci(n):
    sequence = []
    a = 0
    b = 1
    count = 0

    while count < n:
        sequence.append(a)
        next_num = a + b
        a = b
        b = next_num
        count += 1

    return sequence

def print_sequence(sequence):
    print("Fibonacci Sequence:")
    print(", ".join(str(num) for num in sequence))

def main():
    n = get_user_input()
    sequence = generate_fibonacci(n)
    print_sequence(sequence)

if __name__ == "__main__":
    main()
