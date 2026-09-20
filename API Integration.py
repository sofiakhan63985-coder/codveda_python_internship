import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"


def fetch_crypto_prices(crypto_ids=None, currency="usd"):
    if crypto_ids is None:
        crypto_ids = ["bitcoin", "ethereum", "cardano"]

    params = {
        "ids": ",".join(crypto_ids),
        "vs_currencies": currency.lower()
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return {}
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return {}
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return {}
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
        return {}

    formatted_data = {}
    for coin, values in data.items():
        price = values.get(currency.lower(), "N/A")
        formatted_data[coin] = price
        if isinstance(price, (int, float)):
            print(f"• {coin.capitalize()}: ${price:,.2f}")
        else:
            print(f"• {coin.capitalize()}: {price}")

    return formatted_data


if __name__ == "__main__":
    print("\n=== CRYPTOCURRENCY PRICES ===")
    fetch_crypto_prices()