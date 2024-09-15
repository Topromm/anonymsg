from discord.ext import commands
from discord import app_commands
import discord

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())
initial_extensions = ["commands"]
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="you"), status=discord.Status.do_not_disturb)
    print("Online")
    if __name__ == "__main__":
        for extension in initial_extensions:
            try:
                await bot.load_extension(extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print("Failed to load extension {}\n{}".format(extension, exc))
    try:
        synced = await bot.tree.sync()
        print(f"Loaded {len(initial_extensions)} extension(s)")
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


def is_staff():
    async def predicate(interaction: discord.Interaction) -> bool:
        try:
            staff_role = discord.utils.get(interaction.guild.roles, name="staff")
            if staff_role in interaction.user.roles:
                return True
            else:
                await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
                return False
        except AttributeError as e:
            await interaction.response.send_message("Something went wrong. Please ensure that you're using this command inside the server and have required permissions while using staff commands.", ephemeral=True)
            return False
    return app_commands.check(predicate)


@bot.tree.command(name="load", description="Loads the chosen extension.")
@app_commands.describe(extension="Current extensions: commands")
@is_staff()
async def load(interaction: discord.Interaction, extension: str):
    try:
        await bot.load_extension(extension.lower())
        await interaction.response.send_message(f"{extension.lower()} loaded.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"```py\n{type(e).__name__}: {str(e)}\n```", ephemeral=True)


@bot.tree.command(name="unload", description="Unloads the chosen extension.")
@app_commands.describe(extension="Current extensions: commands")
@is_staff()
async def unload(interaction: discord.Interaction, extension: str):
    try:
        await bot.unload_extension(extension.lower())
        await interaction.response.send_message(f"{extension.lower()} unloaded.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"```py\n{type(e).__name__}: {str(e)}\n```", ephemeral=True)


@bot.tree.command(name="reload", description="Reloads the chosen extension.")
@app_commands.describe(extension="Current extensions: commands")
@is_staff()
async def reload(interaction: discord.Interaction, extension: str):
    try:
        await bot.reload_extension(extension.lower())
        await interaction.response.send_message(f"{extension.lower()} reloaded.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"```py\n{type(e).__name__}: {str(e)}\n```", ephemeral=True)


@bot.tree.command(name="ping", description="Get the bot's current latency.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Latency: {round(bot.latency * 1000, 1)}ms", ephemeral=True)


@bot.tree.command(name="send", description="Sends a message in the chosen channel.")
@app_commands.describe(message="What should I say?", channel_id="Where should I say it?")
@is_staff()
async def send(interaction: discord.Interaction, message: str, channel_id: str):
    try:
        channel = bot.get_channel(int(channel_id))
        if channel:
            await channel.send(message)
            await interaction.response.send_message(f"Your message has been sent in {channel.mention}", ephemeral=True)
        else:
            await interaction.response.send_message("Invalid channel ID.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Something went wrong: ```py\n{type(e).__name__}: {str(e)}\n```", ephemeral=True)


@bot.tree.command(name="sendhere", description="Sends a message in the current channel.")
@app_commands.describe(message="What should I say here?")
@is_staff()
async def sendhere(interaction: discord.Interaction, message: str):
    try:
        channel = interaction.channel
        await channel.send(message)
        await interaction.response.send_message("Your message has been sent below.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Something went wrong: ```py\n{type(e).__name__}: {str(e)}\n```", ephemeral=True)


@bot.tree.command(name="dm", description="Sends a DM to the chosen user.")
@app_commands.describe(user="Who should we DM?", message="What should we DM them?")
@is_staff()
async def dm(interaction: discord.Interaction, user: discord.Member, message: str):
    try:
        await user.send(message)
        await interaction.response.send_message(f"Your message has been sent to {user.mention}", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Something went wrong: ```py\n{type(e).__name__}: {str(e)}\n```", ephemeral=True)


@bot.tree.command(name="shutdown", description="Shuts the bot down in case more fatal errors arise.")
@is_staff()
async def shutdown(interaction: discord.Interaction):
    try:
        await interaction.response.send_message("Shutting the bot down now.")
        await bot.close()
    except Exception as e:
        await interaction.response.send_message(f"Something went wrong: ```py\n{type(e).__name__}: {str(e)}\n```", ephemeral=True)


bot.run("TOKEN")

