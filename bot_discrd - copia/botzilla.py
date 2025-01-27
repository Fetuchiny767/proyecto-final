import os, random
import discord
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

token = "MTI1NzQ5MTIzNTc3MDQ2NjMwNQ.GAa1QW.p-XE6h0wiGfAsK-Cv2cw-IeIGKt0WmymOYNBSo"

bot = commands.Bot(command_prefix = "/", intents=intents)

@bot.event
async def on_ready():
    print("botzilla ready")

@bot.command()
async def prevencion(ctx):
    files = os.listdir("img")
    ani_r = random.choice(files)
    ani_path = os.path.join("img", ani_r)
    await ctx.send(file=discord.File(ani_path))

@bot.command()
async def consejo(ctx):
    azar = random.randint(1,2)
    if azar == 1:
        await ctx.send("reduce tu consumo de energia y agua")
    elif azar == 2:
        await ctx.send("elije cosas de segunda mano, asi reduces la carga")


bot.run(token)