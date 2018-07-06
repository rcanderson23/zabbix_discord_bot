from pyzabbix import ZabbixAPI

class zabbixbot:
    def __init__(self, username, password, url):
        self.zab = ZabbixAPI(url)
        self.zab.login(username, password)
        
    #Returns dict of host including item, last value, and unit
    def get_item(self, hostname, item):
        value = self.zab.item.get(host=hostname, search={'key_': '%s' % item})
        return value

    #Returns a list of host dicts including name and hostid
    def get_hosts(self):
        hosts = self.zab.host.get(output=["hostid","name"])
        return hosts

