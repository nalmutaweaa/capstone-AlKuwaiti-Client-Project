import pandas as pd

#function to read data
def load_data(data, sheet=0): #takes the first sheet as defult if user did not specify
    if data.name.endswith(".csv"):
        df= pd.read_csv(data)
    elif data.name.endswith(".xlsx"):
        df= pd.read_excel(data, sheet_name=sheet)
    return df


