def margin_calculator(margin, price):
    """
    Calculates the total price of an item given the margin and the price without tax.

    Parameters:
    margin (float): The margin as a percentage.
    price (float): The price without tax.

    Returns:
    float: The total price of the item.

    """
    try:
        margin = float(margin)
        total = price/(1-margin/100)
        return total
    except:
        total = 0
        return total 

