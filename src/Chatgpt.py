import openai
import os

class Chatgpt:

    def askGPT(prompts):

        responses = []

        #get api_key from enviroment variable
        api_key = os.environ.get('CHATGPT_API')

        # Define OpenAI API key 
        openai.api_key = api_key

        # Set up the model and prompt
        model_engine = "text-davinci-003"

        i = 1
        
        for prompt in prompts:
            # Generate a response
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response = completion.choices[0].text
            responses.append(response)
            print("[Ask ChatGPT] " + str(i))
            i = i + 1
            
        return responses