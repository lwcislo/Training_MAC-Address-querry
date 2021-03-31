import requests
import json 
import argparse

### HARDCODED API LINK
api_address='https://api.macaddress.io/v1'

### EXPENDABLE PARSER FOR PURPOSE OF FURTHER USAGE 
parser = argparse.ArgumentParser(description='Simple Company Name Extractor')
parser.add_argument('--company_name', '-C',action='store_true',
                        help='Sends request to obtain the vendor company name')
parser.add_argument('--mac_address', '-M',dest='mac_address', type=str, nargs=1,
                        default=['44:38:39:ff:ef:57'], help='MAC address in XX:XX:XX:XX:XX:XX format')
parser.add_argument('--api_key', '-K',dest='api_key', type=str, nargs=1,
                        default=['at_fL1h81cB5ZymXGODVFWfm3Zvi9EA9'], help='The API key, please use your own')

option = parser.parse_args()

### ESSENTIAL PART, SENDING A REQUEST, DECODING JSON TO DICT
### AND EXTRACTING THE DESIRED INFORMATION

if option.company_name:
    mac_address=str(option.mac_address[0])
    api_key=str(option.api_key[0])
    payload = {'apiKey':api_key, 'output':'json', 'search':mac_address}
    req = requests.get(api_address, params=payload)
    api_answer={req.text}
    parsed = ""
    for a in api_answer:
            parsed = str(a)
 
### IF FOR SOME REASON JSON WILL BE RETURNED WITH WRONG SIGNS 

    json_acceptable_string = parsed.replace("'", "\"")

    dict = json.loads(json_acceptable_string)
 
    print(dict['vendorDetails']['companyName'])
