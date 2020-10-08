from flask import Flask,request
from socket import *
import json

app = Flask(__name__)
@app.route('/fibonacci', methods=['GET'])
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
@app.route('/register', methods=['PUT'])
def register():
    infor = request.get_json() 
    hostname,ip,as_ip,as_port = infor['hostname'],infor['ip'],infor['as_ip'],infor['as_port']
    server_name,server_port = as_ip,53533
    fs_socket = socket(AF_INET, SOCK_DGRAM) 
    dns_request = {'TYPE': 'A','NAME': hostname,'VALUE': ip,'TTL': 10
    }
    message = json.dumps(dns_request)
    fs_socket.sendto(message.encode(), (server_name, server_port))
    message, server_address = fs_socket.recvfrom(2048)
    fs_socket.close()
    return message.decode()

def get_fibonacci_number():
    num = int(int(request.args.get('number')))
    if num >=0:
    	return 'sequence {0} fibonacci {1}, 200 OK'.format(num, Fibonacci(num))
    else:
    	return 'ERROR 400'

app.run(host='0.0.0.0',
        port=9090,
        debug=True)
