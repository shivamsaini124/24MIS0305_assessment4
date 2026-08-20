import pytest
from ecommerce import process_order


def test_single_product():
    result = process_order([
        {"product_id": "P001", "quantity": 1}
    ])

    assert result["subtotal"] == 1000


def test_multiple_products():
    result = process_order([
        {"product_id": "P001", "quantity": 1},
        {"product_id": "P002", "quantity": 2}
    ])

    assert result["subtotal"] == 2000


def test_zero_quantity():
    with pytest.raises(ValueError):
        process_order([
            {"product_id": "P001", "quantity": 0}
        ])


def test_negative_quantity():
    with pytest.raises(ValueError):
        process_order([
            {"product_id": "P001", "quantity": -1}
        ])


def test_invalid_product():
    with pytest.raises(ValueError):
        process_order([
            {"product_id": "P999", "quantity": 1}
        ])


def test_invalid_coupon():
    with pytest.raises(ValueError):
        process_order(
            [{"product_id": "P001", "quantity": 1}],
            "INVALID"
        )


def test_coupon():
    result = process_order(
        [{"product_id": "P001", "quantity": 1}],
        "SAVE10"
    )

    assert result["discount"] > 0


def test_free_shipping():
    result = process_order([
        {"product_id": "P001", "quantity": 3}
    ])

    assert result["shipping"] == 0


def test_bulk_order():
    result = process_order([
        {"product_id": "P002", "quantity": 10}
    ])

    assert result["discount"] > 0


def test_electronics_discount():
    result = process_order([
        {"product_id": "P001", "quantity": 1}
    ])

    assert result["discount"] > 0


def test_clothing_discount():
    result = process_order([
        {"product_id": "P002", "quantity": 1}
    ])

    assert result["discount"] > 0


def test_out_of_stock():
    with pytest.raises(ValueError):
        process_order([
            {"product_id": "P001", "quantity": 100}
        ])


def test_gst():
    result = process_order([
        {"product_id": "P003", "quantity": 1}
    ])

    assert result["gst"] > 0


def test_final_amount():
    result = process_order([
        {"product_id": "P001", "quantity": 2}
    ])

    assert result["final_amount"] > 0


def test_coupon_20():
    result = process_order(
        [{"product_id": "P003", "quantity": 2}],
        "SAVE20"
    )

    assert result["discount"] > 0


def test_large_order():
    result = process_order([
        {"product_id": "P001", "quantity": 5},
        {"product_id": "P002", "quantity": 5}
    ])

    assert result["subtotal"] == 7500


def test_small_order_shipping():
    result = process_order([
        {"product_id": "P003", "quantity": 1}
    ])

    assert result["shipping"] == 100


def test_maximum_discount():
    result = process_order(
        [{"product_id": "P001", "quantity": 10}],
        "SAVE20"
    )

    assert result["discount"] <= result["subtotal"] * 0.30


def test_two_products():
    result = process_order([
        {"product_id": "P001", "quantity": 1},
        {"product_id": "P003", "quantity": 1}
    ])

    assert result["subtotal"] == 1300


def test_three_products():
    result = process_order([
        {"product_id": "P001", "quantity": 1},
        {"product_id": "P002", "quantity": 1},
        {"product_id": "P003", "quantity": 1}
    ])

    assert result["subtotal"] == 1800


def test_coupon_with_multiple_products():
    result = process_order([
        {"product_id": "P001", "quantity": 2},
        {"product_id": "P003", "quantity": 2}
    ], "SAVE10")

    assert result["final_amount"] > 0