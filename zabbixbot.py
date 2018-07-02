from pyzabbix import ZabbixAPI

class zabbixbot:
    def __init__(self, username, password, url):
        self.zab = ZabbixAPI(url)
        self.zab.login(username, password)
        
    def get_item(self, hostname, item):
        host_values = {'hostname': hostname,
                       'item': item,
                       'lastvalue': ''
                      }

        value = self.zab.item.get(host=hostname, search={'key_': '%s' % item}, limit=1)
        host_values['item'] = value[0]['key_']
        host_values['lastvalue'] = value[0]['lastvalue']
        return host_values

