import discord
import responses

async def send_message(message,user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTE0ODk5NDkxOTg5ODI5MjI1NA.GNdYX7.swFOzWyhc6Xjpfw51X3lYQYQS4B99MMM_Z-73M'
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        print(message)
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        print(f"{user_message} is working")
        channel = str(message.channel)

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message,user_message, is_private=True)
        else:
            await send_message(message,user_message, is_private=False)
    client.run(TOKEN)


