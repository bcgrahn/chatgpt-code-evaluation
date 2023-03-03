import pylint.lint
import os
import time
import big_o
import ast
import coverage
import io
#import memory_profiler
import time

#cyclomatic complexity, code coverage, memory usage, and execution time in python

class CodeEvaluation:

    def evaluate(fileNames):
        evaluations = []
        folder_path = "./public/ResponseFiles"
        pylint_stdout = ""
        # Run pylint on the file and capture the output
        for filename in fileNames:
            file_path = os.path.join(folder_path, filename)
            output = io.StringIO()
            try:
                print("\n[Lint evalutation] " + filename)
                pylint_opts = ['--disable=missing-docstring']
                temp = pylint.lint.Run(pylint_opts + [file_path])
            except:
                #print("[Unable to evaluate lint] " + filename)
                print()

            evaluations.append(pylint_stdout)
        return evaluations
    
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
    
    def bigOEvaluate(fileNames):
        folder_path = "./public/ResponseFiles"
        bigOEvaluations = []
        for filename in fileNames:
           print()
          # https://pypi.org/project/big-O/
           
            # bigOEvaluations.append(start_time - end_time)
        return bigOEvaluations
    
    def analyze_code(fileNames):
        folder_path = "./public/ResponseFiles"
        breakdownEvaluations =  []
        for filename in fileNames:

            print("[Code breakdown] " + filename )
            file_path = os.path.join(folder_path, filename)
            # Load the code from the file
            with open(file_path, 'r') as f:
                code = f.read()

            # Parse the code into an AST
            tree = ast.parse(code)

            # Traverse the AST and extract relevant information
            function_names = []
            variable_names = []
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    function_names.append(node.name)
                elif isinstance(node, ast.Name):
                    variable_names.append(node.id)

            # Calculate metrics
            num_functions = len(function_names)
            num_variables = len(variable_names)

            # Report the results
            result = f"File: {filename}/nNumber of functions: {num_functions}/nNumber of variables: {num_variables}"
            breakdownEvaluations.append(result)
        
        return breakdownEvaluations

# Analyze all Python files in a directory
# directory = 'path/to/directory'
# for filename in os.listdir(directory):
#     if filename.endswith('.py'):
#         analyze_code(os.path.join(directory, filename))
