import requests

API_KEY = "fca_live_kLVu5iZCHDj6pPSFA7ReFyZoDfIe1BUSA1t6lQ2m"
URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCY = ["USD", "CAD", "EUR", "AUD"]

def currency(cur):
    currencies = ",".join(CURRENCY)
    url = f"{URL}&base_currency={cur}&currencies={currencies}"
    try:
        response = requests.get(url)
        RESULT = response.json()
        return(RESULT["data"])
    except Exception as e:
        print(e)
    
exchange = currency("USD")
for i, j in exchange.items():
    print(f"{i} and {j}")