from discord.ext import commands
prefix = "?"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("Everything's all ready to go~")


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)


bot.run('NTg5OTU5NTk1ODI5NzU1OTE0.XQo-zw.Mbi6Oxiffo7HFPVlSd-h4QcxbcM')  
