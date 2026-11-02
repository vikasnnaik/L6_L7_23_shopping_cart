import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


# Branch coverage test cases

# item_total(): category validation branches
def test_valid_food_category():
    assert item_total("food", 100, 2) == 210


def test_valid_electronics_category():
    assert item_total("electronics", 20, 2) == 47


def test_valid_clothing_category():
    assert item_total("clothing", 100, 1) == 112


def test_invalid_category_branch():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


# item_total(): price and quantity validation branches
def test_negative_price_branch():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", -10, 1)


def test_zero_quantity_branch():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", 100, 0)


def test_valid_price_and_quantity_branch():
    assert item_total("food", 100, 2) == 210


# item_total(): bulk discount branches
def test_quantity_at_bulk_threshold():
    assert item_total("food", 100, 10) == 945


def test_quantity_below_bulk_threshold():
    assert item_total("food", 100, 2) == 210


# cart_discount(): discount tier branches
def test_cart_value_at_high_discount_threshold():
    assert cart_discount(5000, False, None) == 500


def test_cart_value_between_discount_thresholds():
    assert cart_discount(2000, False, None) == 200


def test_cart_value_below_discount_threshold():
    assert cart_discount(500, False, None) == 0


# cart_discount(): Prime branches
def test_prime_discount_branch():
    assert cart_discount(500, True, None) == 100


def test_non_prime_discount_branch():
    assert cart_discount(500, False, None) == 0


# cart_discount(): coupon condition branches
def test_valid_coupon_and_eligible_cart():
    assert cart_discount(2000, False, "FLAT10") == 400


def test_valid_coupon_but_ineligible_cart():
    assert cart_discount(500, False, "FLAT10") == 0


def test_invalid_coupon_branch():
    assert cart_discount(2000, False, "INVALID") == 200


# shipping_fee(): Prime and cart value branches
def test_prime_shipping_branch():
    assert shipping_fee(100, True, False) == 0


def test_non_prime_high_value_shipping_branch():
    assert shipping_fee(600, False, False) == 0


def test_non_prime_low_value_shipping_branch():
    assert shipping_fee(100, False, False) == 40


# shipping_fee(): express shipping branches
def test_express_non_prime_shipping():
    assert shipping_fee(100, False, True) == 140


def test_express_prime_shipping():
    assert shipping_fee(100, True, True) == 50


def test_non_express_shipping():
    assert shipping_fee(100, False, False) == 40