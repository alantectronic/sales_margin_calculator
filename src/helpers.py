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