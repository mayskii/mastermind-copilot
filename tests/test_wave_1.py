from app.game import generate_code, validate_guess, check_code_guessed

# --------------------------test validate_guess------------------------------------

def test_validate_guess_false_length_greater_than_four():
    # Arrange
    guess = ['R', 'R', 'R', 'R', 'R']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_true_valid_letters_rygp():
    # Arrange
    guess = ['R', 'Y', 'G', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True


def test_validate_guess_true_valid_letters_bp():
    # Arrange
    guess = ['B', 'B', 'P', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True


def test_validate_guess_false_invalid_letters():
    # Arrange
    guess = ['R', 'S', 'Y', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_true_lowercase_letters():
    # Arrange
    guess = ['b', 'b', 'p', 'p']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True


def test_validate_guess_false_empty_list():
    # Arrange
    guess = []

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_false_length_less_than_four():
    # Arrange
    guess = ['R', 'O', 'Y']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_true_mixed_case_letters():
    # Arrange
    guess = ['R', 'o', 'Y', 'p']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True


def test_validate_guess_false_non_string_types():
    # Arrange
    guess = ['R', 1, 'Y', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_false_with_none_value():
    # Arrange
    guess = ['R', None, 'Y', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False

# --------------------------test check_win_or_lose------------------------------------

def test_check_code_guessed_true():
    # Arrange
    guess = ['R', 'B', 'B', 'P']
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is True


def test_check_code_guessed_no_match_false():
    # Arrange
    guess = ['R', 'B', 'B', 'P']
    code = ['R', 'B', 'B', 'O']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is False

def test_check_code_guessed_true_with_mixed_case_guess():
    # Arrange
    guess = ['r', 'B', 'b', 'P']
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is True


def test_check_code_guessed_all_letters_in_wrong_order_false():
    # Arrange
    guess = ['R', 'B', 'P', 'B']
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is False
