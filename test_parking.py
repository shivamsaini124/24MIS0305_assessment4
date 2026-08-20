import pytest
from parking import ParkingManagement


def test_vehicle_entry():
    parking = ParkingManagement()

    assert parking.entry("KA01", "Car") is True


def test_vehicle_exit():
    parking = ParkingManagement()

    parking.entry("KA01", "Car")

    fee = parking.exit("KA01", 2)

    assert fee == 80


def test_duplicate_vehicle():
    parking = ParkingManagement()

    parking.entry("KA01", "Car")

    with pytest.raises(ValueError):
        parking.entry("KA01", "Car")


def test_invalid_vehicle():
    parking = ParkingManagement()

    with pytest.raises(ValueError):
        parking.entry("KA01", "Bus")


def test_peak_pricing():
    parking = ParkingManagement()

    parking.entry("KA01", "Car")

    fee = parking.exit(
        "KA01",
        2,
        peak=True
    )

    assert fee == 120


def test_lost_ticket():
    parking = ParkingManagement()

    parking.entry("KA01", "Car")

    fee = parking.exit(
        "KA01",
        2,
        lost_ticket=True
    )

    assert fee == 580


def test_ev_charging():
    parking = ParkingManagement()

    parking.entry("EV01", "EV")

    fee = parking.exit(
        "EV01",
        2,
        ev_charging=True
    )

    assert fee == 180


def test_early_exit():
    parking = ParkingManagement()

    parking.entry("KA01", "Bike")

    fee = parking.exit("KA01", 1)

    assert fee == 20