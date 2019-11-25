import requests
import json
import sys
#from time import perf_counter 
import time

def blockIP(ip):
    url = "http://{0}/api/5/http/keyvals/one".format(ip)
    data = {
        ip: "1" 
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.text)

def unblockIP(ip):
    url = "http://{0}/api/5/http/keyvals/one".format(ip)
    data = {
        ip: "0"
    }
    headers = {'content-type': 'application/json'}
    response = requests.patch(url, data=json.dumps(data), headers=headers)
    print(response.text)

def mul(ip, x, y, n_iter):
    for i in range(n_iter):
        url = "http://{0}/mul/{1}/{2}".format(ip, x, y)
        response = requests.get(url)
        print(response.text)

if __name__ == "__main__":
    ip = sys.argv[1]
    api = sys.argv[2]
    n_iter = int(sys.argv[3])
    x = sys.argv[4]
    if api == 'block':
        blockIP(ip)
    elif api == 'unblock':
        unblockIP(ip)
    elif api == 'multiply':
        mul(ip, x, x, n_iter)
