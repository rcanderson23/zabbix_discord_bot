zabbix\_discord\_bot
====================

Installation
--------------------
1. Create your discord application [here](https://discordapp.com/developers/applications/me)
2. After creating your application, create your bot at the bottom of the page
3. Authorize your bot with the url [https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot](https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot) replacing XXXX with your client ID
4. Move `config.sample.ini` to `config.ini`
5. Replace `discord_secret` in `config.ini` with your bot user token 
5. Change values in `config.ini` with appropriate values
6. Create a virtual environment with `virtualenv . -p /usr/bin/python3`
7. Activate with `source bin/activate` and install required packages with `pip install -r requirements.txt`
8. Run bot with `python bot.py`

Functions
--------------------

`z?get $host $zabbix.item` will retreive the last value of that item from specified host in your zabbix server.<br>
`z?listitems $host` will list available items for the host<br>
`z?listshosts` will output all monitored hosts in Zabbix<br>
`z?listproblems` will output all items in a problem state<br>
