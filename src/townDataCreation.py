import pandas as pd
import sys
import json
import logging
from geocoding import get_lat_long

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_and_save_town_coordinates(file_path, output_json_path):
    # Load data into a pandas dataframe
    real_estate_df = pd.read_csv(file_path, low_memory=False)
    logging.info("Data loaded successfully from %s", file_path)

    # Extract unique towns
    unique_towns = real_estate_df['Town'].unique()

    # Fetch coordinates for each town and store in a dictionary
    town_coordinates = {}
    for town in unique_towns:
        town_coordinates[town] = get_lat_long(town)
        logging.info("Fetched coordinates for town: %s", town)

    # Save the town coordinates to a JSON file
    with open(output_json_path, 'w') as json_file:
        json.dump(town_coordinates, json_file)
    logging.info("Town coordinates saved to %s", output_json_path)

def main(file_path, output_json_path):
    fetch_and_save_town_coordinates(file_path, output_json_path)

if __name__ == "__main__":
    file_path = 'data\\Real_Estate_Sales_2001-2020_GL.csv'
    json_path = 'data\\Output\\town_coordinates.json'
    main(file_path, json_path)
