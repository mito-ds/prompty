import json
import pandas as pd
from typing import Callable, TypedDict, List, Optional, Any, TypedDict

class Prompt(TypedDict):
    prompt_name: str
    prompt_function: Callable[[List[str], List[pd.DataFrame], Any, str], str]

def get_column_description(df: pd.DataFrame, include_data=False) -> str:
    column_descriptions = []
    for col in df.columns:
        column_descriptions.append({
            'column name': str(col), # TODO: we should do this as a transpiled string?
            'dtype': str(df[col].dtype)
        })

        if include_data:
            column_descriptions[-1]['column values'] = str(list(df[col].head(5).values))
            
    return json.dumps(column_descriptions)


def get_description_of_dataframe(df_name: str, df: pd.DataFrame, include_data=False) -> str:
    return f"""
    Description of dataframe {df_name}:
    ```
    {get_column_description(df, include_data=False)}
    ```
    """

def get_prompts() -> List[Prompt]:
    return [
        {
            'prompt_name': 'sketch_prompt_with_df_names_only',
            'prompt_function': get_prompt_sketch_with_df_names_only,
        },
        {
            'prompt_name': 'sketch_prompt_with_columns_and_dtypes',
            'prompt_function': get_prompt_sketch_with_columns_and_dtypes,
        },
        {
            'prompt_name': 'sketch_prompt_with_column_and_dtypes_and_first_5_data',
            'prompt_function': get_prompt_sketch_with_columns_and_dtypes_and_first_5_data,
        },
    ] 

def get_prompt_sketch_with_df_names_only(df_names: List[str], dfs: List[pd.DataFrame], current_selection: Any, user_input: str):
    return f"""
    The user wants to edit the pandas dataframes {df_names}. They want to: {user_input}

    The Python code to make this transformation:
    ```
    """

def get_prompt_sketch_with_columns_and_dtypes(df_names: List[str], dfs: List[pd.DataFrame], current_selection: Any, user_input: str):
    df_descriptions = []
    for df_name, df in zip(df_names, dfs):
        df_descriptions.append(get_description_of_dataframe(df_name, df))

    new_line = '\n'
    return f"""
    The user wants to edit the pandas dataframes {df_names}. They want to: {user_input}
    {new_line.join(df_descriptions)}

    The Python code to make this transformation:
    ```
    """

def get_prompt_sketch_with_columns_and_dtypes_and_first_5_data(df_names: List[str], dfs: List[pd.DataFrame], current_selection: Any, user_input: str):
    df_descriptions = []
    for df_name, df in zip(df_names, dfs):
        df_descriptions.append(get_description_of_dataframe(df_name, df, include_data=True))

    new_line = '\n'
    return f"""
    The user wants to edit the pandas dataframes {df_names}. They want to: {user_input}
    {new_line.join(df_descriptions)}

    The Python code to make this transformation:
    ```
    """

def get_prompt_function(df_names: List[str], dfs: List[pd.DataFrame], current_selection: Any, user_input: str):
    param_descriptions = []
    for df_name, df in zip(df_names, dfs):
        param_descriptions.append(f'            - {df_name} (pd.DataFrame): {get_column_description(df)}')

    new_line = '\n'
    return f"""
    def transform({', '.join(df_names)}):
        '''
        This function {user_input}

        Parameters:
            {new_line.join(param_descriptions)}
        '''
    ```
    """