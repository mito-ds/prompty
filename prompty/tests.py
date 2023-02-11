import pandas as pd
from typing import TypedDict, List


class UserInputTestCase(TypedDict):
    test_case_name: str
    df_names: List[str]
    input_dfs: List[pd.DataFrame]
    user_input: str
    output_dfs: List[pd.DataFrame]


def get_tests() -> List[UserInputTestCase]:
    return [
        {
            'test_case_name': 'calculate revenue column',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]})],
            'user_input': 'calculate revenue column',
            'output_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99], 'revenue': [2 * 3.99, 4 * 3.99, 6 * 4.99, 8 * 4.99]})]
        },
        {
            'test_case_name': 'find and replace',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]})],
            'user_input': 'replace 1 with 2',
            'output_dfs': [pd.DataFrame({'id': [2, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]})]
        },
        {
            'test_case_name': 'conditional column transform',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]})],
            'user_input': 'if id is even, then double quantity',
            'output_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 8, 6, 16], 'price': [3.99, 3.99, 4.99, 4.99]})]
        },
        {
            'test_case_name': 'cleanup dtypes',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'date': ['12-22-1997', '12-23-1997', '12-23-1997'], 'is_finished': ['True', 'False', 'True'], 'count': ['1', '2.2', '3']})],
            'user_input': 'cleanup dtypes',
            'output_dfs': [pd.DataFrame({'date': pd.to_datetime(['12-22-1997', '12-23-1997', '12-23-1997']), 'is_finished': [True, False, True], 'count': [1.0, 2.2, 3.0]})]
        },
        {
            'test_case_name': 'vlookup merge',
            'df_names': ['df1', 'df2'],
            'input_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8]}), pd.DataFrame({'id': [1, 2, 3, 4], 'stock': [100, 200, 300, 400], 'price': [3.99, 3.99, 4.99, 4.99]})],
            'user_input': 'vlookup price',
            'output_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]}), pd.DataFrame({'id': [1, 2, 3, 4], 'stock': [100, 200, 300, 400], 'price': [3.99, 3.99, 4.99, 4.99]})]
        },
        {
            'test_case_name': 'pivoting who has the most',
            'df_names': ['df1', 'df2'],
            'input_dfs': [pd.DataFrame({'user_id': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'lemons': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]})],
            'user_input': 'which user has the most lemons',
            'output_dfs': [pd.DataFrame({'user_id': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'amount': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]})]
        },
    ]