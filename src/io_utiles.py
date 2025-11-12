import pandas as pd

def load_csv_file(csv_path: str, clean: bool = False ):

    """
    Return csv file as a Dataframe.
    if clean = true return a cleand version, else return umodified version.
    """

    df = pd.read_csv(csv_path)
    df_clean = df.dropna().drop_duplicates().reset_index(drop=True)

    if clean == True:
        return df_clean
    else:
        return df
 