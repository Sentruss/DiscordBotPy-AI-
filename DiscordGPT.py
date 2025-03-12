import discord 
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY") # <- As this is made by Open.ai Insert your api key here
token = os.getenv("BOT_TOKEN") # <- Add your bot token here through discord dev portal (Note:BOT Token should be highly confidential) 

chat = "" # If you want to add a chat behaviour <-
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):

        try:
            global chat
            chat += f"{message.author}: {message.content}\n"
            print(f'Message from {message.author}: {message.content}')
            if self.user != message.author:
                if self.user in message.mentions:
                    response = openai.Completion.create(
                        model="gpt-3.5-turbo-16k-0613",
                        messages=[
                            {
                                "role": "user",
                                "content": ""
                            }
                        ],
                        temperature=1,
                        max_tokens=256,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    channel = message.channel
                    message_to_send = response.choices[0].text
                    await channel.send(message_to_send)    
        except Exception as e:
            print(e)
