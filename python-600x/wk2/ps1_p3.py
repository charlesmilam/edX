def item_order(order):
    salads = str(order.count('salad'))
    burgers = str(order.count('hamburger'))
    waters = str(order.count('water'))

    return 'salad:' + salads + ' hamburger:' + burgers + ' water:' + waters

print item_order("hamburger water hamburger")
