import random


# Wave 1
VALID_LETTERS = {'R', 'O', 'Y', 'G', 'B', 'P'}

def generate_code():
    # Generate a code of 4 random letters from VALID_LETTERS using a list comprehension
    letters_list = list(VALID_LETTERS)
    return [random.choice(letters_list) for _ in range(4)]


def validate_guess(guess):
    # Exit early if guess is not exactly 4 elements long
    if len(guess) != 4:
        return False

    # Normalize guess for case-insensitive comparison
    normalized_guess = normalize_code(guess)

    # Return False if we find an invalid element of guess
    for letter in normalized_guess:
        if letter not in VALID_LETTERS:
            return False

    return True


def check_code_guessed(guess, code):
    # Normalize guess for case-insensitive comparison
    normalized_guess = normalize_code(guess)
    return code == normalized_guess


def normalize_code(code):
    """Normalize a code by converting all elements to uppercase strings."""
    return [str(letter).upper() for letter in code]


# Wave 2

def color_count(guess, code):
    """
    Returns the number of pegs that are the correct color, regardless of position.
    Counts each letter up to the number of times it appears in the code.
    """
    guess_norm = normalize_code(guess)
    code_norm = normalize_code(code)

    # Считаем, сколько раз каждая буква встречается в code
    code_counts = {}
    for letter in code_norm:
        code_counts[letter] = code_counts.get(letter, 0) + 1

    # Суммируем минимальное количество для каждой буквы в guess
    return sum(min(guess_norm.count(letter), code_counts.get(letter, 0)) for letter in set(guess_norm))


def correct_pos_and_color(guess, code):
    """
    Returns the number of pegs in guess whose color is the same as the peg at the matching index in code.
    """
    guess_norm, code_norm = normalize_code(guess), normalize_code(code)
    return sum(g == c for g, c in zip(guess_norm, code_norm))

def generate_hint(guess, code):
    """
    Returns a tuple:
    (number of pegs correct in both color and position,
    number of pegs correct in color but wrong position)
    """
    correct = correct_pos_and_color(guess, code)
    total_color = color_count(guess, code)
    wrong_position = total_color - correct
    return (correct, wrong_position)

# Wave 3
# Add your Wave 3 functions here