import json
import requests
import urllib3
from login_bt import get_token
import csv
urllib3.disable_warnings()

token = get_token()

def vmm_domain(tenant_name,app_name,epg_name,vmm_domain_name):
    #print(get_token())
    base_url = 'https://-ip-address/api/'
    url_prepend = f'node/mo/uni/tn-{tenant_name}/ap-{app_name}/epg-{epg_name}.json'
    url= base_url+url_prepend
    headers = {
        "Cookie" : f"APIC-Cookie={token}",
        "Content-Type" : "application/json",
        "connection":"keep-alive"}
    
    prepayload={"fvRsDomAtt":{"attributes":{"resImedcy":"immediate",
                                            "tDn":f"uni/vmmp-VMware/dom-{vmm_domain_name}",
                                            "instrImedcy":"immediate","status":"created"},
                                            "children":[{"vmmSecP":{"attributes":{"status":"created"},"children":[]}}]}}


    payload = json.dumps(prepayload)
    response = requests.post(url=url,data=payload,headers=headers,verify=False)
    json_response = json.loads(response.text)
    print(response.status_code)
    #print(response.text)
    return response.status_code

if __name__ == '__main__':
    print (token)
    with open('epg_vmm_list.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
                vmm_domain(row[0],row[1],row[2],row[3])
            except Exception as e:
                print (e)
