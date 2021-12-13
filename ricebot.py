import discord
#import asyncio
from discord import message
from discord import embeds
from discord.errors import ClientException
from discord.ext import commands
from discord_components import *
#import datetime
import os

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
        Button(style=ButtonStyle.green, label='4인최대'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.gray, label='4'),
        Button(style=ButtonStyle.gray, label='5'),
        Button(style=ButtonStyle.gray, label='6'),
        Button(style=ButtonStyle.green, label='4인선점'),
        Button(style=ButtonStyle.red, label='←'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.gray, label='7'),
        Button(style=ButtonStyle.gray, label='8'),
        Button(style=ButtonStyle.gray, label='9'),
        Button(style=ButtonStyle.blue, label='8인최대'),
        Button(style=ButtonStyle.red, label='Clear'),
        Button(style=ButtonStyle.red, label='종료')
    ],
    [
        Button(style=ButtonStyle.gray, label='00'),
        Button(style=ButtonStyle.gray, label='0'),
        Button(style=ButtonStyle.gray, label='000'),
        Button(style=ButtonStyle.blue, label='8인선점'),
        Button(style=ButtonStyle.red, label='종료')
    ]
]

# def calculator(exp):
#     result = ''
#     try:
#         result = str(eval(o))
#     except:
#         result = 'error'
#     return result

@client.command()
async def 경매(ctx):
    await ctx.channel.purge(limit = 1)
    m = await ctx.send(content = 'Loading Calculator')
    expression = '_'
    e = discord.Embed(title = '경매 분배금 계산기', description = '거래소 최저가를 입력하세요.')
    await m.edit(components = buttons, embed = e)
    #delta = datetime.datetime.now + datetime.timedelta(minutes = 5)
    while True:
        res = await client.wait_for('button_click')
        #if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[0].timestamp < delta:
        expression = res.message.embeds[0].description
        if expression == '_' or expression == '거래소 최저가를 입력하세요.':
            expression = ''
        if res.component.label == '←':
            if len(expression) == 1:
                expression = '_'
            else:
                expression = expression[:-1]
        elif res.component.label == 'Clear':
            expression = '_'
        elif res.component.label == '4인최대':
            expression = str(round(int(expression) * 0.7125))
        elif res.component.label == '8인최대':
            expression = str(round(int(expression) * 0.83125))
        elif res.component.label == '4인선점':
            expression = str(round(int(expression) * 0.6477))
        elif res.component.label == '8인선점':
            expression = str(round(int(expression) * 0.7557))
        # elif res.component.label == '종료':
        #     await ctx.channel.purge(limit = 1)
        else:
            expression += res.component.label
        f = discord.Embed(title='경매 분배금 계산기', description = expression)
        await res.respond(content = '', embed = f, type = 7)

client.run(os.environ['token'])