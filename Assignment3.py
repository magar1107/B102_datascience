import random
import string
from datetime import datetime


"""
1. Data Types

1. Find the data type of every value in a mixed list.
"""


def find_types(items):
    result = []
    for item in items:
        result.append(type(item).__name__)
    return result


print(find_types([10, 3.5, "hello", True, [1, 2], (3, 4), {"a": 1}, None]))


"""
2. Convert a nested list into a tuple of tuples.
"""


def nested_to_tuple(nested):
    return tuple(tuple(inner) for inner in nested)


print(nested_to_tuple([[1, 2], [3, 4], [5, 6]]))


"""
3. Remove all duplicate values from a mixed list while preserving the original order.
"""


def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


print(remove_duplicates([1, "a", 2, "a", 1, 3.5, 3.5, "b"]))


"""
2. Operators

4. Check whether a number is a power of 2 using operators.
"""


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


print(is_power_of_two(16))
print(is_power_of_two(18))


"""
5. Swap two numbers using bitwise XOR.
"""


def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


print(swap_xor(5, 9))


"""
6. Find whether a number is divisible by both 4 and 6 using logical operators.
"""


def divisible_by_4_and_6(n):
    return n % 4 == 0 and n % 6 == 0


print(divisible_by_4_and_6(24))
print(divisible_by_4_and_6(8))


"""
7. Calculate the total electricity bill using different unit rates.
"""


def electricity_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    elif units <= 300:
        return 100 * 5 + 100 * 7 + (units - 200) * 10
    return 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12


print(electricity_bill(250))


"""
3. Conditional Statements

8. Check whether three sides can form a triangle.
"""


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


print(is_triangle(3, 4, 5))
print(is_triangle(1, 2, 5))


"""
9. Determine the type of triangle (Equilateral, Isosceles, Scalene).
"""


def triangle_type(a, b, c):
    if not is_triangle(a, b, c):
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"


print(triangle_type(5, 5, 5))
print(triangle_type(5, 5, 8))
print(triangle_type(3, 4, 5))


"""
10. Create a simple ATM menu (Withdraw, Deposit, Balance).
"""


def atm():
    balance = 5000
    while True:
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient balance")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Deposited:", amount)
        elif choice == "3":
            print("Balance:", balance)
        elif choice == "4":
            print("Thank you")
            break
        else:
            print("Invalid choice")


"""
11. Calculate income tax based on different tax slabs.
"""


def income_tax(income):
    if income <= 300000:
        return 0
    elif income <= 600000:
        return (income - 300000) * 0.05
    elif income <= 900000:
        return 300000 * 0.05 + (income - 600000) * 0.10
    elif income <= 1200000:
        return 300000 * 0.05 + 300000 * 0.10 + (income - 900000) * 0.15
    return 300000 * 0.05 + 300000 * 0.10 + 300000 * 0.15 + (income - 1200000) * 0.20


print(income_tax(750000))


"""
12. Create a menu-driven calculator using if-elif.
"""


def calculator():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")


"""
4. Loops

13. Print all prime numbers between 1 and n.
"""


def print_primes(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)


print_primes(30)


"""
14. Find the factorial of a number using a loop.
"""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(5))


"""
15. Print the Fibonacci series up to n terms.
"""


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


fibonacci(10)


"""
16. Check whether a number is an Armstrong number.
"""


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == n


print(is_armstrong(153))
print(is_armstrong(123))


"""
17. Reverse a number and check if it is a palindrome.
"""


def reverse_number(n):
    rev = 0
    original = n
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev, rev == original


print(reverse_number(121))
print(reverse_number(123))


"""
18. Find the Greatest Common Divisor (GCD) of two numbers.
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(48, 18))


"""
5. Functions

19. Write a function to check if a string is a palindrome.
"""


def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("madam"))
print(is_palindrome("hello"))


"""
20. Write a function to count vowels and consonants in a string.
"""


def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


print(count_vowels_consonants("Hello World"))


"""
21. Create a function to calculate simple and compound interest.
"""


def interest(principal, rate, time):
    simple = principal * rate * time / 100
    compound = principal * ((1 + rate / 100) ** time) - principal
    return simple, compound


print(interest(10000, 5, 3))


"""
22. Write a function to return all factors of a number.
"""


def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


print(factors(36))


"""
23. Write a function to find the second-largest number in a list.
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
6. Lists

24. Merge two lists without duplicates.
"""


def merge_lists(list1, list2):
    result = []
    for item in list1 + list2:
        if item not in result:
            result.append(item)
    return result


print(merge_lists([1, 2, 3, 4], [3, 4, 5, 6]))


"""
25. Find the second-largest and second-smallest elements.
"""


def second_largest_smallest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2], unique[1]


print(second_largest_smallest([5, 1, 9, 3, 7, 9, 1]))


"""
26. Rotate a list to the left by k positions.
"""


def rotate_left(numbers, k):
    k = k % len(numbers)
    return numbers[k:] + numbers[:k]


print(rotate_left([1, 2, 3, 4, 5], 2))


"""
27. Separate even and odd numbers into two lists.
"""


def separate_even_odd(numbers):
    evens = []
    odds = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens, odds


print(separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8]))


"""
28. Find the common elements between two lists.
"""


def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result


print(common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7]))


"""
7. Tuples & Sets

29. Count the frequency of each element in a tuple.
"""


def tuple_frequency(t):
    freq = {}
    for item in t:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


print(tuple_frequency((1, 2, 2, 3, 3, 3, 4)))


"""
30. Find the union, intersection, and difference of two sets.
"""


def set_operations(a, b):
    return a | b, a & b, a - b


print(set_operations({1, 2, 3, 4}, {3, 4, 5, 6}))


"""
31. Check whether one set is a subset of another.
"""


def is_subset(a, b):
    return a.issubset(b)


print(is_subset({1, 2}, {1, 2, 3, 4}))
print(is_subset({1, 5}, {1, 2, 3, 4}))


"""
8. Dictionaries

32. Count the frequency of words in a sentence.
"""


def word_frequency(sentence):
    freq = {}
    for word in sentence.lower().split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


print(word_frequency("the cat and the dog and the bird"))


"""
33. Create a dictionary from two lists (keys and values).
"""


def make_dict(keys, values):
    return dict(zip(keys, values))


print(make_dict(["name", "age", "city"], ["Ravi", 20, "Pune"]))


"""
34. Sort a dictionary by its values.
"""


def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))


print(sort_dict_by_value({"a": 3, "b": 1, "c": 2}))


"""
9. File Handling

35. Read a text file and count the number of lines, words, and characters.
"""


def count_file(filename):
    lines = 0
    words = 0
    chars = 0
    with open(filename, "r") as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
    return lines, words, chars


with open("sample.txt", "w") as f:
    f.write("Line one of the file\n")
    f.write("Line two is here\n")
    f.write("Line three\n")
    f.write("Line four ends the file\n")

print(count_file("sample.txt"))


"""
36. Copy only the even-numbered lines from one file to another.
"""


def copy_even_lines(source, destination):
    with open(source, "r") as src, open(destination, "w") as dest:
        line_number = 1
        for line in src:
            if line_number % 2 == 0:
                dest.write(line)
            line_number += 1


copy_even_lines("sample.txt", "even_lines.txt")

with open("even_lines.txt", "r") as f:
    print(f.read())


"""
10. Exception Handling

37. Handle invalid integer input using try-except.
"""


def get_integer():
    try:
        number = int(input("Enter an integer: "))
        print("You entered:", number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


"""
38. Handle file-not-found errors while reading a file.
"""


def read_file(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found:", filename)


read_file("missing_file.txt")


"""
11. Modules

39. Create a random password generator using the random and string modules.
"""


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password


print(generate_password(12))


"""
40. Use the datetime module to calculate the number of days between two dates.
"""


def days_between(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)


print(days_between("2026-01-01", "2026-11-16"))


atm()
calculator()
get_integer()
