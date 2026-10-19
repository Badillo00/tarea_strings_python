# ============================================================
# STRINGS ASSIGNMENT - PYTHON
# ============================================================
# Student: Emanuel Alejandro Badillo Hernandez
# Student ID: 2630419
# Group: 3
# File: 2630419_BadilloEmanuel_t_strings.py
# ============================================================

# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
# A string in Python is a sequence of characters used to store text.
# Strings are immutable, which means their contents cannot be changed
# directly; string methods create and return new strings instead.
# Common string operations include concatenation, length calculation,
# indexing, slicing, searching, replacing, splitting, and joining text.
# Input validation is important because users may enter empty text,
# extra spaces, incorrect formats, or inconsistent capitalization.
# Normalization with methods such as strip() and lower() makes text
# easier and safer to compare and process.
# This program contains six problems that practice string operations,
# input/output design, validation, formatting, and test cases.
# Each problem includes a description, inputs, outputs, validations,
# and three documented test cases: normal, border, and error.

# ------------------------------------------------------------
# PRINCIPLES AND GOOD PRACTICES
# ------------------------------------------------------------
# - Strings are immutable: any modification creates a new string.
# - Normalize user input with strip() and lower() before comparisons.
# - Avoid unexplained "magic numbers" in indexes and slices.
# - Use built-in string methods instead of rewriting basic operations.
# - Validate first that the input is not empty, then validate its format.
# - Use clear variable names and understandable error messages.
# - Keep code organized into functions to make it easier to test.
# - Use constants when a fixed value has a special meaning.

LABEL_WIDTH = 30
MIN_PASSWORD_LENGTH = 8
MIN_PALINDROME_LENGTH = 3


# ============================================================
# Problem 1: Full name formatter
# ============================================================
# Description:
# This problem receives a person's full name and normalizes extra
# spaces and capitalization. It displays the formatted name in
# Title Case and generates initials separated by periods.
#
# Inputs:
# - full_name: string containing at least two words.
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - full_name must not be empty after strip().
# - It must contain at least two words.
# - A string containing only spaces is invalid.
#
# Test cases:
# 1) Normal: "juan carlos tovar"
#    Expected: Juan Carlos Tovar / J.C.T.
# 2) Border: "  ANA   LOPEZ  "
#    Expected: Ana Lopez / A.L.
# 3) Error: "Juan"
#    Expected: Error because at least two words are required.

def problem_1_full_name_formatter():
    print("\n--- Problem 1: Full name formatter ---")

    full_name = input("Enter full name: ").strip()

    if not full_name:
        print("Error: invalid input")
        return

    name_parts = full_name.split()

    if len(name_parts) < 2:
        print("Error: at least two words are required")
        return

    normalized_name = " ".join(name_parts).title()
    initials = ".".join(part[0].upper() for part in name_parts) + "."

    print(f"Formatted name: {normalized_name}")
    print(f"Initials: {initials}")


# ============================================================
# Problem 2: Simple email validator
# ============================================================
# Description:
# This problem validates the basic structure of an email address.
# A valid email must contain exactly one '@', no spaces, and at
# least one '.' after the '@'. If valid, the domain is displayed.
#
# Inputs:
# - email_text: string containing an email address.
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - email_text must not be empty after strip().
# - It must contain exactly one '@'.
# - It must not contain spaces.
# - The local part and domain must not be empty.
# - The domain must contain a '.' after '@'.
#
# Test cases:
# 1) Normal: "student@example.com"
#    Expected: valid / domain example.com
# 2) Border: "a@b.co"
#    Expected: valid / domain b.co
# 3) Error: "student example.com"
#    Expected: invalid

def problem_2_email_validator():
    print("\n--- Problem 2: Simple email validator ---")

    email_text = input("Enter email: ").strip()

    if not email_text:
        print("Valid email: false")
        print("Error: invalid input")
        return

    valid_email = True

    if email_text.count("@") != 1:
        valid_email = False

    if " " in email_text:
        valid_email = False

    if valid_email:
        at_index = email_text.find("@")
        local_part = email_text[:at_index]
        domain_part = email_text[at_index + 1:]

        if not local_part or not domain_part:
            valid_email = False
        elif "." not in domain_part:
            valid_email = False
        elif domain_part.startswith(".") or domain_part.endswith("."):
            valid_email = False

    if valid_email:
        print("Valid email: true")
        print(f"Domain: {domain_part.lower()}")
    else:
        print("Valid email: false")


# ============================================================
# Problem 3: Palindrome checker
# ============================================================
# Description:
# This problem checks whether a phrase reads the same forward
# and backward. Spaces and letter case are ignored.
#
# Inputs:
# - phrase: string containing a phrase.
#
# Outputs:
# - "Normalized phrase: <text>"
# - "Is palindrome: true" or "Is palindrome: false"
#
# Validations:
# - phrase must not be empty after strip().
# - The normalized phrase must contain at least 3 characters.
#
# Test cases:
# 1) Normal: "Anita lava la tina"
#    Expected: palindrome
# 2) Border: "Oso"
#    Expected: palindrome
# 3) Error: "  a  "
#    Expected: Error because fewer than 3 characters remain.

def problem_3_palindrome_checker():
    print("\n--- Problem 3: Palindrome checker ---")

    phrase = input("Enter phrase: ").strip()

    if not phrase:
        print("Error: invalid input")
        return

    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < MIN_PALINDROME_LENGTH:
        print("Error: phrase is too short")
        return

    reversed_phrase = normalized_phrase[::-1]
    is_palindrome = normalized_phrase == reversed_phrase

    print(f"Normalized phrase: {normalized_phrase}")
    print(f"Is palindrome: {str(is_palindrome).lower()}")


# ============================================================
# Problem 4: Sentence word stats
# ============================================================
# Description:
# This problem receives a sentence, separates it into words,
# counts the total words, and shows the first, last, shortest,
# and longest words.
#
# Inputs:
# - sentence: string containing one or more words.
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - sentence must not be empty after strip().
# - There must be at least one valid word after split().
#
# Test cases:
# 1) Normal: "Python makes text processing easy"
#    Expected: 5 words; first Python; last easy
# 2) Border: "Hello"
#    Expected: 1 word; all results are Hello
# 3) Error: "      "
#    Expected: Error: invalid input

def problem_4_sentence_stats():
    print("\n--- Problem 4: Sentence word stats ---")

    sentence = input("Enter sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    words = sentence.split()

    if not words:
        print("Error: invalid input")
        return

    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

        if len(word) > len(longest_word):
            longest_word = word

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# ============================================================
# Problem 5: Password strength classifier
# ============================================================
# Description:
# This problem classifies a password as weak, medium, or strong.
# A strong password must contain at least 8 characters, including
# uppercase, lowercase, digit, and non-alphanumeric symbol.
#
# Inputs:
# - password_input: string containing the password.
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - The password must not be empty.
# - Its length is checked using len().
#
# Classification rules:
# - Weak: shorter than 8 characters, or contains only one character type.
# - Medium: at least 8 characters and contains at least two character types.
# - Strong: at least 8 characters and contains uppercase, lowercase,
#   digit, and symbol.
#
# Test cases:
# 1) Normal: "Python#2026"
#    Expected: strong
# 2) Border: "Password1"
#    Expected: medium
# 3) Error: ""
#    Expected: Error: invalid input

def problem_5_password_strength():
    print("\n--- Problem 5: Password strength classifier ---")

    password_input = input("Enter password: ")

    if not password_input:
        print("Error: invalid input")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    type_count = sum([has_upper, has_lower, has_digit, has_symbol])

    if (
        len(password_input) >= MIN_PASSWORD_LENGTH
        and has_upper
        and has_lower
        and has_digit
        and has_symbol
    ):
        password_strength = "strong"
    elif len(password_input) >= MIN_PASSWORD_LENGTH and type_count >= 2:
        password_strength = "medium"
    else:
        password_strength = "weak"

    print(f"Password strength: {password_strength}")


# ============================================================
# Problem 6: Product label formatter
# ============================================================
# Description:
# This problem receives a product name and price and generates
# one fixed-width label. The final label must contain exactly
# 30 characters. Long labels are cut and short labels are padded.
#
# Inputs:
# - product_name: non-empty string.
# - price_value: positive numeric value.
#
# Outputs:
# - 'Label: "<exactly 30 characters>"'
# - "Length: 30"
#
# Validations:
# - product_name must not be empty after strip().
# - price_value must be numeric.
# - price_value must be greater than 0.
#
# Test cases:
# 1) Normal: product="Keyboard", price="450"
#    Expected: label padded to exactly 30 characters
# 2) Border: product="A", price="1"
#    Expected: valid label padded to 30 characters
# 3) Error: product="Mouse", price="-10"
#    Expected: Error because price must be positive

def problem_6_product_label():
    print("\n--- Problem 6: Product label formatter ---")

    product_name = input("Enter product name: ").strip()

    if not product_name:
        print("Error: invalid input")
        return

    price_text = input("Enter price: ").strip()

    if not price_text:
        print("Error: invalid input")
        return

    try:
        price_value = float(price_text)
    except ValueError:
        print("Error: price must be numeric")
        return

    if price_value <= 0:
        print("Error: price must be positive")
        return

    if price_value.is_integer():
        price_display = str(int(price_value))
    else:
        price_display = f"{price_value:.2f}".rstrip("0").rstrip(".")

    base_label = f"Product: {product_name} | Price: ${price_display}"

    if len(base_label) > LABEL_WIDTH:
        final_label = base_label[:LABEL_WIDTH]
    else:
        spaces_needed = LABEL_WIDTH - len(base_label)
        final_label = base_label + (" " * spaces_needed)

    print(f'Label: "{final_label}"')
    print(f"Length: {len(final_label)}")


# ============================================================
# MAIN PROGRAM
# ============================================================
# The six problems run in order. Each one asks for its own input.
# If an input is invalid, that problem prints an error message and
# the program continues with the next problem.

def main():
    print("========================================")
    print("PYTHON STRINGS ASSIGNMENT")
    print("========================================")

    problem_1_full_name_formatter()
    problem_2_email_validator()
    problem_3_palindrome_checker()
    problem_4_sentence_stats()
    problem_5_password_strength()
    problem_6_product_label()

    print("\n========================================")
    print("Program finished")
    print("========================================")


if __name__ == "__main__":
    main()


# ------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------
# String handling is essential because many programs receive and
# display information in text form. Methods such as lower(), strip(),
# split(), join(), replace(), and title() make text processing easier.
# Normalizing text before comparing it helps avoid errors caused by
# capitalization or unnecessary spaces.
# Validation is important because it prevents invalid or incomplete
# information from being processed by the program.
# This assignment also demonstrates that strings are immutable, so
# transformations create new strings instead of changing the original.
# Slicing is useful for extracting, reversing, or limiting text.
# Clear variable names and organized functions make code easier to read,
# test, maintain, and explain.

# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python Software Foundation. Built-in Types - Text Sequence Type: str.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# 2) Python Software Foundation. Python Tutorial - An Informal Introduction.
#    https://docs.python.org/3/tutorial/introduction.html#strings
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
# 6) Real Python. Python Strings and Character Data.
#    https://realpython.com/python-strings/
#
# ------------------------------------------------------------
# GITHUB REPOSITORY
# ------------------------------------------------------------
# Repository URL:
# https://github.com/Badillo00/tarea_strings_python
#
# Replace the URL above with the real GitHub repository URL before
# submitting the assignment.
#
# ------------------------------------------------------------
# DELIVERY CHECKLIST
# ------------------------------------------------------------
# [x] Correct file name format.
# [x] Cover, executive summary, problems 1-6, conclusions, references.
# [x] Description, inputs, outputs, validations, and 3 test cases.
# [x] English variable names and screen messages.
# [x] String methods, slicing, concatenation, validation, and formatting.
# [ ] Replace the GitHub repository URL with the real repository link.
# [ ] Add the group in the cover section.
# [ ] Run and verify the six problems before submission.
