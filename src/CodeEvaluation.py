from pylint import epylint as lint
class CodeEvaluation:

   # Run(['--errors-only', 'myfile.py'])

    # Define the name of the file to analyze

    def evaluate(fileNames):

        evaluations = []
        # Run pylint on the file and capture the output
        for filename in fileNames:
            (pylint_stdout, pylint_stderr) = lint.py_run(filename, return_std=True)
            print("[Evaluate] " + filename)
            #pylint_output = pylint.lint.Run(["--disable=all", "--enable=error", filename], do_exit=False).linter.stats["global_note"]
            evaluations.append(pylint_stdout)
        return evaluations