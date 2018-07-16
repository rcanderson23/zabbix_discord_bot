import configparser
import os
import sys
import operator
from discord.ext.commands import Bot
import asyncio
from zabbixbot import zabbixbot


config = configparser.ConfigParser()
try:
    config.read_file(open('config.ini'))
except FileNotFoundError:
    exit('Error: File not found. Check file name.')

discord_secret = config['discord']['discord_secret']
zabbix_url = config['zabbix']['zabbix_url']
zabbix_user = config['zabbix']['zabbix_user']
zabbix_password = config['zabbix']['zabbix_password']

zbot = Bot(command_prefix="z?")
zab = zabbixbot(zabbix_user, zabbix_password, zabbix_url)


@zbot.command(name='getitem',
              description="Gets information from zabbix server")
async def get_item(hostname, item):
    output = f"__**Hostname:**__ **{hostname}**\n\n"
    result = zab.get_item(hostname, item)
    for values in result:
        output += f"**item:** {values['key_']}\n**lastvalue:** {values['lastvalue']}\n**units:** {values['units']}\n\n"
    await zbot.say(output)

@zbot.command(name='listitems',
              description="Lists item values available for host")
async def list_items(hostname):
    output = f"__**Hostname:**__ **{hostname}**\nName:Key\n\n"
    result = zab.get_item(hostname, 'all')
    result.sort(key=operator.itemgetter('name'))
    for item in result:
        output += f"{item['name']}:{item['key_']}\n"
    await zbot.say(output)

@zbot.command(name='listhosts',
              description="Lists hosts in zabbix")
async def list_hosts():
    output = "__**Hosts:**__\n\n"
    result = zab.get_hosts()
    result.sort(key=operator.itemgetter('name'))
    for host in result:
        output += f"{host['name']}\n"
    await zbot.say(output)

@zbot.command(name='listproblems',
              description="Lists triggered events in zabbix")
async def list_problems():
    output = ""
    result = zab.get_problems()
    if not result:
        output += "No problems to report"
    else:
        for trigger in result:
            output += f"**Trigger:** {trigger['description']} \n**Host:** {trigger['hosts'][0]['host']}\n\n"
    await zbot.say(output)


zbot.run(discord_secret)
