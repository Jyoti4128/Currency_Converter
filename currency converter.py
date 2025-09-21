import requests

def currency_converter(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    data = response.json()
    
    if to_currency.upper() in data['rates']:
        rate = data['rates'][to_currency.upper()]
        converted = amount * rate
        return converted
    else:
        return None

# --- User Input ---
amount = float(input("Enter amount: "))
from_currency = input("Enter currency you have (e.g., USD, INR, EUR): ")
to_currency = input("Enter currency you want (e.g., USD, INR, EUR): ")

converted_amount = currency_converter(amount, from_currency, to_currency)

if converted_amount:
    print(f"\n💰 {amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")
else:
    print("\n Currency not found or API error!")
