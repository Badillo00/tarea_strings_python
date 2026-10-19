# ============================================================
# NUMBERS AND BOOLEANS ASSIGNMENT - PYTHON
# ============================================================
# Student: Emanuel Alejandro Badillo Hernandez
# Student ID: 2630419
# Group: 3
# File: 2630419_BadilloEmanuel.py
# ============================================================

# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
# The int type is used for whole numbers, while float is used for
# numbers that can contain decimal values.
# Boolean values are represented by True and False and are often
# produced by comparisons such as >, <, ==, >=, and <=.
# Numeric data validation is important because incorrect values
# can produce invalid calculations or runtime errors.
# It is also important to avoid division by zero and unreasonable
# numeric ranges before performing calculations.
# This program contains six problems involving arithmetic operations,
# comparisons, boolean logic, casting, rounding, and decision making.
# Each problem includes inputs, outputs, validations, and test cases.

# ------------------------------------------------------------
# PRINCIPLES AND GOOD PRACTICES
# ------------------------------------------------------------
# - Use int for counters and whole quantities.
# - Use float for quantities that may contain decimal values.
# - Store intermediate results in variables instead of repeating
#   complex expressions.
# - Validate data before performing calculations.
# - Use descriptive lower_snake_case variable names.
# - Use UPPER_SNAKE_CASE for constants.
# - Clearly document what True and False mean in each problem.
# - Avoid division by zero by checking denominators first.

ABSOLUTE_ZERO_C = -273.15
HIGH_TEMPERATURE_C = 30.0
REGULAR_HOURS_LIMIT = 40.0
OVERTIME_MULTIPLIER = 1.5
DISCOUNT_RATE = 0.10
DISCOUNT_PURCHASE_LIMIT = 1000.0
MIN_MONTHLY_INCOME = 8000.0
MAX_DEBT_RATIO = 0.40
MIN_CREDIT_SCORE = 650


# ============================================================
# Problem 1: Temperature converter and range flag
# ============================================================
# Description:
# This problem converts a temperature from Celsius to Fahrenheit
# and Kelvin. It also determines whether the Celsius temperature
# is considered high according to the 30.0 C threshold.
#
# Inputs:
# - temp_c: float representing temperature in Celsius.
#
# Outputs:
# - "Fahrenheit: <value>"
# - "Kelvin: <value>"
# - "High temperature: true|false"
#
# Validations:
# - temp_c must be convertible to float.
# - The temperature cannot be lower than absolute zero.
#
# Test cases:
# 1) Normal: 35
#    Expected: Fahrenheit 95.0, Kelvin 308.15, high = true
# 2) Border: 30
#    Expected: high = true
# 3) Error: -300
#    Expected: Error: invalid input

def problem_1_temperature_converter():
    print("\n--- Problem 1: Temperature converter ---")

    temp_text = input("Enter temperature in Celsius: ").strip()

    try:
        temp_c = float(temp_text)
    except ValueError:
        print("Error: invalid input")
        return

    if temp_c < ABSOLUTE_ZERO_C:
        print("Error: invalid input")
        return

    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    is_high_temperature = temp_c >= HIGH_TEMPERATURE_C

    print(f"Fahrenheit: {round(temp_f, 2)}")
    print(f"Kelvin: {round(temp_k, 2)}")
    print(f"High temperature: {str(is_high_temperature).lower()}")


# ============================================================
# Problem 2: Work hours and overtime payment
# ============================================================
# Description:
# This problem calculates weekly payment. Up to 40 hours are paid
# at the regular hourly rate. Hours above 40 are paid at 150%
# of the regular rate.
#
# Inputs:
# - hours_worked: float
# - hourly_rate: float
#
# Outputs:
# - "Regular pay: <value>"
# - "Overtime pay: <value>"
# - "Total pay: <value>"
# - "Has overtime: true|false"
#
# Validations:
# - hours_worked must be greater than or equal to 0.
# - hourly_rate must be greater than 0.
# - Both inputs must be valid numeric values.
#
# Test cases:
# 1) Normal: hours=45, rate=100
#    Expected: regular=4000, overtime=750, total=4750
# 2) Border: hours=40, rate=100
#    Expected: overtime=0, has overtime=false
# 3) Error: hours=-5, rate=100
#    Expected: Error: invalid input

def problem_2_overtime_payment():
    print("\n--- Problem 2: Work hours and overtime payment ---")

    try:
        hours_worked = float(input("Enter hours worked: ").strip())
        hourly_rate = float(input("Enter hourly rate: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
        return

    regular_hours = min(hours_worked, REGULAR_HOURS_LIMIT)
    overtime_hours = max(hours_worked - REGULAR_HOURS_LIMIT, 0.0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > REGULAR_HOURS_LIMIT

    print(f"Regular pay: {round(regular_pay, 2)}")
    print(f"Overtime pay: {round(overtime_pay, 2)}")
    print(f"Total pay: {round(total_pay, 2)}")
    print(f"Has overtime: {str(has_overtime).lower()}")


# ============================================================
# Problem 3: Discount eligibility with booleans
# ============================================================
# Description:
# This problem determines whether a customer receives a discount.
# A customer is eligible if they are a student, a senior, or the
# purchase total is at least 1000.0.
#
# Inputs:
# - purchase_total: float
# - is_student_text: "YES" or "NO"
# - is_senior_text: "YES" or "NO"
#
# Outputs:
# - "Discount eligible: true|false"
# - "Final total: <value>"
#
# Validations:
# - purchase_total must be greater than or equal to 0.
# - Student and senior answers must be YES or NO.
#
# Test cases:
# 1) Normal: total=1200, student=NO, senior=NO
#    Expected: eligible=true, final total=1080
# 2) Border: total=1000, student=NO, senior=NO
#    Expected: eligible=true
# 3) Error: total=500, student=MAYBE, senior=NO
#    Expected: Error: invalid input

def problem_3_discount_eligibility():
    print("\n--- Problem 3: Discount eligibility ---")

    try:
        purchase_total = float(input("Enter purchase total: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    if purchase_total < 0:
        print("Error: invalid input")
        return

    is_student_text = input("Are you a student? (YES/NO): ").strip().upper()
    is_senior_text = input("Are you a senior? (YES/NO): ").strip().upper()

    if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
        print("Error: invalid input")
        return

    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"

    discount_eligible = (
        is_student
        or is_senior
        or purchase_total >= DISCOUNT_PURCHASE_LIMIT
    )

    if discount_eligible:
        final_total = purchase_total * (1 - DISCOUNT_RATE)
    else:
        final_total = purchase_total

    print(f"Discount eligible: {str(discount_eligible).lower()}")
    print(f"Final total: {round(final_total, 2)}")


# ============================================================
# Problem 4: Basic statistics of three integers
# ============================================================
# Description:
# This problem reads three integers and calculates their sum,
# average, maximum, and minimum. It also checks whether all three
# integers are even.
#
# Inputs:
# - n1: int
# - n2: int
# - n3: int
#
# Outputs:
# - "Sum: <value>"
# - "Average: <value>"
# - "Max: <value>"
# - "Min: <value>"
# - "All even: true|false"
#
# Validations:
# - All three inputs must be convertible to int.
# - Negative integers are allowed.
#
# Test cases:
# 1) Normal: 4, 8, 12
#    Expected: sum=24, average=8, all even=true
# 2) Border: 0, 0, 0
#    Expected: sum=0, average=0, all even=true
# 3) Error: 5, "hello", 10
#    Expected: Error: invalid input

def problem_4_integer_statistics():
    print("\n--- Problem 4: Basic statistics ---")

    try:
        n1 = int(input("Enter first integer: ").strip())
        n2 = int(input("Enter second integer: ").strip())
        n3 = int(input("Enter third integer: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (
        n1 % 2 == 0
        and n2 % 2 == 0
        and n3 % 2 == 0
    )

    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")


# ============================================================
# Problem 5: Loan eligibility
# ============================================================
# Description:
# This problem calculates the monthly debt ratio and determines
# whether a person meets the defined loan eligibility conditions.
#
# Inputs:
# - monthly_income: float
# - monthly_debt: float
# - credit_score: int
#
# Outputs:
# - "Debt ratio: <value>"
# - "Eligible: true|false"
#
# Validations:
# - monthly_income must be greater than 0 to avoid division by zero.
# - monthly_debt must be greater than or equal to 0.
# - credit_score must be greater than or equal to 0.
#
# Test cases:
# 1) Normal: income=12000, debt=3000, score=700
#    Expected: ratio=0.25, eligible=true
# 2) Border: income=8000, debt=3200, score=650
#    Expected: ratio=0.40, eligible=true
# 3) Error: income=0, debt=1000, score=700
#    Expected: Error: invalid input

def problem_5_loan_eligibility():
    print("\n--- Problem 5: Loan eligibility ---")

    try:
        monthly_income = float(input("Enter monthly income: ").strip())
        monthly_debt = float(input("Enter monthly debt: ").strip())
        credit_score = int(input("Enter credit score: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
        return

    debt_ratio = monthly_debt / monthly_income

    eligible = (
        monthly_income >= MIN_MONTHLY_INCOME
        and debt_ratio <= MAX_DEBT_RATIO
        and credit_score >= MIN_CREDIT_SCORE
    )

    print(f"Debt ratio: {round(debt_ratio, 2)}")
    print(f"Eligible: {str(eligible).lower()}")


# ============================================================
# Problem 6: Body Mass Index (BMI) and category flags
# ============================================================
# Description:
# This problem calculates BMI using weight and height values.
# It then evaluates three boolean flags according to the ranges
# required by the assignment.
#
# Inputs:
# - weight_kg: float
# - height_m: float
#
# Outputs:
# - "BMI: <value>"
# - "Underweight: true|false"
# - "Normal: true|false"
# - "Overweight: true|false"
#
# Validations:
# - weight_kg must be greater than 0.
# - height_m must be greater than 0.
#
# Test cases:
# 1) Normal: weight=68, height=1.70
#    Expected: BMI about 23.53, normal=true
# 2) Border: weight=72.25, height=1.70
#    Expected: BMI=25.0, overweight=true
# 3) Error: weight=70, height=0
#    Expected: Error: invalid input

def problem_6_bmi():
    print("\n--- Problem 6: BMI and category flags ---")

    try:
        weight_kg = float(input("Enter weight in kilograms: ").strip())
        height_m = float(input("Enter height in meters: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
        return

    bmi = weight_kg / (height_m * height_m)

    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 25.0
    is_overweight = bmi >= 25.0

    print(f"BMI: {round(bmi, 2)}")
    print(f"Underweight: {str(is_underweight).lower()}")
    print(f"Normal: {str(is_normal).lower()}")
    print(f"Overweight: {str(is_overweight).lower()}")


# ============================================================
# MAIN PROGRAM
# ============================================================
# The six problems are executed in order.
# Invalid input in one problem does not stop the other problems.

def main():
    print("========================================")
    print("NUMBERS AND BOOLEANS ASSIGNMENT")
    print("========================================")

    problem_1_temperature_converter()
    problem_2_overtime_payment()
    problem_3_discount_eligibility()
    problem_4_integer_statistics()
    problem_5_loan_eligibility()
    problem_6_bmi()

    print("\n========================================")
    print("Program finished")
    print("========================================")


if __name__ == "__main__":
    main()


# ------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------
# Integers and floating-point values can be used together to solve
# real-world calculation problems.
# Comparisons produce boolean values that allow programs to make
# decisions using if statements and logical expressions.
# Input validation is essential because invalid ranges can produce
# incorrect results or errors such as division by zero.
# The operators and, or, and not make it possible to combine several
# requirements into a single logical condition.
# Intermediate variables make formulas easier to understand and test.
# These patterns are useful in payroll, discounts, statistics,
# financial evaluations, and many other programming problems.

# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python Software Foundation. Numeric Types - int, float, complex.
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
#
# 2) Python Software Foundation. Boolean Operations.
#    https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
#
# 3) Python Software Foundation. Built-in Functions.
#    https://docs.python.org/3/library/functions.html
#
# 4) Python Software Foundation. Python Tutorial - Numbers.
#    https://docs.python.org/3/tutorial/introduction.html#numbers
#
# 5) Matthes, Eric. Python Crash Course, 3rd Edition.
#    No Starch Press, 2023.
#
# 6) Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition.
#    No Starch Press, 2019.

# ------------------------------------------------------------
# GITHUB REPOSITORY
# ------------------------------------------------------------
# Repository URL:
# https://github.com/Badillo00/tarea_strings_python
#
# The assignment instructions allow using the same repository
# that was already being used.
#
# ------------------------------------------------------------
# DELIVERY CHECKLIST
# ------------------------------------------------------------
# [x] File uses the required student ID and name.
# [x] Cover, executive summary, problems 1-6, conclusions, references.
# [x] Each problem contains description, inputs, outputs, validations,
#     and normal, border, and error test cases.
# [x] Variables, constants, and screen messages are in English.
# [x] Numeric types int and float are used where appropriate.
# [x] Boolean conditions and logical operators are included.
# [x] Input validation and division-by-zero protection are included.
# [x] GitHub repository URL is included.
