from pyzabbix import ZabbixAPI

class zabbixbot:
    def __init__(self, username, password, url):
        self.zab = ZabbixAPI(url)
        self.zab.login(username, password)
        
    #Returns dict of host including item, last value, and unit
    def get_item(self, hostname, item):
        if item == 'all':
            return self.zab.item.get(host=hostname)
        else:
            return self.zab.item.get(host=hostname, search={'key_': '%s' % item})

    #Returns a list of host dicts including name and hostid
    def get_hosts(self):
        return self.zab.host.get(output=["hostid","name"])

    def get_problems(self):
        return self.zab.trigger.get(only_true=1,
                                    monitored=1,
                                    active=1,
                                    selectHosts=['host'],
                                    expandDescription=1)
