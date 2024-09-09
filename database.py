# import pandas as pd

# # Load the dataset
# try:
#     df = pd.read_csv('data_pred.csv', quotechar='"', delimiter=',', skipinitialspace=True, on_bad_lines='skip')
# except pd.errors.ParserError as e:
#     print(f"Error reading the CSV file: {e}")
#     df = None

# def get_reaction_details(reaction):
#     if df is not None:
#         details = df[df['Equation'].str.replace(" ", "") == reaction.replace(" ", "")].to_dict(orient='records')
#         if details:
#             return details[0]
#         else:
#             return {}
#     else:
#         return {}

# # Test get_reaction_details
# if __name__ == "__main__":
#     test_reaction = '4Al + 3Br2 -> 2Al2Br6'
#     print(get_reaction_details(test_reaction))
#---------------------------------------------------------------------------------------------
import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('data_pred.csv', quotechar='"', delimiter=',', skipinitialspace=True, on_bad_lines='skip')
except pd.errors.ParserError as e:
    print(f"Error reading the CSV file: {e}")
    df = None

def get_reaction_details(reaction):
    if df is not None:
        details = df[df['Reaction'].str.replace(" ", "").str.lower() == reaction.replace(" ", "").lower()].to_dict(orient='records')
        if details:
            return details[0]
        else:
            return {}
    else:
        return {}

# Test get_reaction_details
if __name__ == "__main__":
    test_reaction = '4Al + 3Br2'
    print(get_reaction_details(test_reaction))

