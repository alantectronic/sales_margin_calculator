import requests

def get_dolar_to_mxn():
    try:
        response = requests.get("https://mx.dolarapi.com/v1/cotizaciones/usd")
        data = response.text
        i = data.find("venta") + 7
        data = data[i + 1:i+7]
        data = float(data)
        return data

    except Exception as e:
        print(e)

data = get_dolar_to_mxn()
print(data)
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

