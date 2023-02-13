import argparse
import os
import time
from typing import Any, Optional

import openai
from prompty.completions import get_completion

from prompty.prompt import get_prompts
from prompty.io_utils import load_run_id, save_test_instance_to_disk
from prompty.tests import get_tests


def evaludate_prompts_with_test_cases(prompt_name: Optional[str], test_case_name: Optional[str]):
    openai.organization = "org-mZuyZRhv2RgkFivSEaOGeheQ"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    run_id = f'run-{time.time()}'
    prompts = get_prompts()
    tests = get_tests()

    for prompt in prompts:
        if prompt_name is not None and prompt['prompt_name'] != prompt_name:
            continue

        for test in tests:
            if test_case_name is not None and test['test_case_name'] != test_case_name:
                continue

            prompt_string = prompt['prompt_function'](test['df_names'], test['input_dfs'], test['selection'], test['user_input'])

            completion = get_completion(prompt_string)

            save_test_instance_to_disk(
                run_id,
                prompt,
                test,
                prompt_string,
                completion
            )


def main():

    parser = argparse.ArgumentParser(
        prog = 'prompty',
        description = 'A tool for iteratively designing codex prompts.',
    )
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')
    
    # Create the parser for the evaluate command
    parser_eval = subparsers.add_parser('eval', help='Run the evaluation loop on currently defined prompts and test cases.')
    parser_eval.add_argument('--prompt-name', help='If you only want to test a single prompt, pass it here', required=False)
    parser_eval.add_argument('--test-case-name', help='If you only want to run a single test case, pass it here', required=False)
   
    # Create the parser for the load command
    parser_load = subparsers.add_parser('load', help='Load a specific test run by run id.')
    parser_load.add_argument('--run-id', help='The specific run id to load. If this is empty, will load the most recent run by default', required=False)
    parser_load.add_argument('--outfile', help='Where to write the dataframe', required=False)
    parser_load.add_argument('-s', '--short', help='If you only want the prompt_name, test_case_name, and completion', action='store_true')

    args = parser.parse_args()
    if args.command == 'eval':
        evaludate_prompts_with_test_cases(args.prompt_name, args.test_case_name)
    elif args.command == 'load':
        run_df = load_run_id(args.run_id)
        print(args)
        if args.short:
            run_df = run_df[['prompt_name','test_case_name','full_completion']]

        if args.outfile is not None:
            run_df.to_csv(args.outfile, index=False)

        print(run_df)

if __name__ == '__main__':
    main()