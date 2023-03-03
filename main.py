from src.Chatgpt import Chatgpt
from src.PythonFile import PythonFile
from src.CodeEvaluation import CodeEvaluation
from src.dbprovider import dbprovider
from src.txtManager import txtManager
from dotenv import load_dotenv


load_dotenv()

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

lint_evaluations = []
timeEvaluations = []
breakdownEvaluations = []

lint_evaluations = CodeEvaluation.evaluate(fileNames)
breakdownEvaluations = CodeEvaluation.analyze_code(fileNames)
timeEvaluations = CodeEvaluation.timeEvaluate(fileNames)

dbprovider.start(prompts, responses, lint_evaluations)

# txtManager.writeEvaluation()


