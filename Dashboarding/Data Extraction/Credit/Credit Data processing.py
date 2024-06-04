import pandas as pd
import numpy as np
import os
import time
import shutil

# Define the directory path
directory_path = r"E:/Data analytics projects/Financial Tracker/Dashboarding/Data Extraction/Credit"

# Define the list of files and directories to ignore
ignore = [ 'Credit processed master.csv']
# List all files and directories in the specified directory
files_and_dirs = os.listdir(directory_path)
csv_files = [file for file in files_and_dirs if file.endswith('.csv')]

# Create a list to store the files and directories that are not in the ignore list
available_files = [item for item in csv_files if item not in ignore]

# Initialize the counter
i = 0

if len(available_files) > 0:
    print(f'There are {len(available_files)} current account files available...Processing')
    
    # Iterate over the available files
    for x in available_files:
        try:
            # Construct the current file path
            current_file_path = os.path.join(directory_path, x)
            
            # Read the CSV file
            df = pd.read_csv(current_file_path, header=None)
            
            # Process the DataFrame
            df.columns = ["Date", "Transaction_description", "Transaction_amount"]
            df = df[["Date", "Transaction_description", "Transaction_amount"]]
            df['Date'] = pd.to_datetime(df['Date'])
            df['Type'] = 'Credit Card'

            time.sleep(2)
            print('\nAppending file contents to the master file\n')
            
            # Append the dataframe to the master CSV file
            df.to_csv(r"E:/Data analytics projects/Financial Tracker/Dashboarding/Monthly Statements/Credit/Credit processed master.csv", mode='a', index=False, header=False)
            
            i += 1
            
            # Move the processed file to the 'Finished_processing' directory
            shutil.move(current_file_path, r"E:/Data analytics projects/Financial Tracker/Dashboarding/Monthly Statements/Credit/Finished_processing")
            time.sleep(2)

            print(f"File processed and moved to other directory \nNumber of files processed = {i}")
        
        except Exception as e:
            print(f"Error processing file {x}: {e}")

else:
    print('No files to process')