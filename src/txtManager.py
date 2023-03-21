import os

class txtManager:

    def writeResponses(responses, type):
        i = 1
        # Loop through the elements of the array and write them each to their own txt file
        for response in responses:
            path = f'./public/ResponseFiles/responses{i}({type}).txt'
            with open(path, "w") as file:
                print("[Write Response] " + str(i))
                file.write(response + "\n")
            i = i + 1
            
    def writePrompts(prompts, type):
        i = 1
        # Loop through the elements of the array and write them each to their own txt file
        for prompt in prompts:
            path = f'./public/Prompts/prompt{i}({type}).txt'
            with open(path, "w") as file:
                print("[Write prompt] " + str(i))
                file.write(prompt)
            i = i + 1


    def getPromptList():
        # Open the file in read mode
        with open('./public/prompts.txt', 'r') as file:
        # Read the entire file content as a string
            file_content = file.read()

            i = 1
            # Split the file content into sentences using @ as the delimiter
            sentences = file_content.split('@')

            # Create an empty array to store the sentences
            sentence_array = []

            # Loop through the sentences and add them to the array
            for sentence in sentences:
                sentence_array.append(sentence.strip())
                
            sentence_array.pop()

            for sentence in sentence_array:
                print('[Get prompt] ' + str(i))
                i = i + 1

        return sentence_array
    
    def getEvaluationList(num, type):
        evaluationList = []
        # Open the file in read mode
        for i in range(1, (num+1)):
            path = f'./public/LintEvaluations/lintEvaluations{i}({type}).txt'
            with open(path, 'r') as file:
             # Read the entire file content as a string
                file_content = file.read()
                evaluationList.append(file_content)
                
        return evaluationList
    
    def writeSummary(results, type):

        path = f'./public/EvaluationSummary({type}).txt'
        with open(path, "w") as file:
            file.write("")

        for result in results:
            path = f'./public/EvaluationSummary({type}).txt'
            with open(path, "a") as file:
                file.write(result + "\n")
    