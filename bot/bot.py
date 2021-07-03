from discord.ext import commands
import discord
from config import CONFIG

# Enable privledged intents for bot
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.reactions = True

bot = commands.Bot(CONFIG["PREFIX"], intents=intents)

extensions = [
    "modules.ping.cog",
    "modules.poll.cog",
    "modules.roles.cog",
    "modules.sarcasm.cog",
    "modules.watch.cog",
]

for extension in extensions:
    bot.load_extension(extension)


@bot.event
async def on_ready():
    print(f"################## GONK ##################")
    print(f"I am currently logged in as { bot.user }")


# Run the bot
bot.run(CONFIG["DISCORD_TOKEN"])
