import guilded
from guilded.colour import Color
from guilded.ext import commands
from tabulate import tabulate
from config import token
from guilded.ext.commands import MemberConverter

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f"[ Online and connected to Guilded. User: {bot.user} ]")

@bot.command()
@commands.has_server_permissions(kick_members=True)
async def kick(ctx, member: commands.MemberConverter, *, reason=None):
    if member == ctx.author:
        error_embed = guilded.Embed(
            title="Error ❌",
            description="You can't kick yourself. Try again but use a different user id. \n\n*Don't know how to get a user's id? refer to [this post](https://support.guilded.gg/hc/en-us/articles/6183962129303-Developer-mode) to enable **developer** mode.* \n\n*Having trouble? no worries! You can send this to [The Developer](https://www.guilded.gg/u/weebwashere) so the problem can get fixed.*",
            color=0x36363D
        )
        await ctx.send(embed=error_embed)
        return
    try:
        kick = guilded.Embed(
            title=f"Success!",
            description=f"*You have successfully kicked {member.name}!* \n\n**Reason** - `{reason}`\n**By** - {ctx.author.mention}",
            color=0x36363D,
        )
        kick.set_thumbnail(url="https://cdn.gilcdn.com/ContentMediaGenericFiles/c07c747f7f1093b8ad0c32a4394f1c21-Full.webp?w=500&h=500")
        await member.kick()
        await ctx.reply(embed=kick, silent=True)
    except Exception as e:
        print(f"An error occurred while trying to kick the user: {e}")
        error_embed = guilded.Embed(
            title="Error ❌",
            description="An error occurred while trying to kick the user. \n\n*having trouble? no worries! You can send this to [The Developer](https://www.guilded.gg/u/weebwashere) so the problem can get fixed.*",
            color=0x36363D
        )
        error_embed.set_thumbnail(url="https://cdn.gilcdn.com/ContentMediaGenericFiles/aa4b19b0bf393ca43b2f123c22deb94e-Full.webp?w=900&h=900")
        await ctx.send(embed=error_embed, private=True)
        
@bot.command()
@commands.has_server_permissions(ban_members=True)
async def ban(ctx, member: commands.MemberConverter, *, reason=None):
    if member == ctx.author:
        error_embed = guilded.Embed(
            title="Error ❌",
            description="You can't ban yourself. Try again but use a different user id. \n\n*Don't know how to get a user's id? refer to [this post](https://support.guilded.gg/hc/en-us/articles/6183962129303-Developer-mode) to enable **developer** mode.* \n\n*Having trouble? no worries! You can send this to [The Developer](https://www.guilded.gg/u/weebwashere) so the problem can get fixed.*",
            color=0x36363D
        )
        await ctx.send(embed=error_embed)
        return
    try:
        ban = guilded.Embed(
            title=f"Success!",
            description=f"*You have successfully banned {member.name}!* \n\n**Reason** - `{reason}`\n**By** - {ctx.author.mention}",
            color=0x36363D,
        )
        ban.set_thumbnail(url="https://cdn.gilcdn.com/ContentMediaGenericFiles/c07c747f7f1093b8ad0c32a4394f1c21-Full.webp?w=500&h=500")
        await member.ban()
        await ctx.reply(embed=ban, silent=True)
    except Exception as e:
        print(f"An error occurred while trying to ban the user: {e}")
        error_embed = guilded.Embed(
            title="Error ❌",
            description="An error occurred while trying to ban the user. \n\n*having trouble? no worries! You can send this to [The Developer](https://www.guilded.gg/u/weebwashere) so the problem can get fixed.*",
            color=0x36363D
        )
        error_embed.set_thumbnail(url="https://cdn.gilcdn.com/ContentMediaGenericFiles/aa4b19b0bf393ca43b2f123c22deb94e-Full.webp?w=900&h=900")
        await ctx.send(embed=error_embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        permission_em = guilded.Embed(
            title="Insufficient Permissions ❌",
            description=f"{ctx.author.mention}, For the argument `target`, I was expecting the `user` to have the correct permissions.\n\nYou **must** currently have the `{error.missing_perms}` permission in order to execute this command.",
            color=0x36363D
        )
        permission_em.add_field(name="Usage", value="```$ban [userid] [reason]```")
        await ctx.send(embed=permission_em, private=True)
    else:
        print(f"An error occurred: {error}")

bot.run(token)