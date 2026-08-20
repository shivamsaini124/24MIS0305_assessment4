import pytest
from loan import process_loan


def test_valid_loan():
    result = process_loan(
        "C001",
        25,
        50000,
        100000,
        750,
        "salaried",
        500000,
        5
    )

    assert result["approved"] is True
    assert result["emi"] > 0


def test_minimum_age():
    with pytest.raises(ValueError):
        process_loan(
            "C002", 17, 50000, 0,
            750, "salaried", 300000, 5
        )


def test_invalid_salary():
    with pytest.raises(ValueError):
        process_loan(
            "C003", 25, -1000, 0,
            750, "salaried", 300000, 5
        )


def test_poor_credit_score():
    result = process_loan(
        "C004", 25, 50000, 0,
        500, "salaried", 300000, 5
    )

    assert result["approved"] is False


def test_invalid_employment():
    with pytest.raises(ValueError):
        process_loan(
            "C005", 25, 50000, 0,
            750, "student", 300000, 5
        )


def test_emi_accuracy():
    result = process_loan(
        "C006", 30, 50000, 0,
        750, "salaried", 300000, 5
    )

    assert round(result["emi"], 2) == 6082.99