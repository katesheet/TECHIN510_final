import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class OpenAIChat:
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            # base_url="https://openai.ianchen.io/v1",
        )
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]


    def _add_to_messages(self, message, role='assistant'):
        '''
        role is either 'user' or 'assistant'
        '''
        self.messages.append({"role": role, "content": message})


    def get_response(self, instruction):
        self._add_to_messages(instruction, 'user')
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.messages
            )
        response = completion.choices[0].message.content
        # print(response)
        self._add_to_messages(response)
        return response



        