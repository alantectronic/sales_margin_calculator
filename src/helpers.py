import requests

def get_dolar_to_mxn():
    """
    Retrieves the current dollar to mexican peso exchange rate from mx.dolarapi.com/v1/cotizaciones/usd.

    Returns:
    float: The exchange rate if successful, otherwise None.

    """
    try:
        response = requests.get("https://mx.dolarapi.com/v1/cotizaciones/usd")
        data = response.text
        i = data.find("venta") + 7
        data = data[i + 1:i+7]
        data = float(data)
        return data

    except Exception as e:
        print(e)

def margin_calculator(margin, price, currency):
    """
    Calculates the total price of an item given the margin and the price without tax.

    Parameters:
    margin (float): The margin as a percentage.
    price (float): The price without tax.

    Returns:
    float: The total price of the item.

    """
    print(margin, price, currency)
    try:
        if currency == "usd":
            c = get_dolar_to_mxn()
        else:
            c = 1
        price = float(price) * c
        margin = float(margin)
        total = price/(1-margin/100)
        return f'$ {round(total, 2)} MXN'
    except:
        total = 0
        return f'$ {total} MXN'
