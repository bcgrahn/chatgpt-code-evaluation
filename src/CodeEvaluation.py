import pylint.lint
import os
from radon.complexity import cc_visit, cc_rank
from radon.metrics import mi_visit
import radon.complexity as radon_cc
import re
import time

class CodeEvaluation:

    def evaluateLint(num, type):
        # Run pylint on the file and capture the output
        for i in range(1, (num+1)):
            filename = f"response{i}({type}).py"
            short_path = f'./public/ResponseFiles/{filename}'
            file_path = os.path.join(os.getcwd(), short_path)
            output_path = f'--output=./public/LintEvaluations/lintEvaluations{i}({type}).txt'
            
            i = i + 1
            # Define the Pylint command-line arguments
            args = [
                #'--rcfile=pylintrc',  # Path to a Pylint configuration file
                output_path,
                '--msg-template={msg_id} {msg}: {category}: {line:3d},{column}: {obj}:',  # Output format
                file_path,
                '--load-plugins=pylint.extensions.mccabe',
            ]

            try:
                print("[Lint evalutation] " + filename)
                pylint.lint.Run(args)
            except:
                nothing = ""
    
    # def timeEvaluate(fileNames):
    #     timeEvaluations = []
    #     folder_path = "./public/ResponseFiles"
    #     for filename in fileNames:
    #         file_path = os.path.join(folder_path, filename)
    #         start_time = time.time()
    #         command = f"python {file_path}"
    #         os.system(command)

    #         end_time = time.time()
    #         timeEvaluations.append(end_time-start_time)

    #         print("[Evaluate execution time] " + str(end_time-start_time))

    #     return timeEvaluations

    def countCode(num, type):
        word_count = {}
        total = 0.0
        for i in range(1, (num+1)):
            # Open the file for reading
            with open(f'./public/LintEvaluations/lintEvaluations{i}({type}).txt', 'r') as file:
                #words to be excluded
                pattern = r"[*]|Your"
                score = 0.0
                # Loop through each line in the file
                for line in file:
                    # Split the line into words
                    words = line.split(':')
                    if words:
                        # Get the first word of the line
                        regex = r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\''
                        first_word = re.sub(regex, '{variable}', words[0])
            
                        #exclude certain phrases
                        if not re.search(pattern, first_word):
                            # Count the number of occurrences of the word
                            if first_word in word_count:
                                word_count[first_word] += 1
                            else:
                                word_count[first_word] = 1
                        else:
                            #extract the overall score
                            temp = first_word.split(' ')
                            word = temp[0]
                            if word == 'Your':
                                temp2 = temp[6]
                                scores = (temp2.split('/'))
                                score = float(scores[0])
                                total = total + score
                                print(total)

        summary = []
        # Print the word count
        for word, count in word_count.items():
            statement = f'Number: {count} Error: {word}'
            summary.append(statement)

        total = total/float(num)
        overall_rating = f'\n---------------------\nOverall rating: {total}'
        summary.append(overall_rating)
        return summary
    
    
        