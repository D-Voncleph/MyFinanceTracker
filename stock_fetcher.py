import requests

def get_stock_price(symbol, api_key):
    """
    Fetches the current price for a given stock symbol using an API key.
    Returns the price if successful, otherwise returns None.
    """
    # The API endpoint with a placeholder for the stock symbol AND the API key
    api_url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"

    # Make the GET request
    response = requests.get(api_url)

    # Check if the request was successful
    if response.ok:
        # The API returns a list containing one dictionary
        data = response.json()

        # Check if the list is not empty
        if data:
            # Access the first dictionary and get the 'price' value
            price = data[0]['price']
            return price
        else:
            print(f"Error: No data found for symbol '{symbol}'.")
            return None
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None

# This is the main part of the script that uses the function
if __name__ == "__main__":
    # REPLACE THIS WITH YOUR OWN API KEY
    my_api_key = "f5ICE2NcvmESz9lpsiALJyxnskWCGVC7"

    # Check if the API key has been replaced
    if my_api_key == "YOUR_API_KEY":
        print("Please replace 'YOUR_API_KEY' in the script with your actual API key.")
    else:
        # Fetch and print the current price for Apple (AAPL)
        aapl_price = get_stock_price("AAPL", my_api_key)
        if aapl_price:
            print(f"The current price of AAPL is: ${aapl_price}")

        # Fetch and print the current price for Tesla (TSLA)
        tsla_price = get_stock_price("TSLA", my_api_key)
        if tsla_price:
            print(f"The current price of TSLA is: ${tsla_price}")