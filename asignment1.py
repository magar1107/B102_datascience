# Question 1
# Question: Check if a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")


# Question 2
# Question: Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# Question 3
# Question: Find the greater of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")


# Question 4
# Question: Find the greatest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is the greatest")
elif b >= a and b >= c:
    print(b, "is the greatest")
else:
    print(c, "is the greatest")


# Question 5
# Question: Check if a person is eligible to vote (age >= 18).

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Question 6
# Question: Check whether a year is a leap year.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# Question 7
# Question: Check if a character is a vowel or consonant.

ch = input("Enter a character: ")
ch = ch.lower()

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("It is a Vowel")
elif ch >= 'a' and ch <= 'z':
    print("It is a Consonant")
else:
    print("It is not an alphabet")


# Question 8
# Question: Check whether a number is divisible by 5 and 11.

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print(num, "is divisible by both 5 and 11")
else:
    print(num, "is not divisible by both 5 and 11")


# Question 9
# Question: Check if a number is a multiple of both 3 and 7.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print(num, "is a multiple of both 3 and 7")
else:
    print(num, "is not a multiple of both 3 and 7")


# Question 10
# Question: Assign grades based on marks:
#   90-100: A | 80-89: B | 70-79: C | 60-69: D | Below 60: F

marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Question 11
# Question: Check if a character is uppercase or lowercase.

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("It is an Uppercase letter")
elif ch >= 'a' and ch <= 'z':
    print("It is a Lowercase letter")
else:
    print("It is not an alphabet")


# Question 12
# Question: Find whether the entered alphabet is a vowel using if-elif.

ch = input("Enter an alphabet: ")
ch = ch.lower()

if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
else:
    print("Not a vowel")


# Question 13
# Question: Check if three sides can form a triangle.

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")


# Question 14
# Question: Determine the type of triangle (Equilateral, Isosceles, Scalene).

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")


# Question 15
# Question: Find the largest among four numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print(a, "is the largest")
elif b >= a and b >= c and b >= d:
    print(b, "is the largest")
elif c >= a and c >= b and c >= d:
    print(c, "is the largest")
else:
    print(d, "is the largest")


# Question 16
# Question: Check whether a number is a three-digit number.

num = int(input("Enter a number: "))

if num < 0:
    num = -num

if num >= 100 and num <= 999:
    print("It is a three-digit number")
else:
    print("It is not a three-digit number")


# Question 17
# Question: Calculate electricity bill using slab rates.

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity bill = Rs", bill)


# Question 18
# Question: Calculate income tax based on income slabs.

income = float(input("Enter yearly income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20
else:
    tax = 112500 + (income - 1000000) * 0.30

print("Income tax = Rs", tax)


# Question 19
# Question: Check if a student passes (minimum 35 marks in each subject).

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Student has Passed")
else:
    print("Student has Failed")


# Question 20
# Question: Find whether a number is within a given range.

num = int(input("Enter a number: "))
low = int(input("Enter lower limit of range: "))
high = int(input("Enter upper limit of range: "))

if num >= low and num <= high:
    print(num, "is within the range", low, "to", high)
else:
    print(num, "is not within the range", low, "to", high)


# Question 21
# Question: Build a simple calculator using if-elif-else (+, -, *, /).

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result =", a + b)
elif op == '-':
    print("Result =", a - b)
elif op == '*':
    print("Result =", a * b)
elif op == '/':
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# Question 22
# Question: Check if a year is a century leap year.

year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print(year, "is a Century Leap Year")
    else:
        print(year, "is a Century year but NOT a Leap Year")
else:
    print(year, "is not a Century year")


# Question 23
# Question: Determine the season based on the month number.

month = int(input("Enter month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Season: Winter")
elif month >= 3 and month <= 5:
    print("Season: Summer")
elif month >= 6 and month <= 9:
    print("Season: Monsoon")
elif month == 10 or month == 11:
    print("Season: Autumn")
else:
    print("Invalid month number")


# Question 24
# Question: Find the number of days in a month.

month = int(input("Enter month number (1-12): "))
year = int(input("Enter year (needed for February): "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Number of days = 31")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("Number of days = 30")
elif month == 2:

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Number of days = 29")
    else:
        print("Number of days = 28")
else:
    print("Invalid month number")


# Question 25
# Question: Check whether a password meets minimum conditions (length, digits, etc.).

password = input("Enter password: ")

has_digit = False
has_upper = False
has_lower = False

for ch in password:
    if ch >= '0' and ch <= '9':
        has_digit = True
    elif ch >= 'A' and ch <= 'Z':
        has_upper = True
    elif ch >= 'a' and ch <= 'z':
        has_lower = True

if len(password) < 8:
    print("Weak password: must be at least 8 characters")
elif has_digit == False:
    print("Weak password: must contain at least one digit")
elif has_upper == False:
    print("Weak password: must contain at least one uppercase letter")
elif has_lower == False:
    print("Weak password: must contain at least one lowercase letter")
else:
    print("Strong password: all conditions satisfied")


# Question 26
# Question: Determine ticket price based on age category.

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price = Free")
elif age <= 12:
    print("Ticket price = Rs 100")
elif age <= 59:
    print("Ticket price = Rs 200")
else:
    print("Ticket price = Rs 120")


# Question 27
# Question: Calculate discount based on purchase amount.

amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount_percent = 20
elif amount >= 3000:
    discount_percent = 10
elif amount >= 1000:
    discount_percent = 5
else:
    discount_percent = 0

discount = amount * discount_percent / 100
final_amount = amount - discount

print("Discount percent =", discount_percent, "%")
print("Discount amount = Rs", discount)
print("Final amount to pay = Rs", final_amount)


# Question 28
# Question: Check if a person is eligible for a driving license (age and eyesight condition).

age = int(input("Enter your age: "))
eyesight = input("Is your eyesight good? (yes/no): ")
eyesight = eyesight.lower()

if age >= 18 and eyesight == "yes":
    print("You are eligible for a driving license")
elif age < 18:
    print("Not eligible: age must be 18 or above")
else:
    print("Not eligible: eyesight condition is not satisfied")


# Question 29
# Question: Create a login system with username and password validation.

correct_username = "admin"
correct_password = "admin123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful. Welcome,", username)
elif username != correct_username:
    print("Login failed: wrong username")
else:
    print("Login failed: wrong password")


# Question 30
# Question: Create a menu-driven program using if-elif-else with options like:
#   1. Addition  2. Subtraction  3. Multiplication  4. Division  5. Exit

print("----- MENU -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice (1-5): "))

if choice == 5:
    print("Thank you! Exiting the program.")
elif choice >= 1 and choice <= 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Sum =", a + b)
    elif choice == 2:
        print("Difference =", a - b)
    elif choice == 3:
        print("Product =", a * b)
    else:
        if b != 0:
            print("Quotient =", a / b)
        else:
            print("Cannot divide by zero")
else:
    print("Invalid choice. Please enter 1 to 5.")
