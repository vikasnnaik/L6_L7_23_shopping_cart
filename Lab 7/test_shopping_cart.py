
from hypothesis import given, strategies as st
from shopping_cart import cart_total, promo_percent, delivery_zone


# Test 1: Fuzz testing cart_total()
@given(st.text() | st.none())
def test_cart_total_no_crash(s):
    result = cart_total(s)
    assert isinstance(result, int)
    assert result >= 0


# Test 2: Fuzz testing promo_percent()
@given(st.text() | st.none())
def test_promo_percent_no_crash(s):
    result = promo_percent(s)
    assert isinstance(result, int)
    assert 0 <= result <= 100


# Test 3: Fuzz testing delivery_zone()
@given(st.text() | st.none())
def test_delivery_zone_no_crash(s):
    result = delivery_zone(s)
    assert result in ["North", "South", "East", "West", "Unknown"]
