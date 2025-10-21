import pandas as pd


def read_from_csv(file: str, index: str | list[str], column: str):

    data_df = pd.read_csv(file)
    data_dict = data_df.set_index(index).to_dict()[column]

    return data_dict