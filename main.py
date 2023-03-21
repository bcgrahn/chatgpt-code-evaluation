from src.Chatgpt import Chatgpt
from src.PythonFile import PythonFile
from src.CodeEvaluation import CodeEvaluation
from src.dbprovider import dbprovider
from src.txtManager import txtManager
from dotenv import load_dotenv

load_dotenv()

prompts = []
responses = []
fileNames = []
lint_evaluations = []
timeEvaluations = []
breakdownEvaluations = []
timeComplexities = []
complexities = []
evaluationSummary = []

#Get prompts from txt file
prompts = txtManager.getPromptList()
i = len(prompts)

#Itteration 1
#------------------
#ask chatGPT
responses = Chatgpt.askGPT(prompts)
#write responses to txt file
txtManager.writeResponses(responses, 1)
txtManager.writePrompts(prompts, 1)
#create python scripts from all the responses
PythonFile.create(responses, 1)
#Evaluate python pep8 conformaty
CodeEvaluation.evaluateLint(i, 1)
lint_evaluations = txtManager.getEvaluationList(i, 1)
evaluationSummary = CodeEvaluation.countCode(i, 1)
txtManager.writeSummary(evaluationSummary, 1)
#Write results to database
# dbprovider.start(prompts, responses, lint_evaluations)

#Itteration 2
#------------------
#ask chatGPT
newPrompts = []
for prompt in prompts:
    newPrompts.append(prompt + " \nThe response must conform with pythons PEP 8 standard. ")
responses = Chatgpt.askGPT(newPrompts)
#write responses to txt file
txtManager.writeResponses(responses, 2)
txtManager.writePrompts(newPrompts, 2)
#create python scripts from all the responses
PythonFile.create(responses, 2)
#Evaluate python pep8 conformaty
CodeEvaluation.evaluateLint(i, 2)
lint_evaluations = txtManager.getEvaluationList(i, 2)
evaluationSummary = CodeEvaluation.countCode(i, 2)
txtManager.writeSummary(evaluationSummary, 2)

#Itteration 3
#------------------
#ask chatGPT
newNewPrompts = []
for response, evaluation in zip(responses,lint_evaluations):
    newNewPrompts.append("For this piece of python code: " + response + "\n. \n\nFix the known errors from the following list:\n\n" + evaluation)
responses = Chatgpt.askGPT(newNewPrompts)
#write responses to txt file
txtManager.writeResponses(responses, 3)
txtManager.writePrompts(newNewPrompts, 3)
#create python scripts from all the responses
PythonFile.create(responses, 3)
#Evaluate python pep8 conformaty
CodeEvaluation.evaluateLint(i, 3)
lint_evaluations = txtManager.getEvaluationList(i, 3)
evaluationSummary = CodeEvaluation.countCode(i, 3)
txtManager.writeSummary(evaluationSummary, 3)



