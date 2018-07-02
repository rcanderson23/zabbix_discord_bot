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

@zbot.command(name='get',
              description="Gets information from zabbix server")
async def get(host, item):
    output = ""
    result = zab.get_item(host, item)
    for key,value in result.items():
        output += "%s: %s\n" % (key, value)
    await zbot.say(output)


zbot.run(discord_secret)
