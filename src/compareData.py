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

    # Display the data description for specific columns
    print(real_estate_data[['Serial Number', 'Town', 'Longitude', 'Latitude', 'Synth_Longitude', 'Synth_Latitude']].describe())



if __name__ == "__main__":
    csv_path = 'data/Updated_Real_Estate_Sales.csv'  # Update the path as needed
    main(csv_path)