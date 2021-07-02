import discord

# TODO
# add error handling for getters


class Poll:
    def __init__(self, msg: discord.Message):
        self.title = self.get_title()
        self.duration = self.get_duration()
        self.options = self.get_options()
        self.reacts = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
        self.embed = self.create_embed()
        self.voters = {}

    def get_title(self, msg: discord.Message) -> str:
        return msg.content.split()[1]

    def get_duration(self, msg: discord.Message) -> float:
        return msg.content.split()[2]

    def get_options(self, msg: discord.Message):
        return msg.content.split()[3:]

    def create_embed(self):
        embed = self.embed(title=self.title)
        embed.set_author(
            name=self.msg.author.display_name, icon_url=self.msg.author.avatar_url
        )
        for i in range(len(self.options)):
            embed.add_field(name=self.options[i], value=self.emojis[i], inline=True)
        return embed
