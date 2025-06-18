def solution01(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)

def solution02(price):
    if price >= 500000:
        price *= 0.8
    elif price >= 300000:
        price *= 0.9
    elif price >= 100000:
        price *= 0.95
    return int(price)