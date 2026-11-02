import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


# Code coverage test cases

def test_food_item():
    assert item_total("food", 100, 2) == 210


def test_electronics_item():
    assert item_total("electronics", 20, 2) == 47


def test_bulk_quantity_discount():
    assert item_total("food", 100, 10) == 945


def test_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


def test_negative_price():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", -10, 1)


def test_zero_quantity():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", 100, 0)


def test_high_value_cart_discount():
    assert cart_discount(6000, False, None) == 500


def test_medium_value_prime_cart_discount():
    assert cart_discount(2500, True, None) == 300


def test_low_value_cart_discount():
    assert cart_discount(500, False, None) == 0


def test_valid_coupon():
    assert cart_discount(2000, False, "FLAT10") == 400


def test_invalid_coupon():
    assert cart_discount(2000, False, "INVALID") == 200


def test_prime_free_shipping():
    assert shipping_fee(100, True, False) == 0


def test_non_prime_free_shipping():
    assert shipping_fee(600, False, False) == 0


def test_low_value_shipping():
    assert shipping_fee(100, False, False) == 40


def test_express_shipping():
    assert shipping_fee(100, False, True) == 140


def test_prime_express_shipping():
    assert shipping_fee(100, True, True) == 50