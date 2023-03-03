from src.Chatgpt import Chatgpt
from src.PythonFile import PythonFile
from src.CodeEvaluation import CodeEvaluation
from src.dbprovider import dbprovider
from src.txtManager import txtManager
from dotenv import load_dotenv
import src.TimeComplexity

load_dotenv()

prompts = []
responses = []
fileNames = []
lint_evaluations = []
timeEvaluations = []
breakdownEvaluations = []
timeComplexities = []
complexities = []

prompts = txtManager.getPromptList()

responses = Chatgpt.askGPT(prompts)

#generate generic filename
i = 1
for prompt in prompts:
    #create file names for each response
    fileName = f"response{i}.py"
    fileNames.append(fileName)
    i = i + 1

#write responses to txt file
txtManager.writeResponses(responses)
#create python scripts from all the responses
PythonFile.create(responses, fileNames)

#Evaluate python pep* conformaty
lint_evaluations = CodeEvaluation.evaluateLint(fileNames)
timeEvaluations = CodeEvaluation.timeEvaluate(fileNames)
#breakdownEvaluations = CodeEvaluation.analyze_code(fileNames)
#timeComplexities = CodeEvaluation.timeComplexity(fileNames)
#complexities = CodeEvaluation.complexity(fileNames)
#src.TimeComplexity.measure_time_complexity(fileNames)

#Write results to database
dbprovider.start(prompts, responses, lint_evaluations)

# txtManager.writeEvaluation()


