import pytest

from src.library_eligibility import can_borrow


@pytest.mark.parametrize(
    "active_loans, overdue_books",
    [
        (0, 0),  # no loans, no overdue
        (1, 0),  # one loan
        (4, 0),  # just below the 5 loan limit
        (3, 0),  # 3 loans and no overdue books
    ],
)
def test_can_borrow_under_loan_limit_and_no_overdue_returns_true(active_loans, overdue_books):
    # Act
    result = can_borrow(active_loans, overdue_books)

    # Assert
    assert result is True


@pytest.mark.parametrize(
    "active_loans, overdue_books",
    [
        (5, 0),  # exactly at the loan limit
        (6, 0),  # above the loan limit
        (0, 1),  # one overdue book
        (4, 3),  # several overdue books
        (5, 1),  # at the limit and overdue
        (10, 2),  # both conditions broken
    ],
)
def test_can_borrow_at_loan_limit_or_with_overdue_returns_false(active_loans, overdue_books):
    # Act
    result = can_borrow(active_loans, overdue_books)

    # Assert
    assert result is False


@pytest.mark.parametrize(
    "active_loans, overdue_books",
    [
        (-1, 0),  # negative loans
        (0, -1),  # negative overdue books
        (-1, -1),  # both negative
    ],
)
def test_can_borrow_negative_value_raises_value_error(active_loans, overdue_books):
    # Act and Assert
    with pytest.raises(ValueError):
        can_borrow(active_loans, overdue_books)


@pytest.mark.parametrize(
    "active_loans, overdue_books",
    [
        ("2", 0),  # loans is a string
        (2.0, 0),  # loans is a float
        (None, 0),  # loans is None
        (True, 0),  # loans is a bool
        (2, "0"),  # overdue is a string
        (2, 0.0),  # overdue is a float
        (2, None),  # overdue is None
        (2, False),  # overdue is a bool
    ],
)
def test_can_borrow_invalid_type_raises_type_error(active_loans, overdue_books):
    # Act and Assert
    with pytest.raises(TypeError):
        can_borrow(active_loans, overdue_books)
