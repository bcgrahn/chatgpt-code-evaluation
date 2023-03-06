import pylint.lint
import os
import time
import big_o
import ast
import coverage
import io
#import memory_profiler
import time
import radon
from radon.complexity import cc_visit, cc_rank
from radon.metrics import mi_visit
import radon.complexity as radon_cc

#cyclomatic complexity, code coverage, memory usage, and execution time in python

class CodeEvaluation:

    def evaluateLint(fileNames):
        evaluations = []
        folder_path = "./public/ResponseFiles"
        # Run pylint on the file and capture the output
        i = 1
        for filename in fileNames:

            num = str(i)

            short_path = f'./public/ResponseFiles/{filename}'

            file_path = os.path.join(os.getcwd(), short_path)

            output_path = f'--output=./public/LintEvaluations/lintEvaluations{num}.txt'
            
            i = i + 1

            # Define the Pylint command-line arguments
            args = [
                #'--rcfile=pylintrc',  # Path to a Pylint configuration file
                output_path,
                '--msg-template={msg_id}: {category}: {line:3d},{column}: {obj}: {msg} ',  # Output format (text or colorized)
                file_path,  # Path to the Python file to evaluate
            ]

            try:
                print("\n[Lint evalutation] " + filename)
                pylint.lint.Run(args)
            except:
                #print("[Unable to evaluate lint] " + filename)
                print('')
    
    def complexity(fileNames):
        complexEvaluations = []
        folder_path = "./public/ResponseFiles"
        pylint_stdout = ""
        # Run pylint on the file and capture the output
        for filename in fileNames:

            # Define the path to the Python file
            file_path = f'./public/ResponseFiles/{filename}'

            # Get the cyclomatic complexity of the file
            with open(file_path, 'r') as file:
                file_contents = file.read()
                cc = radon_cc.cc_visit(file_contents)
                print(f'Cyclomatic complexity: {cc}')

            # Get the cognitive complexity of the file
            with open(file_path, 'r') as file:
                file_contents = file.read()
                cognitive_cc = radon_cc.cc_visit(file_contents)
                print(f'Cognitive complexity: {cognitive_cc}')

            complexEvaluations.append(pylint_stdout)
        return complexEvaluations
    
    def timeEvaluate(fileNames):
        timeEvaluations = []
        folder_path = "./public/ResponseFiles"
        for filename in fileNames:
            file_path = os.path.join(folder_path, filename)
            start_time = time.time()
            # your algorithm here
            command = f"python {file_path}"
            os.system(command)

            end_time = time.time()
            timeEvaluations.append(end_time-start_time)

            print("[Evaluate execution time] " + str(end_time-start_time))

        return timeEvaluations
    
    # def timeComplexity(fileNames):
    #     folder_path = "./public/ResponseFiles"
    #     bigOEvaluations = []
    #     for filename in fileNames:
    #        print()
    #       # https://pypi.org/project/big-O/
           
    #         # bigOEvaluations.append(start_time - end_time)
    #     return bigOEvaluations
    
    # def analyze_code(fileNames):
    #     folder_path = "./public/ResponseFiles"
    #     breakdownEvaluations =  []
    #     for filename in fileNames:

    #         print("[Code breakdown] " + filename )
    #         file_path = os.path.join(folder_path, filename)
    #         # Load the code from the file
    #         with open(file_path, 'r') as f:
    #             code = f.read()

    #         # Parse the code into an AST
    #         tree = ast.parse(code)

    #         # Traverse the AST and extract relevant information
    #         function_names = []
    #         variable_names = []
    #         for node in ast.walk(tree):
    #             if isinstance(node, ast.FunctionDef):
    #                 function_names.append(node.name)
    #             elif isinstance(node, ast.Name):
    #                 variable_names.append(node.id)

    #         # Calculate metrics
    #         num_functions = len(function_names)
    #         num_variables = len(variable_names)

    #         # Report the results
    #         result = f"File: {filename}/nNumber of functions: {num_functions}/nNumber of variables: {num_variables}"
    #         breakdownEvaluations.append(result)
        
    #     return breakdownEvaluations

# Analyze all Python files in a directory
# directory = 'path/to/directory'
# for filename in os.listdir(directory):
#     if filename.endswith('.py'):
#         analyze_code(os.path.join(directory, filename))
