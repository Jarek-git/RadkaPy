import discord
from discord.ext import commands
import openai

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai_token = "YOUR_OPENAI_API_KEY_HERE"
        self.bot_name = "my_bot_name"

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if self.bot_name in message.content.lower():
            # Call the ChatGPT API with the user's message
            response = await self.get_gpt_response(message.content)
            # Send the response back to the channel
            await message.channel.send(response)

    async def get_gpt_response(self, user_message):
        openai.api_key = self.openai_token
        model_engine = "davinci"
        prompt = f"Conversation with my user:\nUser: {user_message}\nAI:"
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

def setup(bot):
    bot.add_cog(AI(bot))
