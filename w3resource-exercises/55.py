"""
55. Write a Python to find local IP addresses using Python's stdlib
"""
import socket
#from socket import gethostname, getaddrinfo

#host = socket.gethostname()
#ip = socket.getaddrinfo(host='127.0.0.1', port='3307')

#print(f'HOST={host}')
#print(f'IP={ip}')

#print()
#print(str(socket.gethostbyname_ex(host)))

#print(
# [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
#   if not ip.startswith("127.")][:1], 
#   [[
#       (s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) 
#       for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

def get_ip_addrs():
    host_name = socket.gethostname()
    ip_list = socket.gethostbyname_ex(host_name)[2]
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    google_dns = ('8.8.8.8', 53)

    cnx = s.connect(google_dns)

    socket_name = s.getsockname()

    s.close()

    return socket_name[0]


if __name__ == '__main__':
    print(get_ip_addrs())