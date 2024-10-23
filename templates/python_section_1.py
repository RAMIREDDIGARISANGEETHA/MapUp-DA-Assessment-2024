from typing import Dict, List

import pandas as pd


def reverse_by_n_elements(lst: list[int], n: int) -> list[int]:
    """
    Reverses the input list by groups of n elements.
    """
    # Your code goes here.
    for i in range(0, len(lst), n):
        # Reverse each chunk of size n manually
        left = i
        right = min(i + n - 1, len(lst) - 1)
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
    return lst
print(reverse_by_n_elements([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(reverse_by_n_elements([1, 2, 3, 4, 5], 2))
print(reverse_by_n_elements([10, 20, 30, 40, 50, 60, 70], 4))


def group_by_length(lst: List[str]) -> dict[int, list[str]]:
    """
    Groups the strings by their length and returns a dictionary.
    """
    # Your code here
     length_dict = {}
    for word in lst:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(word)

    # Sort the dictionary by keys (lengths)
    return dict(sorted(length_dict.items()))
print(group_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))
print(group_by_length(["one", "two", "three", "four"]))



def flatten_dict(nested_dict: dict, sep: str = '.') -> dict:
    """
    Flattens a nested dictionary into a single-level dictionary with dot notation for keys.
    
    :param nested_dict: The dictionary object to flatten
    :param sep: The separator to use between parent and child keys (defaults to '.')
    :return: A flattened dictionary
    """
    # Your code here
    def flatten(current_dict: Dict, parent_key: str = '') -> Dict:
        items = {}
        for key, value in current_dict.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.update(flatten(value, new_key))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    list_key = f"{new_key}[{i}]"
                    if isinstance(item, dict):
                        items.update(flatten(item, list_key))
                    else:
                        items[list_key] = item
            else:
                items[new_key] = value
        return items

    return flatten(nested_dict)

# Example 
nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

# Flattened dictionary
flattened_dict = flatten_dict(nested_dict)

# Print the flattened dictionary
print(flattened_dict)
    
from itertools import permutations
def unique_permutations(nums: List[int]) -> list[list[int]]:
    """
    Generate all unique permutations of a list that may contain duplicates.
    
    :param nums: List of integers (may contain duplicates)
    :return: List of unique permutations
    """
    # Your code here
    return [list(p) for p in set(permutations(nums))]

# Example Usage
input_list = [1, 1, 2]
output = unique_permutations(input_list)
print(output)


import re
def find_all_dates(text: str) -> list[str]:
    """
    This function takes a string as input and returns a list of valid dates
    in 'dd-mm-yyyy', 'mm/dd/yyyy', or 'yyyy.mm.dd' format found in the string.
    
    Parameters:
    text (str): A string containing the dates in various formats.

    Returns:
    List[str]: A list of valid dates in the formats specified.
    """
    dd_mm_yyyy_pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    mm_dd_yyyy_pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    yyyy_mm_dd_pattern = r'\b\d{4}\.\d{2}\.\d{2}\b'
    
    # Finding the matches for each pattern separately
    dates_dd_mm_yyyy = re.findall(dd_mm_yyyy_pattern, text)
    dates_mm_dd_yyyy = re.findall(mm_dd_yyyy_pattern, text)
    dates_yyyy_mm_dd = re.findall(yyyy_mm_dd_pattern, text)
    
    # Combine all matches into a single list
    all_dates = dates_dd_mm_yyyy + dates_mm_dd_yyyy + dates_yyyy_mm_dd
    
    return all_dates

# Example 
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
output = find_all_dates(text)
print(output)


def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.
    
    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """
    return pd.Dataframe()


def rotate_and_multiply_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Rotate the given matrix by 90 degrees clockwise, then multiply each element 
    by the sum of its original row and column index before rotation.
    
    Args:
    - matrix (List[List[int]]): 2D list representing the matrix to be transformed.
    
    Returns:
    - List[List[int]]: A new 2D list representing the transformed matrix.
    """
    # Your code here
    from typing import List

#  Rotate the matrix by 90 degrees clockwise
def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    # Rotating the matrix by taking elements from the last row to the first column
    rotated_matrix = [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
    return rotated_matrix

# Transform the matrix
def transform_matrix(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    transformed_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # Calculate the sum of all elements in the same row and column, excluding the current element
            row_sum = sum(matrix[i]) - matrix[i][j]
            col_sum = sum(matrix[k][j] for k in range(n)) - matrix[i][j]
            transformed_matrix[i][j] = row_sum + col_sum
    
    return transformed_matrix

# Main function to rotate and transform the matrix
def rotate_and_transform_matrix(matrix: list[list[int]]) -> list[list[int]]:
    # Step 1: Rotate the matrix
    rotated_matrix = rotate_matrix(matrix)
    
    # Step 2: Transform the matrix by replacing each element with the sum of row and column excluding itself
    transformed_matrix = transform_matrix(rotated_matrix)
    
    return transformed_matrix

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
final_matrix = rotate_and_transform_matrix(matrix)

# Display the result
for row in final_matrix:
    print(row)



def time_check(df) -> pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    # Group by (id, id_2)
    grouped = df.groupby(['id', 'id_2'])

    # Create an empty dictionary to store the result
    result = {}

    for (id_val, id_2_val), group in grouped:
        # Get all unique days of the week
        unique_days = group['start'].dt.dayofweek.unique()  # 0=Monday, ..., 6=Sunday

        # Check if all 7 days (0 to 6) are present
        full_week_covered = len(unique_days) == 7

        # Check if the timestamps cover a full 24-hour period
        start_min = group['start'].min().normalize()  # Earliest start time
        end_max = group['end'].max().normalize() + pd.Timedelta(days=1)  # Latest end time, adjusted for the next day

        # Check if the total period covers at least 7 days and a full 24 hours
        full_24_hour_coverage = (end_max - start_min) >= pd.Timedelta(days=7)

        # Add to the result dictionary
        result[(id_val, id_2_val)] = not (full_week_covered and full_24_hour_coverage)

    # Convert the result dictionary to a Pandas Series with a MultiIndex
    return pd.Series(result)
