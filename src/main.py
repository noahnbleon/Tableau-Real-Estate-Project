import pandas as pd
import sys
import json
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_town_coordinates(json_file_path):
    with open(json_file_path, 'r') as file:
        return json.load(file)

def extract_coordinates(df):
    def extract_lat_long(point_str):
        if isinstance(point_str, str):
            point_str = point_str.replace('POINT (', '').replace(')', '')
            longitude, latitude = point_str.split(' ')
            return float(longitude), float(latitude)
        return None, None

    df['Longitude'], df['Latitude'] = zip(*df['Location'].apply(extract_lat_long))
    return df

def create_synth_locations(df, town_coordinates):
    def create_synth_location(row):
        town = row['Town']
        if town in town_coordinates:
            lat, long = town_coordinates[town]
            return f'POINT ({long} {lat})'
        return None

    df['Synth_Location'] = df.apply(create_synth_location, axis=1)
    return df

def extract_synth_coordinates(df):
    def extract_lat_long(point_str):
        if isinstance(point_str, str):
            point_str = point_str.replace('POINT (', '').replace(')', '')
            longitude, latitude = point_str.split(' ')
            return float(longitude), float(latitude)
        return None, None

    df['Synth_Longitude'], df['Synth_Latitude'] = zip(*df['Synth_Location'].apply(extract_lat_long))
    return df

def process_real_estate_data(file_path, town_coordinates):
    real_estate_df = pd.read_csv(file_path, low_memory=False)
    logging.info("Data loaded successfully from %s", file_path)

    real_estate_df = extract_coordinates(real_estate_df)
    real_estate_df = create_synth_locations(real_estate_df, town_coordinates)
    real_estate_df = extract_synth_coordinates(real_estate_df)
    

    return real_estate_df

def main(file_path, json_file_path):
    logging.info("Starting processing for %s", file_path)

    # Load town coordinates from JSON file
    town_coordinates = load_town_coordinates(json_file_path)
    logging.info("Town coordinates loaded successfully from %s", json_file_path)

    processed_df = process_real_estate_data(file_path, town_coordinates)

    output_file_path = 'data/Updated_Real_Estate_Sales.csv'
    processed_df.to_csv(output_file_path, index=False)
    logging.info("Processed data saved to %s", output_file_path)

if __name__ == "__main__":
    csv_path = 'data\\Real_Estate_Sales_2001-2020_GL.csv'
    json_path = 'data\\Output\\town_coordinates.json'
    main(csv_path, json_path)