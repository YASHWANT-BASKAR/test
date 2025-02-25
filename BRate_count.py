# Import the pandas library
import pandas as pd

# Specify the file path - update this to the actual file path on your system
file_path = r"C:\Users\yashw\Downloads\True_11_25_02_25_MD_new.csv" # Replace with the path to your CSV file

# Load the CSV data into a pandas DataFrame
data = pd.read_csv(file_path)

# Count the occurrences of each unique value in the 'BRate' column
brate_counts = data['BRate'].value_counts()

# Display the counts in the terminal
print("BRate Value Counts:")
print(brate_counts)

# Optional: Save the output to a new CSV file if needed
brate_counts.to_csv('BRate_counts_.csv', header=['Count'])
