import pandas as pd

# Read the text file into a DataFrame
df = pd.read_csv('users.txt', header=None, names=['User'])

# Remove duplicate names
df_unique = df.drop_duplicates()

# Save the unique names to a new text file
df_unique.to_csv('unique_users.txt', index=False, header=False)