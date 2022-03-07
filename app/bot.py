import os

from discord.ext import commands

from helpers import (
        hello_function, 
        kanye_quote, 
        launch_bubblebot, 
        stop_bubblebot
    )


client = commands.Bot(command_prefix="!")
tkn = os.environ.get("PYTHON_DISCORD_TOKEN")


@client.command()
async def ping(ctx):
    msg = f"Online - {client}"
    await ctx.send(msg)

@client.command()
async def hello(ctx):
    msg = hello_function()
    await ctx.send(msg)

@client.command()
async def kanye(ctx):
    msg = kanye_quote()
    await ctx.send(msg)

@client.command()
async def bubblebot(ctx):
    msg = launch_bubblebot()
    await ctx.send(msg)

@client.command()
async def bubblebotstop(ctx):
    msg = stop_bubblebot()
    await ctx.send(msg)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("------")

client.run(tkn)
