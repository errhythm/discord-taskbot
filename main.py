import discord
import os
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

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())  


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
  try:
    x = ' '.join(args)
    course, task, date = x.split(' - ')
    try:
      date = date.replace(' ', '-')
    except:
      None
    try:
      date = date.replace('/', '-')
    except:
      None  
    try:
      if 'January' in date:
        date = date.replace('January', '01')
      if 'january' in date:
        date = date.replace('january', '01')
      elif 'Jan' in date:
        date = date.replace('Jan', '01')
      elif 'jan' in date:
        date = date.replace('jan', '01')
      elif 'February' in date:
        date = date.replace('February', '02')
      elif 'Feb' in date:
        date = date.replace('Feb', '02')
      elif 'March' in date:
        date = date.replace('March', '03')
      elif 'Mar' in date:
        date = date.replace('Mar', '03')
      elif 'April' in date:
        date = date.replace('April', '04')
      elif 'Apr' in date:
        date = date.replace('Apr', '04')
      elif 'May' in date:
        date = date.replace('May', '05')
      elif 'June' in date:
        date = date.replace('June', '06')
      elif 'Jun' in date:
        date = date.replace('Jun', '06')
      elif 'July' in date:
        date = date.replace('July', '07')
      elif 'Jul' in date:
        date = date.replace('Jul', '07')
      elif 'August' in date:
        date = date.replace('August', '08')
      elif 'Aug' in date:
        date = date.replace('Aug', '08')
      elif 'September' in date:
        date = date.replace('September', '09')
      elif 'Sep' in date:
        date = date.replace('Sep', '09')
      elif 'October' in date:
        date = date.replace('October', '10')
      elif 'Oct' in date:
        date = date.replace('Oct', '10')
      elif 'November' in date:
        date = date.replace('November', '11')
      elif 'Nov' in date:
        date = date.replace('Nov', '11')
      elif 'December' in date:
        date = date.replace('December', '11')
      elif 'Dec' in date:
        date = date.replace('Dec', '11')  
      elif 'february' in date:
        date = date.replace('february', '02')
      elif 'feb' in date:
        date = date.replace('feb', '02')
      elif 'march' in date:
        date = date.replace('march', '03')
      elif 'mar' in date:
        date = date.replace('mar', '03')
      elif 'april' in date:
        date = date.replace('april', '04')
      elif 'apr' in date:
        date = date.replace('apr', '04')
      elif 'may' in date:
        date = date.replace('may', '05')
      elif 'june' in date:
        date = date.replace('june', '06')
      elif 'jun' in date:
        date = date.replace('jun', '06')
      elif 'july' in date:
        date = date.replace('july', '07')
      elif 'jul' in date:
        date = date.replace('jul', '07')
      elif 'august' in date:
        date = date.replace('august', '08')
      elif 'aug' in date:
        date = date.replace('aug', '08')
      elif 'september' in date:
        date = date.replace('september', '09')
      elif 'sep' in date:
        date = date.replace('sep', '09')
      elif 'october' in date:
        date = date.replace('october', '10')
      elif 'oct' in date:
        date = date.replace('oct', '10')
      elif 'november' in date:
        date = date.replace('november', '11')
      elif 'nov' in date:
        date = date.replace('nov', '11')
      elif 'december' in date:
        date = date.replace('december', '11')
      elif 'dec' in date:
        date = date.replace('dec', '11')  
    except:
      None
    date = "{2}-{1}-{0}".format(*date.split('-'))
    s = secrets.token_urlsafe(1)
    moddate = date+s
    try:
      moddate = moddate.replace('-', '')
    except:
      None
    db[moddate] = x
    embed = discord.Embed(title="Tasks Remaining")
    embed.set_author(name="CSE Bois", url="http://reminderbot.ehsanurrahmanra.repl.co/")
    embed.set_thumbnail(url="https://i.imgur.com/3ZvXM4e.gif")
    hkeys = db.keys()
    keys = sorted(hkeys)
    for id in keys:
        task = db[id]
        embed.add_field(name=task, value="Task ID: "+id, inline=False)
    embed.set_footer(text="To add a task, type !addtask  {Course - Task - Date(DD-MM-YYYY)}. Remove a task by the id number, !removetask {id}. If task doesnt work, please go to this link and then try again. http://reminderbot.ehsanurrahmanra.repl.co/")
    await ctx.channel.purge()
    await ctx.send(embed=embed)
  except:
    await ctx.send("Incorrect format, please try again!")



@client.command()
async def removetask(ctx, *args):
    deltok = ' '.join(args)
    del db[deltok]
    embed = discord.Embed(title="Tasks Remaining")
    embed.set_author(name="CSE Bois", url="http://reminderbot.ehsanurrahmanra.repl.co/")
    embed.set_thumbnail(url="https://i.imgur.com/3ZvXM4e.gif")
    hkeys = db.keys()
    keys = sorted(hkeys)
    if not keys:
      embed.add_field(name="No Task Available", value="NA", inline=False)
    else:
      for id in keys:
          task = db[id]
          embed.add_field(name=task, value="Task ID: "+id, inline=False)
    embed.set_footer(text="To add a task, type !addtask  {Course - Task - Date(DD-MM-YYYY)}. Remove a task by the id number, !removetask {id}. If task doesnt work, please go to this link and then try again. http://reminderbot.ehsanurrahmanra.repl.co/")
    await ctx.channel.purge()
    await ctx.send(embed=embed)

@client.command()
async def deltask(ctx, *args):
    deltok = ' '.join(args)
    del db[deltok]
    embed = discord.Embed(title="Tasks Remaining")
    embed.set_author(name="CSE Bois", url="http://reminderbot.ehsanurrahmanra.repl.co/")
    embed.set_thumbnail(url="https://i.imgur.com/3ZvXM4e.gif")
    hkeys = db.keys()
    keys = sorted(hkeys)
    if not keys:
      embed.add_field(name="No Task Available", value="NA", inline=False)
    else:
      for id in keys:
          task = db[id]
          embed.add_field(name=task, value="Task ID: "+id, inline=False)
    embed.set_footer(text="To add a task, type !addtask  {Course - Task - Date(DD-MM-YYYY)}. Remove a task by the id number, !removetask {id}. If task doesnt work, please go to this link and then try again. http://reminderbot.ehsanurrahmanra.repl.co/")
    await ctx.channel.purge()
    await ctx.send(embed=embed)

@client.command()
async def remtask(ctx, *args):
    deltok = ' '.join(args)
    del db[deltok]
    embed = discord.Embed(title="Tasks Remaining")
    embed.set_author(name="CSE Bois", url="http://reminderbot.ehsanurrahmanra.repl.co/")
    embed.set_thumbnail(url="https://i.imgur.com/3ZvXM4e.gif")
    hkeys = db.keys()
    keys = sorted(hkeys)
    if not keys:
      embed.add_field(name="No Task Available", value="NA", inline=False)
    else:
      for id in keys:
          task = db[id]
          embed.add_field(name=task, value="Task ID: "+id, inline=False)
    embed.set_footer(text="To add a task, type !addtask  {Course - Task - Date(DD-MM-YYYY)}. Remove a task by the id number, !removetask {id}. If task doesnt work, please go to this link and then try again. http://reminderbot.ehsanurrahmanra.repl.co/")
    await ctx.channel.purge()
    await ctx.send(embed=embed)

client.run(os.getenv("TOKEN"))  
