## Simple Company Name Extractor

Optional arguments:
```
  -h, --help            show this help message and exit
  --company_name, -C    Sends request to obtain the vendor company name
  --mac_address MAC_ADDRESS, -M MAC_ADDRESS
                        MAC address in XX:XX:XX:XX:XX:XX format
  --api_key API_KEY, -K API_KEY
                        The API key, please use your own

```
Usage:

```
$python3 simple_script.py -C -M <MAC ADDRESS> -K <PRIVATE KEY>

$<PARSED ANSWER>
```

I.e.

```
$python3 simple_script.py -C -M 44:38:39:ff:ef:57 -K at_fL1h81cB5ZymXGODVFWfm3Zvi9EA9

$Cumulus Networks, Inc
```

### IMPORTANT

Please be aware, that the key given as an example is not a secure solution,
one using this script should generate her or his own, and do not use it 
in automated manner as it is not safe to pass it as an argument.
