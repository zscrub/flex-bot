import os
import interactions

from helpers import (
                hello_function, 
                kanye_quote, 
                launch_bubblebot, 
                stop_bubblebot
        )

tkn = os.getenv("PYTHON_DISCORD_TOKEN")
bot = interactions.Client(token=tkn)


@bot.command(
        name="hello",
        description="Welcoming command"
    )
async def hello_fn(ctx: interactions.CommandContext):
    insult = hello_function()
    await ctx.send(insult)


@bot.command(
        name="kanye",
        description="help function for the bot, returns bot description"
    )
async def kanye_fn(ctx: interactions.CommandContext):
    kanye = knaye_quote()
    await ctx.send(kanye)
 

@bot.command(
        name="bubblebot_run",
        description="Launches BubbleBot"
    )
async def launch_bubblebot_fn(ctx: interactions.CommandContext):
    output = launch_bubblebot()
    await ctx.send(output)


@bot.command(
        name="bubblebot_kill",
        description="Kills BubbleBot"
    )
async def stop_bubblebot_fn(ctx: interactions.CommandContext):
    output = stop_bubblebot()
    await ctx.send(output)


@bot.event
async def on_ready():
    print('flex-bot started')
    print('------')

if __name__=="__main__":
    bot.start()

