import os
import json
import signal
import requests
import subprocess
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
    url = "http://api.kanye.rest?"
    kanye = requests.get(url).json()
    kanye = kanye["quote"]
    print(f"Kanye quote: {kanye}")
    await ctx.send(kanye)


class BotProcess:
    process_id = None
    def set_pid(self, process_id):
        self.process_id = process_id

bubblebot = BotProcess()

@bot.command(
        name="bubblebot",
        description="Launches BubbleBot"
    )
async def launch_bubblebot(ctx: interactions.CommandContext):
    subprocess.Popen(["python", 'bots/DiscordBot/bot.py'], preexec_fn=os.setsid)
    bubblebot.set_pid(subprocess.Popen(["python", 'bots/DiscordBot/bot.py'], preexec_fn=os.setsid).pid)
    await ctx.send("Launching BubbleBot...")


@bot.event
async def on_ready():
    print('flex-bot started')
    print('------')

if __name__=="__main__":
    try:
        bot.start()
    except KeyboardInterrupt:
        os.killpg(os.getpgid(bubblebot.process_id), signal.SIGTERM)
        print("Killing bot subprocesses...")
