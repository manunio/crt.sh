from crtsh import crtshAPI
import json
import sys
import os
import subprocess

if not len(sys.argv) == 3:
    print("filename & url not set")
    sys.exit(1)

filename = sys.argv[1]  # "shopifycloud"
url = sys.argv[2]  # "shopifycloud.com"

out = f'out/{filename}/{filename}'
hosts = []

print("Fetching from crt.sh..")
json_data = json.dumps(crtshAPI().search(url))
os.makedirs(os.path.dirname(f'{out}.json'), exist_ok=True)
with open(f'{out}.json', 'w') as f:
    json.dump(json_data, f)


print(f"Writing response from crt.sh  to {out}.json file..")
with open(f'{out}.json', 'r') as f:
    for v in json.loads(json.loads(f.read())):
        if v.get('common_name'):
            hosts.append(v.get('common_name'))

print("Removing duplicate lines if any..")
hosts_without_duplicates = list(set(hosts))

os.makedirs(os.path.dirname(f'{out}.json'), exist_ok=True)

print(f"Writing subdomains from {out}.json  to {out}-crtsh.txt file..")
with open(f'{out}-crtsh.txt', 'w') as f1:
    for h in hosts_without_duplicates:
        f1.write(h + '\n')

print(f"Sending hosts from {out}-crtsh.txt to httprobe command..")
# it's not advisable to use shell=True,
# in this case as its a simple program we will use it.
process = subprocess.Popen(
        f"cat {out}-crtsh.txt | httprobe > {out}-urls.txt",
        shell=True
        )
process.communicate()

print("Done..")
