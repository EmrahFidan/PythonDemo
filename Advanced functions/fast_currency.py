import requests
from bs4 import BeautifulSoup

def get_exchange_rates(url):
    """
    Get exchange rates from the given URL.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        dict: A dictionary containing currency names as keys and their values as values.
    """
    try:
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")

        currency_names = soup.find_all("span", {"class": "name"})
        currency_values = soup.find_all("span", {"class": "value"})

        exchange_rates = {}
        for name, value in zip(currency_names, currency_values):
            exchange_rates[name.text] = value.text.strip()

        return exchange_rates
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)
        return {}

def main():
    url = "https://www.doviz.com/"
    exchange_rates = get_exchange_rates(url)

    if exchange_rates:
        for currency, value in exchange_rates.items():
            print(f"{currency} = {value}")
    else:
        print("Unable to fetch exchange rates. Please try again later.")

if __name__ == "__main__":
    main()
