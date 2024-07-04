import pandas as pd

def remove_duplicates(input_file: str, output_file: str):
    # Read the text file into a DataFrame
    df = pd.read_csv(input_file, header=None, names=['User'])

    # Remove duplicate names
    df_unique = df.drop_duplicates()

    # Save the unique names to a new text file
    df_unique.to_csv(output_file, index=False, header=False)