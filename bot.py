import os
import discord


client = discord.Client()
tkn = os.environ.get("PYTHON_DISCORD_TOKEN")

@client.event
async def on_message(message):

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(tkn)
