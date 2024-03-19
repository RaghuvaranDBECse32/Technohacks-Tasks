def convert_currency(amount, from_currency, to_currency):
    # Replace 'YOUR_API_KEY' with your actual API key from Open Exchange Rates
    api_key = 'YOUR_API_KEY'
    url = f'https://open.er-api.com/v6/latest/{from_currency}'
    
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            if to_currency in data['rates']:
                exchange_rate = data['rates'][to_currency]
                converted_amount = amount * exchange_rate
                return converted_amount
            else:
                return f"Error: Currency '{to_currency}' not found."
        else:
            return "Error: Unable to fetch exchange rates."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to Currency Converter!")
    amount = float(input("Enter amount to convert: "))
    from_currency = input("Enter currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter currency to convert to (e.g., EUR): ").upper()

    result = convert_currency(amount, from_currency, to_currency)
    if isinstance(result, float):
        print(f"{amount} {from_currency} is equivalent to {result} {to_currency}")
    else:
        print(result)

if __name__ == "__main__":
    main()
