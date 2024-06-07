# Unblock Googlebot

Ever had google get added to your firewall? Ever try to figure out which IP address google was using when it got blocked? Fear not! We can purge your firewall of all google bot IP addresses.

This script assumes you're using Crowdsec and IPTables. There's a command to purge your blacklist, and it's this:

`ipset del crowdsec-blacklists X.X.X.X`

## Python to the rescue

This script will download the latest list of IP ranges from google, and run that command against all of them. Huzzah!
