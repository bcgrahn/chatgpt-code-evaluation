from src.Chatgpt import Chatgpt
from src.PythonFile import PythonFile
from src.CodeEvaluation import CodeEvaluation
from src.dbprovider import dbprovider
from src.txtManager import txtManager

prompts = []
responses = []
evaluations = []
fileNames = []

prompts = txtManager.getPromptList()
i = 1

for prompt in prompts:
    res = Chatgpt.askGPT(prompt)
    responses.append(res)
    evaluations.append("dummy data")
     
    fileName = f"response{i}.py"
    fileNames.append(fileName)
    i = i + 1

txtManager.writeResponses(responses)

PythonFile.create(responses, fileNames)
evaluation_array = []
evaluation_array = CodeEvaluation.evaluate(fileNames)

dbprovider.start(prompts, responses, evaluation_array)

# txtManager.writeEvaluation()


