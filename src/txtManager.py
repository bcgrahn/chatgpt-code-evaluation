import os

class txtManager:

    def writeResponses(responses):
        i = 1
        # Loop through the elements of the array and write them to the file
        for response in responses:
            path = f'./public/ResponseFiles/responses{i}.txt'
            with open(path, "w") as file:
                print("[Write Response] " + str(i))
                file.write(response + "\n")
            i = i + 1

    def getPromptList():
        # Open the file in read mode
        with open('./public/prompts.txt', 'r') as file:
        # Read the entire file content as a string
            file_content = file.read()

            i = 1
            # Split the file content into sentences using a period as the delimiter
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
    
    def getEvaluationList(num):
        evaluationList = []
        # Open the file in read mode
        for i in range(1, (num+1)):
            path = f'./public/LintEvaluations/lintEvaluations{i}.txt'
            with open(path, 'r') as file:
             # Read the entire file content as a string
                file_content = file.read()
                evaluationList.append(file_content)
                
        return evaluationList