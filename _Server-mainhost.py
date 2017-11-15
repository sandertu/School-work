from socket import *
import shutil
import os

#Client connects to server
#Clien enteres username, server checks if username is in use
#Client creates or joins a sudoku process, server guides client to room or creates process for user
#Loop

def handle_client(client_socket, lobby_socket):
    try:
        print 'New client connected from %s:%d' % client_addr
        print 'Local end-point socket bound on: %s:%d''' % client_socket.getsockname()
        # 0x will be system call to client

        while True:
            client_socket.send('0xname')
            name = client_socket.recv(1024)
            if 0 <length(name) < 9:
                break
            else:
                client_socket.send('0xnonecommand')

        print 'Service offered, client %s:%d is using a service ...'\
        '' % client_addr
        # Wait for the client to close connection
        # This one will block till client sends something or disconnects
        client_socket.recv(1)
        print 'Client %s:%d finished using service' % client_addr
        # Here we assume client is gone
    except soc_err as e:
        if e.errno == 107:
              print 'Client %s:%d left before server could handle it'\
              '' % client_addr
    else:
        print 'Error: %s' % str(e)
    finally:
        client_socket.close()
        print 'Client %s:%d disconnected' % client_addr

if __name__ == '__main__':
    # Main infoormation for server
    client_list = []
    print 'Application started'
    sok = socket(AF_INET, SOCK_STREAM)
    serverip = '127.0.0.1'
    serverport = 4000
    # Cleaning main folder of previous session info
    if not os.path.exists('Sudoku tables'):
        os.makedirs('Sudoku tables')
        print 'New folder sudoku created'
    else:
        try:
            shutil.rmtree('Sudoku tables')
            print 'Old folder Sudoku deleted'
            os.makedirs('Sudoku tables')
            print 'New folder Sudoku created'
        except WindowsError:
            print 'No previous files'
    # Adding new files for session
    for x in range(1,55):
        f = open('Sudoku tables\\sutoku lobby %d.txt' %x, 'w+')
        f.write('Welcome to sudoku lobby %d' %x)
        f.close()


# Bind socket
    sok.bind((serverip, serverport))
    sok.listen(5)
    print 'Server started and listening on %s:%d' % sok.getsockname()
    try:
        while True:
            client_sok = None
            print 'Server waiting'
            client_sok, client_addr = sok.accept()
            print 'Client connected from %s:%d' % client_addr
            handle_client(client_socket)
    except KeyboardInterrupt:
        print 'Keyboard interrupt issued, closing server'
    finally:
        if client_sok != None:
            client_sok.close()
        sok.close
        for x in client_list:
            x.close
    print 'Server cleanly closed'



