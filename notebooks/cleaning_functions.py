import pandas as pd
import re
import numpy as np

# FUNCTIONS AVAILABLE :
#     drop_columns
#     clean_column_names
#     value_snake_case
#     extract_number
#     categorize_rating
#     lowercase_categories
#     split_category

#     replace_organisation_size
#     clean_country_column
#     convert_ransom_cost_to_numeric
#     ensure_numeric_finite

#################################################
def drop_columns(df, columns_to_drop):
    """
    Drops the specified columns from a DataFrame.
    
    Parameters:
    df (DataFrame): The input DataFrame
    columns_to_drop (list): A list of column names to be dropped
    
    Returns:
    DataFrame: The DataFrame with the specified columns dropped
    
    Example:
    df = drop_columns(df,'description ')
    """
    
    # Drop the specified columns from the DataFrame
    df = df.drop(columns=columns_to_drop)
    
    return df

#################################################

def clean_column_names(df):
    """
    Cleans column names of a DataFrame by converting to lowercase, replacing spaces with underscores,
    and removing special characters and symbols.
    
    Parameters:
    df (DataFrame): The input DataFrame
    
    Returns:
    DataFrame: The DataFrame with cleaned column names
    
    exemple:
    df = clean_column_names(df)
    """
    
    # Convert column names to lowercase
    lowercase = lambda x: x.lower()
    df = df.rename(columns=lowercase)
    
    # Replace spaces with underscores in column names
    replace_func = lambda x: x.replace(' ', '_')
    df = df.rename(columns=replace_func)
    
    # Remove special characters and symbols from column names
    pattern = r"[^\w\s]"
    df.columns = [re.sub(pattern, '', col) for col in df.columns]
    
    return df

#################################################
def value_snake_case(dataframe, columns):
    """
    Convert all values in specified column(s) of a DataFrame to snake case.

    Parameters:
    dataframe (pd.DataFrame): The dataFrame to be modified.
    columns (str or list): The column whose values are to be comverted. Can be a single column or a list.

    Returns:
    pd.DataFrame: A DataFrame with the values in specified columns converted tosnake case.
    
    Examples :
    df = value_snake_case(df, 'column_name') 
    df = value_snake_case(df, ['column1', 'column2', 'column3']) 
    """

    # Ensure columns is a list
    if isinstance(columns, str):
        columns = [columns]

    # Function to convert a string to snake case
    def convert_to_snake_case(s):
        # Replace all non-word characters (except spaces) with ''
        s = re.sub(r'[^\w\s]', '', s)
        # Replace all spaces and underscores with a single underscore
        s = re.sub(r'[\s_]+', '_', s.lower())
        return s

    # Apply the conversion to each specified column
    for col in columns:
        if col in dataframe.columns:
            dataframe[col] = dataframe[col].astype(str).apply(convert_to_snake_case)

    return dataframe


#################################################
def extract_number(value):
    """
    Extracts a numerical value from the input. Returns np.nan if no valid number can be extracted.
    """
    if isinstance(value, str):
        match = re.search(r'\d+\.\d+', value)
        return float(match.group()) if match else np.nan
    elif isinstance(value, float):
        return value
    else:
        return np.nan

#################################################
def categorize_rating(value):
    """
    Categorizes a rating into 'negative', 'neutral', or 'positive'. Returns 'Invalid rating' for ratings outside the expected range.
    """
    if value >= 0 and value <= 2.999:
        return 'negative'
    elif value >= 3 and value <= 3.999:
        return 'neutral'
    elif value >= 4 and value <= 5:
        return 'positive'
    else:
        return 'Invalid rating'

#################################################
def lowercase_categories(df):
    """
    Converts all values in the 'category' column to lowercase.
    """
    df['category'] = df['category'].str.lower()
    return df

#################################################

def split_category(df):
    """
    Splits the 'category' column at each '/' and adds new columns.
    """
    # Split the 'category' column at each '/'
    split_df = df['category'].str.split('/', expand=True)

    # Add the new columns to the original DataFrame
    df = pd.concat([df, split_df], axis=1)

    return df

#################################################

