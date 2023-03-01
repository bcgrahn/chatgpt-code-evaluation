import openai

class Chatgpt:

    def askGPT(prompt_):
        # Define OpenAI API key 
        openai.api_key = "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"

        # Set up the model and prompt
        model_engine = "text-davinci-003"
        prompt = prompt_

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
        #print("[Response] " + response)
        return response