from socket import *
import json

server_port = 53533
as_socket = socket(AF_INET, SOCK_DGRAM)
as_socket.bind(('', server_port))
while True:
    message, client_address = as_socket.recvfrom(2048)
    d = json.loads(message.decode())
    if len(d) == 4:
        with open('infor.txt', 'w') as outfile:
            json.dump(d, outfile)
            message = '201'
    elif len(d) == 2: 
        with open("infor.txt", 'r', encoding='utf-8') as outfile:
            for line in outfile.readlines():
                data = json.loads(line)
                if d['TYPE'] == data['TYPE'] and d['NAME'] == data['NAME']:
                    message = json.dumps(data)
                else:
                    message = 'ERROR'
    else:
        message ='ERROR'

    as_socket.sendto(message.encode(), client_address)

