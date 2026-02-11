import disnake
from disnake.ext import commands


class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guild = disnake.utils.get(self.bot.guilds, name='Studio Social Impacts FE3')

        if guild:
            print(f'Found guild: {guild.name} (ID: {guild.id})')

            for category in guild.categories:
                await category.delete()

            for channel in guild.text_channels:
                await channel.delete()

            general_category = await guild.create_category("Algemeen")
            flutter_category = await guild.create_category("Flutter")
            kotlin_category = await guild.create_category("Kotlin (Android)")
            projects_category = await guild.create_category("Projecten & Werk")

            await self.create_channels(guild, general_category)
            await self.create_channels(guild, flutter_category)
            await self.create_channels(guild, kotlin_category)
            await self.create_channels(guild, projects_category)

    async def create_channels(self, guild, category):
        if category.name == "Algemeen":
            channels = ['👋-welkom', '📢-aankondigingen']
        elif category.name == "Flutter":
            channels = ['🐦-flutter-vragen']
        elif category.name == "Kotlin (Android)":
            channels = ['🐢-kotlin-vragen']
        elif category.name == "Projecten & Werk":
            channels = ['💻-huidige-projecten']
        else:
            channels = []
        for channel_name in channels:
            await guild.create_text_channel(channel_name, category=category)

def setup(bot):
    bot.add_cog(Setup(bot))