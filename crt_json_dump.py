from crtsh import crtshAPI
import json
import sys


if not len(sys.argv) == 3:
    print("filename & url not set")
    sys.exit(1)

filename = sys.argv[1]  # "shopifycloud"
url = sys.argv[2]  # "shopifycloud.com"


print("fetching from crt.sh..")
print()
json_data = json.dumps(crtshAPI().search(url))
with open(f'{filename}.json', 'w') as f:
    json.dump(json_data, f)

hosts = []

print(f"writing response from crt.sh  to {filename}.json file..")
print()
with open(f'{filename}.json', 'r') as f:
    for v in json.loads(json.loads(f.read())):
        if v.get('common_name'):
            hosts.append(v.get('common_name'))

print("removing duplicate lines if any..")
print()
hosts_without_duplicates = list(set(hosts))

print(f"writing subdomains from {filename}.json  to {filename}-crtsh.txt file..")
with open(f'{filename}-crtsh.txt', 'w') as f1:
    for h in hosts_without_duplicates:
        f1.write(h + '\n')


