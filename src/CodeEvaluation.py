import pylint.lint

class CodeEvaluation:

   # Run(['--errors-only', 'myfile.py'])

    # Define the name of the file to analyze

    def evaluate(fileNames):
        # Run pylint on the file and capture the output
        for filename in fileNames:
            print("[Evaluate] " + filename)
            pylint_output = pylint.lint.Run(["--disable=all", "--enable=error", filename], do_exit=False).linter.stats["global_note"]
            # Print the output
            # print(pylint_output)