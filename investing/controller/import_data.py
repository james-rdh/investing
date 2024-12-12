from dotenv import load_dotenv
import requests
import json

def load_data_dictionary():
    try:
        with open('data-dictionary.json', 'r') as f:
            DATA_DICTIONARY = json.load(f)
    except FileNotFoundError:
        print("Error: data_dictionary.json file not found.")
        exit(1)
    return DATA_DICTIONARY
    
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

def import_data(endpoint_id, *params):
    try:
        # get data dictionary
        DATA_DICTIONARY = load_data_dictionary()
        # get endpoint
        endpoints = DATA_DICTIONARY['definitions']['endpoints']['endpoints']
        endpoint = next(ep for ep in endpoints if ep['id'] == endpoint_id)
        # get connection details
        if endpoint['location']['protocol'] == "https":
            base_url = endpoint['location']['baseUrl']
            params = params
        # get the data
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        # save the data
        with open(f'../data/raw/{endpoint['id']}.json', 'w') as f:
            json.dump(data, f, indent=4)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error importing data from : {e}")
    except ValueError as e:
        print(f"A value error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("hello world")

if __name__ == "__main__":
    main()