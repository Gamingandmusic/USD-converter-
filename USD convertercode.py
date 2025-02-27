import requests

def fetch_exchange_rate(currency_code):
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    return data["rates"][currency_code]

def convert_currency(usd_amount, exchange_rate):
    return usd_amount * exchange_rate

def main():
    print("""
    Currency converter, converts USD$ to another Currency.
    by Gamingandmusic
    """)
    
    # Input
    usd = float(input("Amount of money in USD$: "))

    # Fetch exchange rates
    cad_rate = fetch_exchange_rate("CAD")
    gbp_rate = fetch_exchange_rate("GBP")
    euro_rate = fetch_exchange_rate("EUR")

    # Convert currencies
    cad = convert_currency(usd, cad_rate)
    gbp = convert_currency(usd, gbp_rate)
    euro = convert_currency(usd, euro_rate)

    # Print results
    print("Currency conversions:")
    print(f"USD: ${usd:.2f}")
    print(f"EUR: €{euro:.2f}")
    print(f"CAD: C${cad:.2f}")
    print(f"GBP: £{gbp:.2f}")

    # End program
    input("Press enter to quit")

if __name__ == "__main__":
    main()
