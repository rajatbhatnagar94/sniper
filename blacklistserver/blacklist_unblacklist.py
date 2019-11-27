from flask import Flask, request, Response
import requests
import json
import sys
#from time import perf_counter 
import jsonpickle
import time

app = Flask(__name__)

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

@app.route('/block/<ip>', methods=['POST'])
def blockIP(ip):
    server_ip = 'nginx'
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
    response_pickled = jsonpickle.encode({
        'text': 'blocked' 
    })
    return Response(response=response_pickled, status=200)

@app.route('/unblock/<ip>', methods=['POST'])
def unblockIP(ip):
    server_ip = 'nginx'
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
    response_pickled = jsonpickle.encode({
        'text': 'unblocked' 
    })
    return Response(response=response_pickled, status=200)

app.run(host="0.0.0.0", port=5001)

#if __name__ == "__main__":
#    server_ip="localhost"
#    ip = sys.argv[1]
#    api = sys.argv[2]
#    if api == 'block':
#        blockIP(server_ip, ip)
#    elif api == 'unblock':
#        unblockIP(server_ip, ip)
#    elif api == 'getinfo':
#        getInfo(server_ip, ip)
