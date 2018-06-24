import configparser
import os
import sys
from pyzabbix import ZabbixAPI
from discord.ext.commands import Bot
import asyncio

config = configparser.ConfigParser()
try:
    config.read_file(open('config.ini'))
except FileNotFoundError:
    exit('Error: File not found. Check file name.')

discord_secret = config['discord']['discord_secret']
zabbix_url = config['zabbix']['zabbix_url']
zabbix_user = config['zabbix']['zabbix_user']
zabbix_password = config['zabbix']['zabbix_password']


zab = ZabbixAPI(zabbix_url)
zab.login(zabbix_user, zabbix_password)
zbot = Bot(command_prefix="z?")


#gets first result from zabbix API and returns a dict  
def get_item(host_name, item):
    host_values = { 'hostname': host_name,
                    'item': item,
                    'lastvalue': ''
                  }
    value = zab.item.get(host=host_name, search={'key_': '%s' % item}, limit=1)
    host_values['item'] = value[0]['key_']
    host_values['lastvalue'] = value[0]['lastvalue']
    return host_values

@zbot.command(name='get',
              description="Gets information from zabbix server")
async def get(host, item):
    output = ""
    result = get_item(host, item)
    for key,value in result.items():
        output += "%s: %s\n" % (key, value)
    await zbot.say(output)


zbot.run(discord_secret)
