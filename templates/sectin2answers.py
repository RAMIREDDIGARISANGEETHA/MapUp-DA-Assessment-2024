#9)

#import pandas as pd
import numpy as np

def calculate_distance_matrix(file_path):
    # Load the dataset from CSV
    df = pd.read_csv(file_path, index_col=0)

    # Initialize an empty DataFrame for storing cumulative distances
    distance_matrix = pd.DataFrame(np.inf, index=df.index, columns=df.columns)

    # Set the diagonal values to 0 (distance to self is 0)
    np.fill_diagonal(distance_matrix.values, 0)

    # Copy the known distances from the original matrix
    for i in df.index:
        for j in df.columns:
            if i == j:
                distance_matrix.loc[i, j] = 0  # Set diagonal to 0
            elif pd.notnull(df.loc[i, j]):
                distance_matrix.loc[i, j] = df.loc[i, j]  # Copy distance
                distance_matrix.loc[j, i] = df.loc[i, j]  # Ensure symmetry

    # Apply the Floyd-Warshall algorithm for cumulative distances
    for k in df.index:
        for i in df.index:
            for j in df.columns:
                # Check if the distance through k is shorter
                if distance_matrix.loc[i, j] > distance_matrix.loc[i, k] + distance_matrix.loc[k, j]:
                    distance_matrix.loc[i, j] = distance_matrix.loc[i, k] + distance_matrix.loc[k, j]

    return distance_matrix

# Example usage (assuming the CSV file path is provided):
# result_df = calculate_distance_matrix(file_path)
# print(result_df)

#10)
import pandas as pd
from itertools import combinations

def unroll_distance_matrix(df):
    # Get unique values of id_start and id_end
    ids = set(df['id_start'].unique()).union(set(df['id_end'].unique()))
    
    # Create all combinations of ids, excluding same id_start and id_end
    id_combinations = list(combinations(ids, 2))
    
    # Create an empty list to store the new rows
    rows = []
    
    # Loop through all combinations
    for id1, id2 in id_combinations:
        # Get the distance for each combination
        distance_row_1 = df[(df['id_start'] == id1) & (df['id_end'] == id2)]
        distance_row_2 = df[(df['id_start'] == id2) & (df['id_end'] == id1)]
        
        # If a matching distance is found, add the entry to the new DataFrame
        if not distance_row_1.empty:
            rows.append({'id_start': id1, 'id_end': id2, 'distance': distance_row_1['distance'].values[0]})
        if not distance_row_2.empty:
            rows.append({'id_start': id2, 'id_end': id1, 'distance': distance_row_2['distance'].values[0]})
    
    # Convert the list of rows into a DataFrame
    return pd.DataFrame(rows)
df = pd.DataFrame({
    'id_start': [1001400]*9,
    'id_end': [1001402, 1001404, 1001406, 1001408, 1001410, 1001412, 1001414, 1001416, 1001418],
    'distance': [9.7, 29.9, 45.9, 67.6, 78.7, 94.3, 112.5, 125.7, 139.3]
})


#11)

def find_ids_within_ten_percentage_threshold(df: pd.DataFrame, reference_id: int) -> list:
    """
    Finds IDs within a 10% threshold of the average distance of a reference ID.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the distance matrix.
        reference_id (int): The reference ID from the id_start column.
    
    Returns:
        list: A sorted list of IDs from the id_start column that lie within the 10% threshold.
    """
    # Get the row for the reference ID and calculate its average distance
    reference_row = df.loc[reference_id]
    reference_avg_distance = reference_row.mean()

    # Calculate the 10% threshold range (floor and ceiling)
    lower_bound = reference_avg_distance * 0.9
    upper_bound = reference_avg_distance * 1.1

    # Create an empty list to store matching IDs
    matching_ids = []

    # Iterate over all rows (IDs) in the DataFrame to check the average distances
    for idx, row in df.iterrows():
        avg_distance = row.mean()
        if lower_bound <= avg_distance <= upper_bound:
            matching_ids.append(idx)

    # Return a sorted list of matching IDs
    return sorted(matching_ids)

# Example of how to use the function
matching_ids = find_ids_within_ten_percentage_threshold(df, 1001404)
print(matching_ids)


# 12)

import pandas as pd

def calculate_toll_rate(df):
    # Define the rate coefficients for each vehicle type
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    
    # Multiply each vehicle type column by its corresponding coefficient
    df['moto_rate'] = df['moto'] * rate_coefficients['moto']
    df['car_rate'] = df['car'] * rate_coefficients['car']
    df['rv_rate'] = df['rv'] * rate_coefficients['rv']
    df['bus_rate'] = df['bus'] * rate_coefficients['bus']
    df['truck_rate'] = df['truck'] * rate_coefficients['truck']
    
    return df
df = pd.DataFrame({
    'id_start': [1001400]*10,
    'id_end': [1001402, 1001404, 1001406, 1001408, 1001410, 1001412, 1001414, 1001416, 1001418, 1001420],
    'moto': [7.76, 23.92, 36.72, 54.08, 62.96, 75.44, 90.00, 100.56, 111.44, 121.76],
    'car': [11.64, 35.88, 55.08, 81.12, 94.44, 113.16, 135.00, 150.84, 167.16, 182.64],
    'rv': [14.55, 44.85, 68.85, 101.40, 118.05, 141.45, 168.75, 188.55, 208.95, 228.30],
    'bus': [21.34, 65.78, 100.98, 148.72, 173.14, 207.46, 247.50, 276.54, 306.46, 334.84],
    'truck': [34.92, 107.64, 165.24, 243.36, 283.32, 339.48, 405.00, 452.52, 501.48, 547.92]
})

df_with_rates = calculate_toll_rate(df)
print(df_with_rates)

#13)

