# ============================================================
# LISTS AND TUPLES ASSIGNMENT - PYTHON
# ============================================================
# Student: Emanuel Alejandro Badillo Hernandez
# Student ID: 2630419
# Group: 3
# File: 2630419_BadilloEmanuel_listas_tuplas.py
# ============================================================

# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
# Lists and tuples are Python collections used to store multiple values.
# A list is ordered and mutable, which means its elements can be changed.
# A tuple is ordered and immutable, which means its elements cannot
# be modified after the tuple is created.
# Lists are useful when data must be added, removed, sorted, or updated.
# Tuples are useful for fixed data such as coordinates or measurements.
# This program contains six problems that use lists and tuples in
# practical situations such as shopping items, points, grades, and words.
# Each problem includes inputs, outputs, validations, and test cases.

# ------------------------------------------------------------
# PRINCIPLES AND GOOD PRACTICES
# ------------------------------------------------------------
# - Use lists when elements need to be added, removed, or changed.
# - Use tuples when the stored values should remain fixed.
# - Validate inputs before adding them to a collection.
# - Avoid changing a list while iterating over it unless necessary.
# - Verify indexes before accessing a list or tuple position.
# - Check that a list is not empty before using min(), max(), or average.
# - Use clear variable names and understandable output messages.
# - Use built-in functions such as len(), sum(), min(), max(), and sorted().


# ============================================================
# Problem 1: Shopping list basics
# ============================================================
# Description:
# This problem creates a shopping list from comma-separated text.
# It adds a new item, shows the total number of items, and checks
# whether a specific item is present in the list.
#
# Inputs:
# - initial_items_text: comma-separated string.
# - new_item: string to add.
# - search_item: string to search.
#
# Outputs:
# - "Items list: <list>"
# - "Total items: <number>"
# - "Found item: true|false"
#
# Validations:
# - initial_items_text must not be empty after strip().
# - new_item must not be empty.
# - search_item must not be empty.
#
# Test cases:
# 1) Normal: "apple,banana,orange", new="milk", search="banana"
#    Expected: found=true
# 2) Border: "apple", new="bread", search="apple"
#    Expected: two items, found=true
# 3) Error: initial list="   "
#    Expected: Error: invalid input

def problem_1_shopping_list():
    print("\n--- Problem 1: Shopping list basics ---")

    initial_items_text = input("Enter initial items separated by commas: ").strip()

    if not initial_items_text:
        print("Error: invalid input")
        return

    raw_items = initial_items_text.split(",")
    items_list = []

    for item in raw_items:
        clean_item = item.strip().lower()
        if clean_item:
            items_list.append(clean_item)

    if not items_list:
        print("Error: invalid input")
        return

    new_item = input("Enter new item: ").strip().lower()
    search_item = input("Enter item to search: ").strip().lower()

    if not new_item or not search_item:
        print("Error: invalid input")
        return

    items_list.append(new_item)
    is_in_list = search_item in items_list

    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {str(is_in_list).lower()}")


# ============================================================
# Problem 2: Points and distances with tuples
# ============================================================
# Description:
# This problem uses two tuples to represent points in a 2D plane.
# It calculates the Euclidean distance between the points and creates
# another tuple containing the midpoint.
#
# Inputs:
# - x1, y1, x2, y2: float values.
#
# Outputs:
# - "Point A: <tuple>"
# - "Point B: <tuple>"
# - "Distance: <value>"
# - "Midpoint: <tuple>"
#
# Validations:
# - All four values must be convertible to float.
#
# Test cases:
# 1) Normal: (0,0) and (3,4)
#    Expected: distance=5.0, midpoint=(1.5,2.0)
# 2) Border: (2,2) and (2,2)
#    Expected: distance=0.0
# 3) Error: x1="hello"
#    Expected: Error: invalid input

def problem_2_points_and_distance():
    print("\n--- Problem 2: Points and distances ---")

    try:
        x1 = float(input("Enter x1: ").strip())
        y1 = float(input("Enter y1: ").strip())
        x2 = float(input("Enter x2: ").strip())
        y2 = float(input("Enter y2: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, 2)}")
    print(f"Midpoint: {midpoint}")


# ============================================================
# Problem 3: Number list statistics
# ============================================================
# Description:
# This problem reads several numbers separated by commas and stores
# them in a list. It calculates the sum, average, minimum, maximum,
# and displays the sorted list.
#
# Inputs:
# - numbers_text: comma-separated numeric values.
#
# Outputs:
# - "Numbers: <list>"
# - "Sum: <value>"
# - "Average: <value>"
# - "Minimum: <value>"
# - "Maximum: <value>"
# - "Sorted numbers: <list>"
#
# Validations:
# - Input must not be empty.
# - Every element must be convertible to float.
# - The resulting list must contain at least one number.
#
# Test cases:
# 1) Normal: "10,20,30"
#    Expected: sum=60, average=20
# 2) Border: "5"
#    Expected: min=max=5
# 3) Error: "10,abc,20"
#    Expected: Error: invalid input

def problem_3_number_statistics():
    print("\n--- Problem 3: Number list statistics ---")

    numbers_text = input("Enter numbers separated by commas: ").strip()

    if not numbers_text:
        print("Error: invalid input")
        return

    number_parts = numbers_text.split(",")
    numbers_list = []

    try:
        for part in number_parts:
            clean_part = part.strip()

            if not clean_part:
                print("Error: invalid input")
                return

            numbers_list.append(float(clean_part))
    except ValueError:
        print("Error: invalid input")
        return

    if not numbers_list:
        print("Error: invalid input")
        return

    sum_value = sum(numbers_list)
    average_value = sum_value / len(numbers_list)
    minimum_value = min(numbers_list)
    maximum_value = max(numbers_list)
    sorted_numbers = sorted(numbers_list)

    print(f"Numbers: {numbers_list}")
    print(f"Sum: {round(sum_value, 2)}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Minimum: {minimum_value}")
    print(f"Maximum: {maximum_value}")
    print(f"Sorted numbers: {sorted_numbers}")


# ============================================================
# Problem 4: Student grades with a list
# ============================================================
# Description:
# This problem stores a student's grades in a list and calculates
# the average. It also determines whether the student passed using
# an average of 70.0 or higher.
#
# Inputs:
# - student_name: string.
# - grades_text: comma-separated grades.
#
# Outputs:
# - "Student: <name>"
# - "Grades: <list>"
# - "Average: <value>"
# - "Passed: true|false"
#
# Validations:
# - student_name must not be empty.
# - grades_text must not be empty.
# - Each grade must be numeric and between 0 and 100.
#
# Test cases:
# 1) Normal: name="Alex", grades="80,90,70"
#    Expected: average=80, passed=true
# 2) Border: grades="70"
#    Expected: average=70, passed=true
# 3) Error: grades="90,105,80"
#    Expected: Error: invalid input

def problem_4_student_grades():
    print("\n--- Problem 4: Student grades ---")

    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Error: invalid input")
        return

    grades_text = input("Enter grades separated by commas: ").strip()

    if not grades_text:
        print("Error: invalid input")
        return

    grades_list = []

    try:
        for grade_text in grades_text.split(","):
            clean_grade = grade_text.strip()

            if not clean_grade:
                print("Error: invalid input")
                return

            grade = float(clean_grade)

            if grade < 0 or grade > 100:
                print("Error: invalid input")
                return

            grades_list.append(grade)
    except ValueError:
        print("Error: invalid input")
        return

    if not grades_list:
        print("Error: invalid input")
        return

    average = sum(grades_list) / len(grades_list)
    is_passed = average >= 70.0

    print(f"Student: {student_name.title()}")
    print(f"Grades: {grades_list}")
    print(f"Average: {round(average, 2)}")
    print(f"Passed: {str(is_passed).lower()}")


# ============================================================
# Problem 5: Word list analysis
# ============================================================
# Description:
# This problem reads a sentence, converts it to lowercase, removes
# simple punctuation, and stores its words in a list.
# It then reports total words, unique words, longest word, and
# how many times a searched word appears.
#
# Inputs:
# - sentence: string.
# - search_word: string.
#
# Outputs:
# - "Words list: <list>"
# - "Total words: <number>"
# - "Unique words: <list>"
# - "Longest word: <word>"
# - "Occurrences: <number>"
#
# Validations:
# - sentence must not be empty.
# - search_word must not be empty.
# - words list must contain at least one word.
#
# Test cases:
# 1) Normal: "python is easy and python is useful", search="python"
#    Expected: occurrences=2
# 2) Border: "hello", search="hello"
#    Expected: one word, occurrences=1
# 3) Error: sentence="   "
#    Expected: Error: invalid input

def problem_5_word_list_analysis():
    print("\n--- Problem 5: Word list analysis ---")

    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    normalized_sentence = sentence.lower()

    punctuation_marks = [".", ",", ";", ":", "!", "?"]

    for mark in punctuation_marks:
        normalized_sentence = normalized_sentence.replace(mark, "")

    words_list = normalized_sentence.split()

    if not words_list:
        print("Error: invalid input")
        return

    search_word = input("Enter word to search: ").strip().lower()

    if not search_word:
        print("Error: invalid input")
        return

    unique_words = []

    for word in words_list:
        if word not in unique_words:
            unique_words.append(word)

    longest_word = words_list[0]

    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word

    occurrences = words_list.count(search_word)

    print(f"Words list: {words_list}")
    print(f"Total words: {len(words_list)}")
    print(f"Unique words: {unique_words}")
    print(f"Longest word: {longest_word}")
    print(f"Occurrences: {occurrences}")


# ============================================================
# Problem 6: Fixed student record with a tuple
# ============================================================
# Description:
# This problem creates a tuple containing fixed information about
# a student: name, age, and final grade. It then accesses each
# element by index and determines whether the final grade is passing.
#
# Inputs:
# - student_name: string.
# - student_age: int.
# - final_grade: float.
#
# Outputs:
# - "Record: <tuple>"
# - "Name: <value>"
# - "Age: <value>"
# - "Final grade: <value>"
# - "Passed: true|false"
#
# Validations:
# - student_name must not be empty.
# - student_age must be greater than 0.
# - final_grade must be between 0 and 100.
#
# Test cases:
# 1) Normal: "Maria", 18, 85
#    Expected: passed=true
# 2) Border: "Luis", 18, 70
#    Expected: passed=true
# 3) Error: "Ana", -1, 90
#    Expected: Error: invalid input

def problem_6_student_tuple_record():
    print("\n--- Problem 6: Student tuple record ---")

    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Error: invalid input")
        return

    try:
        student_age = int(input("Enter student age: ").strip())
        final_grade = float(input("Enter final grade: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    if student_age <= 0 or final_grade < 0 or final_grade > 100:
        print("Error: invalid input")
        return

    student_record = (student_name.title(), student_age, final_grade)
    is_passed = student_record[2] >= 70.0

    print(f"Record: {student_record}")
    print(f"Name: {student_record[0]}")
    print(f"Age: {student_record[1]}")
    print(f"Final grade: {student_record[2]}")
    print(f"Passed: {str(is_passed).lower()}")


# ============================================================
# MAIN PROGRAM
# ============================================================
# The six problems run in order.
# If one problem receives invalid input, the program continues
# with the next problem.

def main():
    print("========================================")
    print("LISTS AND TUPLES ASSIGNMENT")
    print("========================================")

    problem_1_shopping_list()
    problem_2_points_and_distance()
    problem_3_number_statistics()
    problem_4_student_grades()
    problem_5_word_list_analysis()
    problem_6_student_tuple_record()

    print("\n========================================")
    print("Program finished")
    print("========================================")


if __name__ == "__main__":
    main()


# ------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------
# Lists are useful when a collection needs to change during program
# execution because elements can be added, removed, or reordered.
# Tuples are useful when values should remain fixed after creation.
# Both structures allow ordered data to be accessed by index.
# Functions such as len(), sum(), min(), max(), and sorted() make
# collection processing easier and keep the code simple.
# Validating input before storing values prevents invalid data from
# affecting later calculations.
# This assignment helped practice list operations, tuple creation,
# indexing, searching, sorting, counting, and numeric aggregation.

# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python Software Foundation. Data Structures - Lists.
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 2) Python Software Foundation. Sequence Types - list and tuple.
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
#
# 3) Python Software Foundation. Built-in Functions.
#    https://docs.python.org/3/library/functions.html
#
# 4) Matthes, Eric. Python Crash Course, 3rd Edition.
#    No Starch Press, 2023.
#
# 5) Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition.
#    No Starch Press, 2019.
#
# 6) Real Python. Lists and Tuples in Python.
#    https://realpython.com/python-lists-tuples/

# ------------------------------------------------------------
# GITHUB REPOSITORY
# ------------------------------------------------------------
# Repository URL:
# https://github.com/Badillo00/tarea_strings_python

# ------------------------------------------------------------
# DELIVERY CHECKLIST
# ------------------------------------------------------------
# [x] Cover, executive summary, six problems, conclusions, references.
# [x] Each problem includes description, inputs, outputs, validations,
#     and normal, border, and error test cases.
# [x] Variables and output messages are in English.
# [x] Only lists and tuples are used as collection structures.
# [x] Input validation is included.
# [x] GitHub repository URL is included.
