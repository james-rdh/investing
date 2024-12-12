import json

def clean_alpha_vantage_stock_data(input_file, output_file):
    """
    Cleans and transforms Alpha Vantage stock data.

    Args:
        input_file (str): The path to the raw Alpha Vantage data file.
        output_file (str): The path to save the cleaned data.
    """
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)

        time_series = data['Time Series (Daily)']
        cleaned_data = []

        for date, values in time_series.items():
            cleaned_data.append({
                'date': date,
                'open': float(values['1. open']),
                'high': float(values['2. high']),
                'low': float(values['3. low']),
                'close': float(values['4. close']),
                'adjusted_close': float(values['5. adjusted close']),
                'volume': int(values['6. volume']),
                'dividend_amount': float(values['7. dividend amount']),
                'split_coefficient': float(values['8. split coefficient'])
            })

        with open(output_file, 'w') as f:
            json.dump(cleaned_data, f, indent=4)

            print(f"Data from {input_file} cleaned and saved to {output_file}")

    except Exception as e:
        print(f"Error cleaning data from {input_file}: {e}")

def main():
    clean_alpha_vantage_stock_data("../data/raw/daily_adjusted_stock_data_IBM.json", "../data/processed/daily_adjusted_stock_data_IBM.json")

if __name__ == "__main__":
    main()