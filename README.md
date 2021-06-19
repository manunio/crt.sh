crt_json_dump.py
========
This program searches given url at crt.sh,
extracts common_name(subdomains) from response and stores it
<domain>-crtsh.txt.

example:
`
python3 crt_json_dump.py shopifycloud shopifycloud.com
`

crt.sh Python utility
========
This project aims at helping you to interact with [crt.sh](https://crt.sh) website. 

Git clone the repo. 

```bash
git clone https://github.com/PaulSec/crt.sh
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Then, you can start interacting with crt.sh this way: 

```python
from crtsh import crtshAPI
import json

print(json.dumps(crtshAPI().search('uber.com')))
```

The result is an array of dictionary items which looks like this: 

```json 
[
  {
      "issuer_ca_id": 16418,
      "issuer_name": "C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3",
      "name_value": "hatch.uber.com",
      "min_cert_id": 325717795,
      "min_entry_timestamp": "2018-02-08T16:47:39.089",
      "not_before": "2018-02-08T15:47:39"
  },
  ....
]
```

License
========

This has been released under MIT License. For any question, feel free to contact me on Twitter [@PaulWebSec](https://twitter.com/@PaulWebSec).
