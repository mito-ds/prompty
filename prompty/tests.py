import pandas as pd
from typing import List

from prompty.types import UserInputTestCase

def get_tests() -> List[UserInputTestCase]:
    return [
        {
            'test_case_name': 'calculate revenue column',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]})],
            'user_input': 'calculate revenue column',
            'selection': None,
            'output_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99], 'revenue': [2 * 3.99, 4 * 3.99, 6 * 4.99, 8 * 4.99]})]
        },
        {
            'test_case_name': 'find and replace',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]})],
            'user_input': 'replace 1 with 2',
            'selection': None,
            'output_dfs': [pd.DataFrame({'id': [2, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]})]
        },
        {
            'test_case_name': 'conditional column transform',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]})],
            'user_input': 'if id is even, then double quantity',
            'selection': None,
            'output_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 8, 6, 16], 'price': [3.99, 3.99, 4.99, 4.99]})]
        },
        {
            'test_case_name': 'cleanup dtypes',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'date': ['12-22-1997', '12-23-1997', '12-23-1997'], 'is_finished': ['True', 'False', 'True'], 'count': ['1', '2.2', '3']})],
            'user_input': 'cleanup dtypes',
            'selection': None,
            'output_dfs': [pd.DataFrame({'date': pd.to_datetime(['12-22-1997', '12-23-1997', '12-23-1997']), 'is_finished': [True, False, True], 'count': [1.0, 2.2, 3.0]})]
        },
        {
            'test_case_name': 'vlookup merge',
            'df_names': ['df1', 'df2'],
            'input_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8]}), pd.DataFrame({'id': [1, 2, 3, 4], 'stock': [100, 200, 300, 400], 'price': [3.99, 3.99, 4.99, 4.99]})],
            'user_input': 'vlookup price',
            'selection': None,
            'output_dfs': [pd.DataFrame({'id': [1, 2, 3, 4], 'quantity': [2, 4, 6, 8], 'price': [3.99, 3.99, 4.99, 4.99]}), pd.DataFrame({'id': [1, 2, 3, 4], 'stock': [100, 200, 300, 400], 'price': [3.99, 3.99, 4.99, 4.99]})]
        },
        {
            'test_case_name': 'pivoting who has the most',
            'df_names': ['df1', 'df2'],
            'input_dfs': [pd.DataFrame({'user_id': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'lemons': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]})],
            'user_input': 'which user has the most lemons',
            'selection': None,
            'output_dfs': [pd.DataFrame({'user_id': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'lemons': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]})]
        },
        {
            'test_case_name': 'delete selected column',
            'df_names': ['df1', 'df2'],
            'input_dfs': [pd.DataFrame({'user_id': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'lemons': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]}), pd.DataFrame({'user_id': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'melons': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]})],
            'user_input': 'delete selected columns',
            'selection': {'selected_df_name': 'df2', 'selected_columns': ['user_id'], 'selected_rows': []},
            'output_dfs': [pd.DataFrame({'user_id': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'lemons': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]}), pd.DataFrame({'melons': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]})]
        },
        {
            'test_case_name': 'rename headers to lowercase',
            'df_names': ['df1', 'df2'],
            'input_dfs': [pd.DataFrame({'USER_ID': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'LEMONS': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]}), pd.DataFrame({'USER_ID': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'MELONS': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]})],
            'user_input': 'rename all columns to lowercase',
            'selection': {'selected_df_name': 'df2', 'selected_columns': ['user_id'], 'selected_rows': []},
            'output_dfs': [pd.DataFrame({'USER_ID': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'LEMONS': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]}), pd.DataFrame({'user_id': [1, 2, 1, 4, 5, 3, 7, 7, 4, 2, 1], 'melons': [100, 200, 1, 3, 4, 123, 12, 23, 412, 23, 1]})],
        },
        {
            'test_case_name': 'format as percentages',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'user_id': [1, 2, 3, 4], 'time_online': [.2, .4, .9, .10]})],
            'user_input': 'format as percentage',
            'selection': {'selected_df_name': 'df1', 'selected_columns': ['time_online'], 'selected_rows': []},
            'output_dfs': [pd.DataFrame({'user_id': [1, 2, 3, 4], 'time_online': [.2, .4, .9, .10]})],
        },
        {
            'test_case_name': 'create a graph',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'user_id': [1, 2, 3, 4], 'time_online': [.2, .4, .9, .10]})],
            'user_input': 'graph user id vs. time online',
            'selection': {'selected_df_name': 'df1', 'selected_columns': ['time_online'], 'selected_rows': []},
            'output_dfs': [pd.DataFrame({'user_id': [1, 2, 3, 4], 'time_online': [.2, .4, .9, .10]})],
        },
        {
            'test_case_name': 'import: recent csv',
            'df_names': [],
            'input_dfs': [],
            'user_input': 'import most recent csv from current folder',
            'selection': None,
            'output_dfs': [], # TODO
        },
        {
            'test_case_name': 'import: from GPT knowledge',
            'df_names': [],
            'input_dfs': [],
            'user_input': 'create dataframe with fortune 10 companies',
            'selection': None,
            'output_dfs': [], # TODO
        },
        {
            'test_case_name': 'export: excel',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'user_id': [1, 2, 3, 4], 'time_online': [.2, .4, .9, .10]})],
            'user_input': 'download to excel',
            'selection': {'selected_df_name': 'df1', 'selected_columns': ['time_online'], 'selected_rows': []},
            'output_dfs': [pd.DataFrame({'user_id': [1, 2, 3, 4], 'time_online': [.2, .4, .9, .10]})],
        },
        {
            'test_case_name': 'export: email',
            'df_names': ['df1'],
            'input_dfs': [pd.DataFrame({'user_id': [1, 2, 3, 4], 'time_online': [.2, .4, .9, .10]})],
            'user_input': 'send df1 in email',
            'selection': {'selected_df_name': 'df1', 'selected_columns': ['time_online'], 'selected_rows': []},
            'output_dfs': [pd.DataFrame({'user_id': [1, 2, 3, 4], 'time_online': [.2, .4, .9, .10]})],
        },
        # TODO: on top of specified tests, do tests with massive dataframes:
            # lots of columns
            # lots of rows
            # huge pieces of data in the dataframe
    ]