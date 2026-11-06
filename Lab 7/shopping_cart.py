
import re

ZONES = {
    "1": "North", "2": "North",
    "3": "West", "4": "West",
    "5": "South", "6": "South",
    "7": "East", "8": "East"
}


def cart_total(cart):
    if not isinstance(cart, str) or not cart.strip():
        return 0

    total = 0

    try:
        items = cart.split(',')

        for item in items:
            match = re.fullmatch(
                r"\s*([^:,]+):\s*(\d+)\s*x\s*(\d+)\s*",
                item
            )

            if not match:
                return 0

            name, price, qty = match.groups()

            if not name.strip():
                return 0

            total += int(price) * int(qty)

        return total

    except (ValueError, TypeError, OverflowError):
        return 0


def promo_percent(code):
    if not isinstance(code, str):
        return 0

    match = re.fullmatch(r"OFF(\d{1,3})", code.strip().upper())

    if not match:
        return 0

    percentage = int(match.group(1))

    if 0 <= percentage <= 100:
        return percentage

    return 0


def delivery_zone(pincode):
    if not isinstance(pincode, str):
        return "Unknown"

    if not re.fullmatch(r"[0-9]{6}", pincode):
        return "Unknown"

    return ZONES.get(pincode[0], "Unknown")


def main():
    print("==== Running cart_total ====")
    user_input = input(
        "Enter cart as name:pricexqty CSV "
        "(e.g. pen:10x2,book:250x1): "
    )
    result = cart_total(user_input)
    print("Cart Total:", result)

    print("\n==== Running promo_percent ====")
    user_input = input("Enter a promo code (e.g. OFF20): ")
    result = promo_percent(user_input)
    print("Discount Percent:", result)

    print("\n==== Running delivery_zone ====")
    user_input = input("Enter a 6 digit pincode (e.g. 560085): ")
    result = delivery_zone(user_input)
    print("Delivery Zone:", result)


if __name__ == "__main__":
    main()
