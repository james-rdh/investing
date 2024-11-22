from .models import *
import json

def main():
    # Get data dictionary
    try:
        with open('./data/data_dictionary.json', 'r') as f:
            DATA_DICTIONARY = json.load(f)
    except FileNotFoundError:
        print("Error: data_dictionary.json file not found.")
        exit(1)
    
    # User login
    
    # Connect to data
    
    # Display data
    assets = {
        "GOOGL": {
            "quantity": 30,
            "purchase_price": 159.53
        },
        "MSFT": {
            "quantity": 10,
            "purchase_price": 404.60
        },
        "BRK-B": {
            "quantity": 9,
            "purchase_price": 445.98
        },
        "ADBE": {
            "quantity": 3,
            "purchase_price": 516.66
        }
    }
    
    return assets

if __name__ == '__main__':
    main()