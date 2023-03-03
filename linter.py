import os
import pylint.lint

# Define the path to the Python file you want to evaluate
file_path = os.path.join(os.getcwd(), './public/ResponseFiles/response1.py')

# Define the Pylint command-line arguments
args = [
    #'--rcfile=pylintrc',  # Path to a Pylint configuration file
    '--output-format=text',  # Output format (text or colorized)
    file_path,  # Path to the Python file to evaluate
]

# Run Pylint on the Python file
pylint.lint.Run(args, do_exit=False).linter.stats


# Print the evaluation results
#print(f"Total score: {pylint_output('global_note')}")

# for category, score, count in pylint_output.get('by_category'):
#     print(f"{category.title()} - Score: {score:.2f}, Count: {count}")