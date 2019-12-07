code for sniper - application security

python3 client.py 34.83.115.103 multiply 500 100
python3 blacklist_unblacklist.py 67.166.38.83 unblock
- curl -X POST http://34.83.251.142:5001/block/67.166.38.83 - blocking an ip address (IP Address might change)
- curl -X POST http://34.83.251.142:5001/unblock/67.166.38.83 - unblocking an ip address (IP Address might change)
- curl http://34.82.145.163/mul/10/10 - nginx server running (Ip Address might change)

- curl -H "Content-Type: application/json" -X DELETE http://localhost/api/6/http/keyvals/one (Deleting all keys in nginx)

- ps -aux | grep 'python3' | awk '{print $2}' | xargs kill ( Killing all processes of python3)
- python3 client.py frontend 100

