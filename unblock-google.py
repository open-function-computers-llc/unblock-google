#!/usr/bin/env python3

import urllib.request, json, ipaddress, subprocess

jsonLists = [
    "https://developers.google.com/search/apis/ipranges/googlebot.json",
    "https://developers.google.com/static/search/apis/ipranges/special-crawlers.json",
    "https://developers.google.com/static/search/apis/ipranges/user-triggered-fetchers.json",
    "https://developers.google.com/static/search/apis/ipranges/user-triggered-fetchers-google.json"
]

for jsonURL in jsonLists:
    with urllib.request.urlopen(jsonURL) as url:
        data = json.loads(url.read().decode())
        for addressData in data["prefixes"]:
            for k in addressData:
                if (k != "ipv4Prefix"):
                    continue

                net = ipaddress.ip_network(addressData[k])
                for i in net:
                    p = subprocess.run(["ipset", "del", "crowdsec-blacklists", str(i)])
                    if (p.returncode == 0):
                        print("Unblocked "+str(i))
