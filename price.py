def format_price(price):
    return "Цена: %s руб." % str(round(price))


display_price = format_price(56.24)
print(display_price)
