
import pandas as pd
from typing import Any, List, Optional, TypedDict

class Selection(TypedDict):
    selected_df_name: str
    selected_columns: List[Any]
    selected_rows: List[Any]

class UserInputTestCase(TypedDict):
    test_case_name: str
    df_names: List[str]
    input_dfs: List[pd.DataFrame]
    selection: Optional[Selection]
    user_input: str
    output_dfs: List[pd.DataFrame]

class TestResultSaveFormat(TypedDict):
    prompt_name: str
    test_case_name: str
    prompt_string: str
    completion: str
    error: str