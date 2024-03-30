import os
import openai
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key

llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

def text_complition(prompt: str) -> dict:
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f'Human: {prompt}\nAI: ',
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )

        response_text = response['choices'][0]['text'].strip()

        if "vacation" in prompt or "travel" in prompt:
            template = """
            I really want to travel to {location}. What should I do there?
            Respond in one short sentence.
            """
            langchain_prompt = PromptTemplate(
                input_variables=["location"],
                template=template,
            )
            final_prompt = langchain_prompt.format(location=response_text)

        elif "quantum physics" in prompt:
            template = """
            I want to learn about quantum physics. What should I read?
            Respond in one short sentence.
            """
            langchain_prompt = PromptTemplate(
                input_variables=["book"],
                template=template,
            )
            final_prompt = langchain_prompt.format(book=response_text)

        else: "emotion" in prompt or "feeling" in prompt
        template = """
        I am feeling {emotion}. What should I do?
        Respond in one short sentence.
        """
        langchain_prompt = PromptTemplate(
            input_variables=["emotion"],
            template=template,
        )
        final_prompt = langchain_prompt.format(emotion=response_text)
        

        langchain_response = llm(final_prompt)

        return {
            'status': 1,
            'response': langchain_response
        }
    except Exception as e:
        return {
            'status': 0,
            'response': str(e) 
        }

# Testler
print(text_complition("Where should I go on vacation?"))
print(text_complition("Tell me about quantum physics."))
