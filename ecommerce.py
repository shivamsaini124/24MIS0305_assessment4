PRODUCTS = {
    "P001": {"category": "electronics", "price": 1000, "stock": 20},
    "P002": {"category": "clothing", "price": 500, "stock": 50},
    "P003": {"category": "books", "price": 300, "stock": 100},
}


def process_order(items, coupon=None):
    subtotal = 0
    category_discount = 0

    for item in items:
        product_id = item["product_id"]
        quantity = item["quantity"]

        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if product_id not in PRODUCTS:
            raise ValueError("Invalid product")

        product = PRODUCTS[product_id]

        if quantity > product["stock"]:
            raise ValueError("Out of stock")

        amount = product["price"] * quantity
        subtotal += amount

        if product["category"] == "electronics":
            category_discount += amount * 0.10

        elif product["category"] == "clothing":
            category_discount += amount * 0.05

        if quantity >= 10:
            category_discount += amount * 0.05

    coupons = {
        "SAVE10": 0.10,
        "SAVE20": 0.20
    }

    if coupon is not None:
        if coupon not in coupons:
            raise ValueError("Invalid coupon")

        coupon_discount = subtotal * coupons[coupon]
    else:
        coupon_discount = 0

    total_discount = min(
        category_discount + coupon_discount,
        subtotal * 0.30
    )

    taxable_amount = subtotal - total_discount
    gst = taxable_amount * 0.18

    shipping = 0 if taxable_amount >= 2000 else 100

    final_amount = taxable_amount + gst + shipping

    return {
        "subtotal": subtotal,
        "discount": total_discount,
        "gst": gst,
        "shipping": shipping,
        "final_amount": final_amount
    }