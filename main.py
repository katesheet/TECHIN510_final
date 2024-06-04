from openai_api import OpenAIChat

chat = OpenAIChat()

while True:
    ins = input('type in the message you want to send to gpt: ')
    response = chat.get_response(ins)
    print('gpt says: ', response)

