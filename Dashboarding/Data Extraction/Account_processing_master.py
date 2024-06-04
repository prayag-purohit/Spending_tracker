#Run both the files in Credit and Current repositories
import subprocess

# Define the paths to the Python scripts in other directories
credit_script_path = r"E:\Data analytics projects\Financial Tracker\Dashboarding\Data Extraction\Credit\Credit Data processing.py"
current_script_path = r"E:\Data analytics projects\Financial Tracker\Dashboarding\Data Extraction\Current\Current Data processing.py"

# Run the 'credit' script
print("Running Credit Data processing.py:")
credit_output = subprocess.run(['python', credit_script_path], capture_output=True, text=True)
print(credit_output.stdout)

# Run the 'current' script
print("\nRunning Current Data processing.py:")
current_output = subprocess.run(['python', current_script_path], capture_output=True, text=True)
print(current_output.stdout)


#Combine data from account master files
import pandas as pd


#Process data for machine learning, and add other data visualization needs
#Run deduplication and other checks
