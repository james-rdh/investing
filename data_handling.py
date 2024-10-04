# %pip install python-dotenv requests
import os # interact with the file system
from dotenv import load_dotenv # load the API key
import requests # communicate with the API
import json # work with json data
import sqlite3 # interact with the database

class DataHandler:
    def __init__(self, data_source = 'Alpha Vantage'):
        self.data_source = data_source
        load_dotenv()
        self.api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
    
    def create_database(self, db_path='./data/investment_data.db', db_schema_path='./db_schema.sql'):   
        """
        Creates a SQLite database with the specified schema for investment data.

        This function sets up a SQLite database with tables to store information 
        related to investment symbols, stock data, portfolios, positions, and 
        transactions. It handles the database connection, table creation, 
        and ensures foreign key constraints are enabled.

        Args:
            db_path (str, optional): The path to the SQLite database file. 
                                    Defaults to './data/investment_data.db'.
        """
        conn = None
        try:
            # connect to the database and create the tables
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            with open(db_schema_path, 'r') as f:
                cursor.executescript(f.read())
            conn.commit()
            print("Database and tables created successfully!")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            if conn:
                conn.close()

    def get_daily_ohlcv_data(self, symbol, outputsize='compact'):
        '''
        Fetches daily historical stock data from Alpha Vantage API.

        Args:
            symbol (str): The stock symbol (e.g., 'IBM').
            outputsize (str, optional): 'compact' (default; last 100 data points) or 'full' (full history). 

        Returns:
            list of tuples: Each tuple represents a row with the following 
                            elements: (symbol, date, open, high, low, close, volume).
                            Suitable for insertion into a SQLite table.
        '''
        if self.data_source == 'Alpha Vantage':
            base_url = 'https://www.alphavantage.co/query?'
            params = {
                'function': 'TIME_SERIES_DAILY',
                'symbol': symbol,
                'outputsize': outputsize,
                'apikey': self.api_key
            }
            response = requests.get(base_url, params=params)
            data = response.json()
            print("Data retrieved:\n", data['Meta Data'])
            time_series_data = data['Time Series (Daily)']
            data = []
            for date, values in time_series_data.items():
                row = (
                    symbol,
                    date,
                    float(values['1. open']),
                    float(values['2. high']),
                    float(values['3. low']),
                    float(values['4. close']),
                    int(values['5. volume'])
                )
                data.append(row)
            return data
    
    def insert_daily_ohlcv_data_into_database(self, data, db_path='./data/investment_data.db'):
        """
        Inserts stock data into the SQLite database.

        Args:
            data (list of tuples): Stock data to insert. Each tuple should have the format:
                                    (symbol, date, open, high, low, close, volume).
            db_path (str): Path to the SQLite database file.
        """
        conn = None
        try:
            # connect to the database and insert the data
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            for row in data:
                symbol, date, open_, high, low, close, volume = row
                cursor.execute("SELECT id FROM Instruments WHERE symbol = ?", (symbol,))
                instrument_id = cursor.fetchone()
                if instrument_id is None:
                    cursor.execute("INSERT INTO Instruments (symbol) VALUES (?)", (symbol,))
                    instrument_id = cursor.lastrowid
                else:
                    instrument_id = instrument_id[0]
                try:
                    cursor.execute('''
                        INSERT INTO InstrumentOHLCVs (instrument_id, date, open, high, low, close, volume) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (instrument_id, date, open_, high, low, close, volume))
                except sqlite3.IntegrityError:
                    print(f"Data for {symbol} on {date} already exists. Skipping.")
            conn.commit()
            print("Stock data inserted successfully!")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            if conn:
                conn.close()
    
    def get_last_close_data(self, symbol, datatype='json'):
        """
        Fetches the last close price for a given symbol from the Alpha Vantage API.

        This function retrieves the latest closing price for the specified financial
        instrument using the GLOBAL_QUOTE function of the Alpha Vantage API. 

        Args:
            symbol (str): The symbol of the financial instrument (e.g., 'IBM').
            datatype (str, optional): The format for the returned data. 
                                    Can be 'json' (default) or 'csv'.

        Returns:
            str: The last closing price as a string.

        Raises:
            KeyError: If the API response does not contain the expected keys 
                    ('Global Quote' or '05. price'). This could indicate an 
                    error with the API request or the symbol provided.
        """
        if self.data_source == 'Alpha Vantage':
            base_url = 'https://www.alphavantage.co/query?'
            params = {
                'function': 'GLOBAL_QUOTE',
                'symbol': symbol,
                'datatype': datatype,
                'apikey': self.api_key
            }
            try:
                response = requests.get(base_url, params=params)
                response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
                last_close = response.json()["Global Quote"]["05. price"]
                return last_close
            except requests.exceptions.RequestException as e:
                print(f"Error during API request: {e}")
                # You can add more specific error handling or logging here
                raise  # Re-raise the exception to be handled by the caller
            except KeyError as e:
                print(f"Error extracting close price from API response: {e}")
                raise