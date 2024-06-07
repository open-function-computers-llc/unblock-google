import urllib.request, json, ipaddress, subprocess

with urllib.request.urlopen("https://developers.google.com/search/apis/ipranges/googlebot.json") as url:
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
