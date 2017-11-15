import time
from socket import *



if __name__ == '__main__':
    print 'Hello! Please enter a nickname, less than 9 charakters and contains no spaces'
    while True:
        name = raw_input()
        print name
        print  len(name)
        if " " not in name:
            if len(name) < 9:
                if len(name)< 1:
                    print 'Please re-enter a suitable nickname, less than 9 charakters and contains no spaces'
                else:
                    print "Nickname is acceptable"
                    break
        else:
            print 'Please re-enter a suitable nickname, less than 9 charakters and contains no spaces'
    print 'Please enter the server ip address, default 127.0.0.1'
    ip = str(raw_input())
    print 'Please enter the server ip address, default 4000: '
    sock = int(raw_input())
    destination = (ip, sock)
    print destination
    sok = socket(AF_INET, SOCK_STREAM)
    try:
        sok.connect(destination)
        print 'Connected to %s:%d' %ip, sock
    except error:
        print 'Address %s:%d socket connection failed' %(ip, sock)


#        client_socket.send('0xnonecommand')
#   count = 1
#   ip = '192.168.0.1'
#  sok = 4000
#  sok_limit = 1000
#    new_c_sok = socket(AF_INET, SOCK_STREAM)
#    while count < (sok_limit+1):
#       try:
#           new_c_sok.bind((ip, sok+count))
#       except socket.error:
#           if x == sok_limit:
#              print 'Socket limit reached'
#              break
#          else:
#              count += 1
#  print 'Listening socket closed'