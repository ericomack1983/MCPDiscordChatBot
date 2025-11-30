from dotenv import load_dotenv
from openai import OpenAI, completions
import discord
import os
import openai

load_dotenv()
def chat_with_gpt(question):
    client = OpenAI(api_key="XXXXXXXX") #os.getenv('OPENAI_API_KEY'))
    print(f"User question GPT: {question}")
    completion = openai.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Respond like matrix agent smith the following question: {question}",}
        ],
        model="gpt-3.5-turbo",  
    )
    response = completion.choices[0].message.content
    print(f"OpenAI response: {response}")
    return response 

    # Example usage
    #user_prompt = "What is the capital of France?"
    #gpt_response = chat_with_gpt(user_prompt)
    #print(f"ChatGPT: {gpt_response}")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
       await message.channel.send('Hello! How can I assist you today?')

    if message.content.startswith('$question'):
        message_content = message.content.split("$question")[1]
        print(f"User question: {message_content}")
        gpt_response = chat_with_gpt(message_content)
        print(f"ChatGPT response: {gpt_response}")
        await message.channel.send(gpt_response)
        #await message.channel.send(message_content)
client.run(os.getenv('DISCORD_TOKEN'))
