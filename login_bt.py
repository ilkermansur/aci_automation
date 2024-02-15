import requests
import json
 
def get_token():  
   url = "https://192.168.222.240/api/aaaLogin.json"
 
   payload = {
      "aaaUser": {
         "attributes": {
            "name":"admin",
            "pwd":"Aa123456"
         }
      }
   }
 
   headers = {
      "Content-Type" : "application/json"
   }
 
   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False).json()
   token = response['imdata'][0]['aaaLogin']['attributes']['token']
    
   return str(token)

def main():
   token = get_token()
   print("The token is: " + token)
 
if __name__ == "__main__":
   main()
