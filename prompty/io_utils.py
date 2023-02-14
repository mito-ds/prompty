
import json
import os
from typing import Any, Optional

import pandas as pd

from prompty.prompt import Prompt
from prompty.types import TestResultSaveFormat, UserInputTestCase

TEST_CASE_FOLDER = 'outputs/'

def save_test_instance_to_disk(run_id: str, prompt: Prompt, test_case: UserInputTestCase, prompt_string: str, completion_or_error: Any) -> None:
    
    # Create the output folder if it does not exist
    if not os.path.exists(TEST_CASE_FOLDER):
        os.mkdir(TEST_CASE_FOLDER)

    # Then, create a folder for this test sequence
    run_id_folder = os.path.join(TEST_CASE_FOLDER, run_id)
    if not os.path.exists(run_id_folder):
        os.mkdir(run_id_folder)

    # Then, make a folder for each prompt
    prompt_folder = os.path.join(run_id_folder, prompt['prompt_name'])
    if not os.path.exists(prompt_folder):
        os.mkdir(prompt_folder)

    test_result: TestResultSaveFormat = {
        'prompt_name': prompt['prompt_name'],
        'test_case_name': test_case['test_case_name'],
        'prompt_string': prompt_string,
        'completion': completion_or_error if not isinstance(completion_or_error, Exception) else '',
        'error': str(completion_or_error) if isinstance(completion_or_error, Exception) else ''
    }

    # Then, finially write the file for this test result
    test_result_file = os.path.join(prompt_folder, test_case['test_case_name'] + '.txt')
    with open(test_result_file, 'w') as f:
        f.write(json.dumps(test_result))
    

def load_run_id(run_id: Optional[str], short=False) -> pd.DataFrame:

    if run_id is not None:
        run_id_folder = os.path.join(TEST_CASE_FOLDER, run_id)
    else:
        # If no run id is passed, just look at the most recent run id
        all_subdirs = [os.path.join(TEST_CASE_FOLDER, d) for d in os.listdir(TEST_CASE_FOLDER)]
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        run_id_folder = latest_subdir

    test_result_paths = [os.path.join(dp, f) for dp, dn, filenames in os.walk(run_id_folder) for f in filenames if os.path.splitext(f)[1] == '.txt']

    test_results = []
    for test_result_path in test_result_paths:
        with open(test_result_path, 'r') as f:
            test_result = json.loads(f.read())
            if test_result['completion'] != '':
                test_result['full_completion'] = test_result['completion']['choices'][0]['text']
            else:
                test_result['full_completion'] = ''
            test_results.append(test_result)

    run_df = pd.DataFrame(test_results)

    if short:
        run_df = run_df[['prompt_name','test_case_name','full_completion', 'error']]

    return run_df