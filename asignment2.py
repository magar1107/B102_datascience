import random


"""
Even or Odd Function
Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".
"""


def is_even(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


print(is_even(4))
print(is_even(7))


"""
Largest of Two Numbers
Write a function largest(a, b) that returns the larger number.
"""


def largest(a, b):
    if a > b:
        return a
    return b


print(largest(10, 25))


"""
Print Numbers
Write a function print_numbers(n) that prints numbers from 1 to n using a loop.
"""


def print_numbers(n):
    for i in range(1, n + 1):
        print(i)


print_numbers(5)


"""
Sum of Numbers
Write a function sum_n(n) that returns the sum of numbers from 1 to n.
"""


def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_n(10))


"""
Multiplication Table
Write a function table(n) that prints the multiplication table of n from 1 to 10.
"""


def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


table(5)


"""
Count Even Numbers
Write a function that takes a list and returns how many even numbers it contains.
Example:
count_even([1, 2, 3, 4, 6])
Output: 3
"""


def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


print(count_even([1, 2, 3, 4, 6]))


"""
Find Maximum
Without using max(), write a function that returns the largest number in a list.
"""


def find_max(numbers):
    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest


print(find_max([3, 9, 2, 15, 7]))


"""
FizzBuzz
Write a function that prints numbers from 1 to 100.
If divisible by 3, print "Fizz".
If divisible by 5, print "Buzz".
If divisible by both, print "FizzBuzz".
"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz()


"""
Palindrome Checker
Write a function that returns True if a string is a palindrome.
"""


def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("madam"))
print(is_palindrome("hello"))


"""
Count Vowels
Write a function that counts the vowels in a string.
"""


def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count


print(count_vowels("Hello World"))


"""
Second Largest Number
Write a function that returns the second largest number in a list without using sort().
"""


def second_largest(numbers):
    first = None
    second = None
    for num in numbers:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
    return second


print(second_largest([4, 8, 1, 9, 6]))


"""
Write a function grade(marks) that:
Returns "A" for marks >= 90
Returns "B" for marks >= 80
Returns "C" for marks >= 70
Returns "D" for marks >= 60
Otherwise returns "F"
"""


def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    return "F"


print(grade(95))
print(grade(72))
print(grade(40))


"""
Guessing Game
Generate a random number between 1 and 10.
Keep asking the user to guess until they get it right.
Use a loop, conditionals, and functions.
"""


def guessing_game():
    secret = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == secret:
            print("Correct!")
            break
        elif guess < secret:
            print("Too low, try again.")
        else:
            print("Too high, try again.")


guessing_game()
