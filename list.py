import json

hosts = []

with open('paypal_data.json', 'r') as f:
    for v in json.loads(json.loads(f.read())):
        if v.get('common_name'):
            hosts.append(v.get('common_name'))

with open('paypal-crtsh.txt', 'w') as f1:
    for h in hosts:
        f1.write(h + '\n')