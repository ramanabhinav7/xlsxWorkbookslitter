import pandas as pd

def split_excel_to_sheets(input_file, output_prefix):
    # Read the Excel file into a Pandas DataFrame
    xl = pd.ExcelFile(input_file)
    
    # Iterate through each sheet in the Excel file
    for sheet_name in xl.sheet_names:
        # Read the current sheet into a DataFrame
        df = pd.read_excel(input_file, sheet_name=sheet_name)
        
        # Write the DataFrame to a new Excel file with a single sheet
        output_file = f"{output_prefix}_{sheet_name}.xlsx"
        df.to_excel(output_file, index=False)
        print(f"Sheet '{sheet_name}' has been saved to '{output_file}'")

# Example usage
input_file = "POPULAR_DAT_REQUIRED.xlsx"  # Replace with the path to your input Excel file
output_prefix = "output_sheet"  # Prefix for output file names
split_excel_to_sheets(input_file, output_prefix)
