# Config usage:
#   Copy this file and remove .example, 'cp config.example.py config.py'
#   See Mike or Bryan for any issues or questions.

# TOKENS:
#    Get tokens from discord dev portal/server, add them to
#    DISCORD_TOKEN and DISCORD_GUILD

import os

def init():
    global prefix, admin_roles, default_role, token, guild_id

    # change this string to your preferred command prefix
    prefix = "."

    # change these strings to your prefered admin and default roles
    admin_roles = ["Black Giant Squirrel", "Grizzled Squirrel"]
    default_role = "Kit"

    # leave these alone
    DISCORD_TOKEN = "Nzk5NjgzODcwNzM1ODU5NzEy.YAHJpA.nJ5GfTpRNfgdvo2tras_46hOyCk"
    token = DISCORD_TOKEN

    DISCORD_GUILD = "420371160312709130"
    guild_id = DISCORD_GUILD
