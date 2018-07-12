from pyzabbix import ZabbixAPI

zab = ZabbixAPI('https://zabbix.carsonisawesome.com')
zab.login('discord', 'discord')
output = ""
results = zab.trigger.get(only_true=1,
                         monitored=1,
                         active=1,
                         selectHosts=['host'],
                         expandDescription=1)
for trigger in results:
    output += "Trigger: %s \nHost: %s\n\n" % (trigger['description'], trigger['hosts'][0]['host'])

print(output)
