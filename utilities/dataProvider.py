import os

import pandas as pd


def get_data(sheetName, fileName="testdata.xlsx"):
    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )  # Directory where configReader.py is located
    EXCEL_PATH = os.path.join(BASE_DIR, "..", "exceldata", fileName)

    # Read the entire sheet into a DataFrame
    df = pd.read_excel(EXCEL_PATH, sheet_name=sheetName, header=0)

    # Convert to list of lists (excluding header row)
    # dropna(how='all') removes rows where ALL values are NaN
    # values.tolist() converts to list of lists
    mainList = df.dropna(how="all").values.tolist()

    return mainList
