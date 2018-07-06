import configparser
import os
import sys
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
    output = "__**Hostname:**__ **%s**\n\n" % hostname
    result = zab.get_item(hostname, item)
    for values in result:
        output += "**item:** %s\n**lastvalue:** %s\n**units:** %s\n\n" \
            % (values['key_'], values['lastvalue'], values['units'])
    await zbot.say(output)

@zbot.command(name='listitems',
              description="Lists item values available for host")
async def list_items(hostname):
    output = "__**Hostname:**__ **%s**\n\n" % hostname
    result = zab.get_item(hostname, item)

zbot.run(discord_secret)
