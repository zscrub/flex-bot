import os
import json
import requests
import interactions

tkn = os.getenv("PYTHON_DISCORD_TOKEN")
bot = interactions.Client(token=tkn)

@bot.command(
        name="hello",
        description="Welcoming command"
    )
async def hello_function(ctx: interactions.CommandContext):
    insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&amp;type=json")
    insult = insult.text
    await ctx.send(str(insult))

@bot.command(
        name="kanye",
        description="help function for the bot, returns bot description"
    )
async def kanye_quote(ctx: interactions.CommandContext):
    kanye = requests.get("api.kanye.rest").json()
    kanye = kanye["quote"]
    await ctx.send(kanye)

bot.start()
