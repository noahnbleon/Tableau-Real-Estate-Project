# Data Augmentation
## Overview
This Python project is aimed at analyzing and validating geographic data within a Connecticut real estate dataset. Key components include the townDataCreation.py script, which efficiently generates a JSON file of geographic coordinates for towns using the `OpenStreetMap Nominatim API`. The primary script, main.py, loads this data and calculates distances between actual and synthetic property locations using the Haversine formula. This process is crucial for verifying the accuracy of synthetic coordinates. Additionally, the script analyzes spatial distributions and discrepancies in the dataset, providing valuable insights for real estate analysis and ensuring the integrity of the geographic data used.

## Requirements
This portion of the project used the following Python libraries:
1. Pandas
2. Numpy
3. JSON
4. Logging
5. Requests
   
## File Descriptions
1. geocoding.py: A utility script that fetches latitude and longitude data for given town names by making requests to the `OpenStreetMap Nominatim API`.

2. townDataCreation.py: Generates a JSON file containing precise geographic coordinates for towns in Connecticut, minimizing API calls and ensuring accurate geolocation data for the project.

3. compareData.py: Analyzes real estate data by calculating distances between actual and synthetic locations and provides statistical insights into the spatial distribution of properties.

4. main.py: The central script of the project, orchestrating the loading, processing, and analysis of real estate data, including the calculation of distances using the Haversine formula and generating summaries of the dataset's geographic characteristics.

## geocoding.py
The get_lat_long function in Python is designed to fetch the geographic coordinates (latitude and longitude) of a specified town in Connecticut. It constructs a geocoding query by appending 'Connecticut' to the provided town name, ensuring more precise location results. The function then communicates with the `OpenStreetMap Nominatim API`, sending the query and processing the response to extract and return the latitude and longitude if available, or None if the town cannot be found or in case of an error (no errors occurred when this was executed).
```python
import requests

def get_lat_long(town_name):
    
    # Append 'Connecticut' to the town name for more accurate geocoding
    full_query = f"{town_name}, Connecticut"
    
    # Encode the town name to be URL-friendly
    town_name_encoded = requests.utils.quote(full_query)

    # Nominatim API endpoint with the encoded town name
    url = f"https://nominatim.openstreetmap.org/search?q={town_name_encoded}&format=json"

    # Make the request
    response = requests.get(url, headers={"User-Agent": "YourAppName"})

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if data:
            # Extract latitude and longitude
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
        else:                                                                                                               
            return None, None
    else:
        return None, None 
```
## townDataCreation.py
The townDataCreation.py script efficiently generates a JSON file with geographic coordinates for Connecticut towns, minimizing API calls to `OpenStreetMap Nominatim`. This approach ensures responsible usage of web resources while providing accurate data for location-based analyses in the project
```python
import pandas as pd
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
```

## compareData.py
After the creation of the JSON file, it was crucial to determine if the program had successfully found the coordinates before the main program was run to create a new CSV file. This was done using the `haversine formula`:\
$`
- $`a = sin²(φB - φA/2) + cos φA * cos φB * sin²(λB - λA/2)`$
- $`c = 2 * atan2( √a, √(1−a) )`$
- $`d = R ⋅ c`$
- *Note the haversine function used is based on one found here: https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128#:~:text=For%20example%2C%20haversine(%CE%B8),longitude%20of%20the%20two%20points.*

After creating the haversine function it was necessary to perform some analysis using the following program:
```python
import pandas as pd
import numpy as np

def load_data(file_path):
    columns_to_load = ['Serial Number', 'Location', 'Longitude', 'Latitude', 'Synth_Location', 'Synth_Longitude', 'Synth_Latitude', 'Town']
    df = pd.read_csv(file_path, usecols=columns_to_load)
    return df

def haversine(lon1, lat1, lon2, lat2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

def calculate_distances(df):
    # Filter out rows with any null values in the specified columns
    filtered_df = df.dropna(subset=['Longitude', 'Latitude', 'Synth_Longitude', 'Synth_Latitude'])

    # Apply the Haversine formula to the filtered DataFrame
    distances = filtered_df.apply(lambda row: haversine(row['Longitude'], row['Latitude'], 
                                                        row['Synth_Longitude'], row['Synth_Latitude']), axis=1)
    filtered_df['Distance'] = distances
    return filtered_df



def count_non_null_cells(df):
    location_columns = ['Location', 'Longitude', 'Latitude', 'Synth_Location', 'Synth_Longitude', 'Synth_Latitude']
    non_null_counts = df[location_columns].notnull().sum()
    print("Non-null counts for location columns:")
    print(non_null_counts)

def analyze_locations(df):
    # Filter out rows where the original 'Location' is not null
    non_null_locations_df = df[df['Location'].notna()]

    # Analysis 1: Compare Original and Synthetic Coordinates
    # Display the counts of matching and non-matching coordinates
    matching_coords = non_null_locations_df[(non_null_locations_df['Longitude'] == non_null_locations_df['Synth_Longitude']) &
                                            (non_null_locations_df['Latitude'] == non_null_locations_df['Synth_Latitude'])]
    print(f"Number of matching original and synthetic coordinates: {len(matching_coords)}")

    non_matching_coords = non_null_locations_df[(non_null_locations_df['Longitude'] != non_null_locations_df['Synth_Longitude']) |
                                                (non_null_locations_df['Latitude'] != non_null_locations_df['Synth_Latitude'])]
    print(f"Number of non-matching original and synthetic coordinates: {len(non_matching_coords)}")

    # Analysis 2: Geographical Distribution Analysis
    # Count properties per unique original location
    location_counts = non_null_locations_df['Location'].value_counts()
    print("Number of properties per unique location:")
    print(location_counts.head(10))  # Display top 10 locations by property count


def filter_large_distances(df, distance_threshold=50):
    # Filter the DataFrame for distances greater than the threshold
    filtered_df = df[df['Distance'] > distance_threshold]
    return filtered_df[['Serial Number', 'Town', 'Distance']]

def main(csv_file_path):
    # Load the data
    real_estate_data = load_data(csv_file_path)
    
    # Calculate distances
    real_estate_data_with_distances = calculate_distances(real_estate_data)
    
    # Filter for large distances and select required columns
    large_distance_data = filter_large_distances(real_estate_data_with_distances)
    
    # Display the result
    print(large_distance_data.describe())

    # Display the original data description
    print(real_estate_data.describe())

if __name__ == "__main__":
    csv_path = 'data/Updated_Real_Estate_Sales.csv'  # Update the path as needed
    main(csv_path)
```
*Note: not all of the functions created were used in the final execution of the main method, however, they were used to perform analysis during the process. This analysis was not crucial for the final interpretation but used for determining specific details about the data*

The result of this program was two key data frames:
1. large_distance_data (used to find cities that have abnormally large distances between the original location data and the synthetic data.
   
|        | Serial Number | Distance    |
|--------|---------------|-------------|
| count  | 5.18e+02      | 518.000000  |
| mean   | 3.832947e+05  | 102.507205  |
| std    | 2.145142e+06  | 220.020859  |
| min    | 8.237e+03     | 50.179277   |
| 25%    | 3.0374e+04    | 58.949696   |
| 50%    | 1.20036e+05   | 75.266077   |
| 75%    | 1.90636e+05   | 97.997658   |
| max    | 2.001001e+07  | 4053.957663 |

2. real_estate_data
   
|        | Serial Number | Longitude   | Latitude    | Synth_Longitude | Synth_Latitude |
|--------|---------------|-------------|-------------|-----------------|----------------|
| count  | 9.97213e+05   | 197697.0000 | 197697.0000 | 997213.000000   | 997213.000000  |
| mean   | 4.311864e+05  | -72.873124  | 41.500454   | -72.866767      | 41.497140      |
| std    | 6.549219e+06  | 0.450165    | 0.259607    | 0.431664        | 0.260501       |
| min    | 0.000000e+00  | -121.230910 | 34.345810   | -73.628460      | 41.026486      |
| 25%    | 3.0444e+04    | -73.188310  | 41.291420   | -73.204835      | 41.281484      |
| 50%    | 7.0303e+04    | -72.893090  | 41.505950   | -72.893712      | 41.498986      |
| 75%    | 1.51878e+05   | -72.617270  | 41.720100   | -72.612035      | 41.714267      |
| max    | 2.0005e+09    | -71.187550  | 44.934590   | -71.828682      | 42.022500      |


This presented a key finding, given the max of ≈4053, the mean of ≈102, and the standard deviation of ≈220, it was clear that there were some discrepancies between the original and synthetic data. Initially this points to the synthetic data having some issues, however, when analyzing the second data frame it is apparent that the `min Longitude` of **-121.230910** and a `min Latitude` of **34.345810**. This was original data that posed an error, as these coordinates are in the Pacific Ocean just west of Santa Barbara, California. All of the boundaries of the synthetic data we produced were within the state of Connecticut and aggregated by town, which demonstrated that the synthetic data had been successfully created.

## main.py
This main program was run to create a new CSV file with the synthetic data added to a dataframe of the original CSV file. The new data frame was subsequently exported into a new CSV file called `Updated_Real_Estate_Sales.csv`.
```python
import pandas as pd
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
```
