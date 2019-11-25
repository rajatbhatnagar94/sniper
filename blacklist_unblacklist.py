import requests
import json
import sys
#from time import perf_counter 
import time

def getInfo(server_ip, ip):
    url = "http://{0}/api/5/http/keyvals/one".format(server_ip)
    data = {
        ip: "1" 
    }
    headers = {'content-type': 'application/json'}
    response = requests.get(url, data=json.dumps(data), headers=headers)
    status = "unknown"
    value = response.json().get(ip) 
    if value is not None:
        if value == "1":
            status = "blacklist"
        else:
            status = "Non Blacklisted"

    print("current status - {0}".format(status))
    return response.json().get(ip)

def blockIP(server_ip, ip):
    url = "http://{0}/api/5/http/keyvals/one".format(server_ip)
    data = {
        ip: "1" 
    }
    headers = {'content-type': 'application/json'}
    method = 'post'
    is_existing = getInfo(server_ip, ip)
    if is_existing:
        method = 'patch'
    response = requests.request(method, url, data=json.dumps(data), headers=headers)
    print(response.text)

def unblockIP(server_ip, ip):
    url = "http://{0}/api/5/http/keyvals/one".format(server_ip)
    data = {
        ip: "0"
    }
    headers = {'content-type': 'application/json'}
    method = 'post'
    is_existing = getInfo(server_ip, ip)
    if is_existing:
        method = 'patch'
    response = requests.request(method, url, data=json.dumps(data), headers=headers)
    print(response.text)

if __name__ == "__main__":
    server_ip="localhost"
    ip = sys.argv[1]
    api = sys.argv[2]
    if api == 'block':
        blockIP(server_ip, ip)
    elif api == 'unblock':
        unblockIP(server_ip, ip)
    elif api == 'getinfo':
        getInfo(server_ip, ip)
