from openai_api import OpenAIChat
from paper import Paper

chat = OpenAIChat()


paper = Paper('abc', '2406.01574')
response = chat.get_response('summarize the paper 100 words: '+ paper.get_paper())
print('gpt says: ', response)

