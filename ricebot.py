import discord
from discord import message
from discord import embeds
from discord.errors import ClientException
from discord.ext import commands
from discord_components import *
import datetime

client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    print('ready')
    DiscordComponents(client)

buttons = [
    [
        Button(style=ButtonStyle.gray, label='1'),
        Button(style=ButtonStyle.gray, label='2'),
        Button(style=ButtonStyle.gray, label='3'),
        Button(style=ButtonStyle.green, label='4인')
    ],
    [
        Button(style=ButtonStyle.gray, label='4'),
        Button(style=ButtonStyle.gray, label='5'),
        Button(style=ButtonStyle.gray, label='6'),
        Button(style=ButtonStyle.green, label='8인')
    ],
    [
        Button(style=ButtonStyle.gray, label='7'),
        Button(style=ButtonStyle.gray, label='8'),
        Button(style=ButtonStyle.gray, label='9'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.gray, label='00'),
        Button(style=ButtonStyle.gray, label='0'),
        Button(style=ButtonStyle.gray, label='000'),
        Button(style=ButtonStyle.red, label='Clear')
    ]
]

def calculator(exp):
    o = exp.replace('×', '*')
    o = o.replace('÷', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'error'
    return result

@client.command()
async def 경매(ctx):
    m = await ctx.send(content = 'Loading Calculator')
    expression = '_'
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(title = '경매 분배금 계산기', description = '거래소 최저가를 입력하세요.', timestamp = delta)
    await m.edit(components = buttons, embed = e)
    while m.created_at < delta:
        res = await client.wait_for('button_click')
        #if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[0].timestamp < delta:
        expression = res.message.embeds[0].description
        if expression == '_' or expression == 'error' or expression == '거래소 최저가를 입력하세요.':
            expression = ''
        if res.component.label == '←':
            expression = expression[:-1]
        elif res.component.label == 'Clear':
            expression = '_'
        elif res.component.label == '4인':
            expression = str(round(int(calculator(expression)) * 95 / 100 * 3 / 4))
        elif res.component.label == '8인':
            expression = str(round(int(calculator(expression)) * 95 / 100 * 7 / 8))
        else:
            expression += res.component.label
        f = discord.Embed(title='경매 분배금 계산기', description = expression, timestamp = delta)
        await res.respond(content = '', embed = f, type = 7)

client.run('OTA3NTU1NzM4NTMxMDEyNjA4.YYo5JQ.xI4OOCGaypiVocUQw5jLJ6-Elc8')