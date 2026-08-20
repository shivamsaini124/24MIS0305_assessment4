import pytest
from hospital import calculate_bill


def test_normal_patient():
    result = calculate_bill(
        30, "normal", 1, 500, 300
    )

    assert result["payable"] == 1300


def test_emergency():
    result = calculate_bill(
        30, "emergency", 1, 500, 300
    )

    assert result["consultation_fee"] == 750


def test_senior_citizen():
    result = calculate_bill(
        65, "normal", 1, 500, 300
    )

    assert result["consultation_fee"] == 400


def test_insurance():
    result = calculate_bill(
        30, "normal", 1, 500, 300, True
    )

    assert result["insurance"] > 0


def test_follow_up():
    result = calculate_bill(
        30, "follow-up", 1, 500, 300
    )

    assert result["consultation_fee"] == 250


def test_invalid_age():
    with pytest.raises(ValueError):
        calculate_bill(
            0, "normal", 1, 500, 300
        )


def test_invalid_appointment():
    with pytest.raises(ValueError):
        calculate_bill(
            30, "abc", 1, 500, 300
        )