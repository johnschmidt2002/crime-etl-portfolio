import os
import pandas as pd

def load_state_nibrs(state_code, base_path="raw_data/FBI NIBRS Crime Data 2021"):
    """
    Loads all CSVs for a given state's NIBRS folder (e.g., 'CA-2021').
    Returns a dictionary of DataFrames keyed by file name.
    """
    state_path = os.path.join(base_path, f"{state_code}-2021")

    if not os.path.exists(state_path):
        raise FileNotFoundError(f"No folder found for {state_code}-2021 at {state_path}")

    dataframes = {}
    for file in os.listdir(state_path):
        if file.endswith(".csv"):
            df_name = file.replace(".csv", "")
            csv_path = os.path.join(state_path, file)
            dataframes[df_name] = pd.read_csv(csv_path)
    return dataframes
