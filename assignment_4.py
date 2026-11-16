"""
1. Write a Python program to check whether a number is even or odd.
"""


def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


print(even_or_odd(10))
print(even_or_odd(7))


"""
2. Write a program to find the largest of three numbers.
"""


def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c


print(largest_of_three(12, 45, 30))


"""
3. Write a program to check whether a given number is prime.
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(17))
print(is_prime(20))


"""
4. Write a program to print the Fibonacci series up to n terms.
"""


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


fibonacci(10)


"""
5. Write a program to find the factorial of a number using a loop.
"""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(5))


"""
6. Write a program to reverse a string without using [::-1].
"""


def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result


print(reverse_string("python"))


"""
7. Write a program to check whether a string is a palindrome.
"""


def is_palindrome(s):
    return s == reverse_string(s)


print(is_palindrome("madam"))
print(is_palindrome("hello"))


"""
8. Write a program to count the number of vowels and consonants in a string.
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
9. Write a program to find the sum of all elements in a list.
"""


def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_list([10, 20, 30, 40]))


"""
10. Write a program to find the largest and smallest element in a list without using max() or min().
"""


def largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest


print(largest_smallest([8, 3, 15, 1, 9]))


"""
11. Write a program to remove duplicate elements from a list.
"""


def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


"""
12. Write a program to count how many times each element appears in a list using a dictionary.
"""


def count_elements(items):
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


print(count_elements([1, 2, 2, 3, 3, 3, 4]))


"""
13. Write a program to find the second-largest number in a list.
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
14. Write a program to sort a list without using sort() or sorted().
"""


def sort_list(numbers):
    items = numbers[:]
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


print(sort_list([5, 2, 9, 1, 7]))


"""
15. Write a function that accepts a list of numbers and returns a list containing only the even numbers.
"""


def get_even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))


"""
16. Write a program to find the frequency of each character in a string.
"""


def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


print(char_frequency("banana"))


"""
17. Write a program to check whether two strings are anagrams of each other.
"""


def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return char_frequency(s1) == char_frequency(s2)


print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))


"""
18. Write a program to find all duplicate values in a list.
"""


def find_duplicates(items):
    freq = count_elements(items)
    duplicates = []
    for key in freq:
        if freq[key] > 1:
            duplicates.append(key)
    return duplicates


print(find_duplicates([1, 2, 2, 3, 4, 4, 5, 5, 5]))


"""
19. Write a program that takes a sentence and finds the longest word.
"""


def longest_word(sentence):
    longest = ""
    for word in sentence.split():
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("Python is a very powerful programming language"))


"""
20. Create a simple student marks program that:
   1. accepts marks for 5 subjects,
   2. calculates the total and percentage,
   3. assigns a grade, and displays whether the student passed or failed.
"""


def student_marks():
    marks = []
    for i in range(1, 6):
        m = float(input("Enter marks for subject " + str(i) + ": "))
        marks.append(m)

    total = sum_list(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    passed = True
    for m in marks:
        if m < 35:
            passed = False

    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    if passed:
        print("Result: Pass")
    else:
        print("Result: Fail")


student_marks()
