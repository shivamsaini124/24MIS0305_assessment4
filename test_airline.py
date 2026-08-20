import pytest
from airline import AirlineReservation


def test_successful_booking():
    flight = AirlineReservation()

    fare = flight.book("P001", 5000)

    assert fare > 0
    assert flight.available_seats == 9


def test_double_booking():
    flight = AirlineReservation()

    flight.book("P001", 5000)

    with pytest.raises(ValueError):
        flight.book("P001", 5000)


def test_cancellation():
    flight = AirlineReservation()

    flight.book("P001", 5000)

    refund = flight.cancel("P001")

    assert refund > 0
    assert flight.available_seats == 10


def test_invalid_passenger():
    flight = AirlineReservation()

    with pytest.raises(ValueError):
        flight.cancel("INVALID")


def test_fully_booked():
    flight = AirlineReservation(1)

    flight.book("P001", 5000)

    with pytest.raises(ValueError):
        flight.book("P002", 5000)


def test_excess_baggage():
    flight = AirlineReservation()

    charge = flight.baggage_charge(25)

    assert charge == 1000


def test_normal_baggage():
    flight = AirlineReservation()

    assert flight.baggage_charge(10) == 0


def test_business_class():
    flight = AirlineReservation()

    fare = flight.book(
        "P001",
        5000,
        "Adult",
        "Business"
    )

    assert fare > 5000


def test_dynamic_pricing():
    flight = AirlineReservation(2)

    fare = flight.book("P001", 5000)

    assert fare > 5000