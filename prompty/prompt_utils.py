import pandas as pd

def get_dataframe_creation_code(df_name: str, df: pd.DataFrame, include_data=False) -> str:
    if include_data:
        return f'{df_name} = pd.DataFrame({df.head(5).to_dict("dict")})'
    else:
        return f'{df_name} = pd.DataFrame'