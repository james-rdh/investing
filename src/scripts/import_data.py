import os
from dotenv import load_dotenv
import requests
import json

# Get data dictionary
try:
    with open('data_dictionary.json', 'r') as f:
        DATA_DICTIONARY = json.load(f)
except FileNotFoundError:
    print("Error: data_dictionary.json file not found.")
    exit(1)
    
# # Access endpoint information
# customer_db_endpoint = next(ep for ep in DATA_DICTIONARY['definitions']['endpoints']['endpoints'] if ep['id'] == 'EP_12345678')
# host = customer_db_endpoint['location']['host']
# port = customer_db_endpoint['location']['port']

# # Get api keys
# try:
#     load_dotenv()
#     ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
# except FileNotFoundError:
#     print("Error: .env file not found.")
#     exit(1)
# except KeyError as e:
#     print(f"Error: {e.args[0]} not found in the environment.")
#     exit(1)

def import_country_data():
    try:
        data_flow = DATA_DICTIONARY['data_flows']['Import country data']
        base_url = data_flow['source']['location']['baseUrl']
        params = {
            "fields": ['field1', 'field2']
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error importing data from : {e}")
    return data

def import_stock_data(symbol, output_size=None):
    return

def import_daily_stock_data(symbol, output_size=None):
    try:
        data_flow = DATA_DICTIONARY['data_flows']['Import daily stock data']
        base_url = data_flow['source']['location']['baseUrl']
        params = {
            "function": 'TIME_SERIES_DAILY_ADJUSTED',
            "symbol": symbol,
            "apikey": ALPHA_VANTAGE_API_KEY
        }
        if output_size == 'full':
            params['outputsize'] = output_size

        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        with open(f'../data/raw/{source}_{symbol}.json', 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Data for {symbol} from Alpha Vantage imported successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error importing data from Alpha Vantage: {e}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("hello world")

if __name__ == "__main__":
    main()