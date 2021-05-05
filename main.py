import discord
import os
import time
import secrets
import discord.ext
import discordslashcommands
from replit import db
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
from discord.ext import commands
import discordslashcommands as dsc

TOKEN = os.environ['TOKEN']

client = discord.Client()

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())  #put your own prefix here


@client.event
async def on_ready():
    print("bot online")
    manager = dsc.Manager(client) # create the manager
    addtask = dsc.Command(name="addtask", description="Add a task") 
    option = dsc.Option(name="Task", description="Date - Course - Task", type=dsc.STRING, required=True)
    manager.add_global_command(addtask) 
    addtask.add_option(option) # create the manager
    removetask = dsc.Command(name="removetask", description="Remove a task") 
    option1 = dsc.Option(name="id", description="ID of the task", type=dsc.STRING, required=True)
    manager.add_global_command(removetask) 
    removetask.add_option(option1)
    print("all done")
    

@client.command()
async def addtask(ctx, *args):
    await ctx.channel.purge()
    token = secrets.token_urlsafe(5)
    x = ' '.join(args)
    db[token] = x
    embed = discord.Embed(title="Tasks Remaining")
    embed.set_author(name="Sample TaskBot", url="https://errhythm.me")
    embed.set_thumbnail(url="https://i.imgur.com/qzFDxaj.png")
    keys = db.keys()
    for id in keys:
        task = db[id]
        embed.add_field(name=task, value="Task ID: "+id, inline=False)
    embed.set_footer(text="To add a task, type !addtask {Task}. Remove a task by the id number, !removetask {id}")
    await ctx.send(embed=embed)



@client.command()
async def removetask(ctx, *args):
    await ctx.channel.purge()
    deltok = ' '.join(args)
    del db[deltok]
    embed = discord.Embed(title="Tasks Remaining")
    embed.set_author(name="Sample TaskBot", url="https://errhythm.me")
    embed.set_thumbnail(url="https://i.imgur.com/qzFDxaj.png")
    keys = db.keys()
    if not keys:
      embed.add_field(name="No Task Available", value="NA", inline=False)
    else:
      for id in keys:
          task = db[id]
          embed.add_field(name=task, value="Task ID: "+id, inline=False)
    embed.set_footer(text="To add a task, type !addtask {Task}. Remove a task by the id number, !removetask {id}")
    await ctx.send(embed=embed)


client.run(os.getenv("TOKEN"))  
