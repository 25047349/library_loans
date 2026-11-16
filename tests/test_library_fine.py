import pytest

from src.library_fine import calculate_fine


@pytest.mark.parametrize(
    "days_overdue, expected_fine",
    [
        (0, 0),  
        (1, 50),
        (2, 100),   
        (10, 500), 
        (11, 550),  
        (100, 5000),  
    ],
)
def test_calculate_fine_valid_days_returns_50_cents_per_day(days_overdue, expected_fine):
    # Act
    result = calculate_fine(days_overdue)

    # Assert
    assert result == expected_fine


def test_calculate_fine_returns_int():
    # Act
    result = calculate_fine(3)

    # Assert
    assert type(result) is int


@pytest.mark.parametrize("days_overdue", [-1, -100])
def test_calculate_fine_negative_days_raises_value_error(days_overdue):
    # Act and Assert
    with pytest.raises(ValueError):
        calculate_fine(days_overdue)


@pytest.mark.parametrize("days_overdue", ["5", 2.5, None, True, False, [3]])
def test_calculate_fine_invalid_type_raises_type_error(days_overdue):
    # Act and Assert
    with pytest.raises(TypeError):
        calculate_fine(days_overdue)
