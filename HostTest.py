import socket
import sys
import traceback
from threading import Thread

piList = [["Empty"],["Empty"]]

def lijst (ip, naam):
    for i in range(len(piList)):
        for j in range(len(piList[i])):
            if piList[i][j] == "Empty":
                piList[i][j] = naam, ip
                return
            #else:
                #print("Geen ruimte voor meer systemen, vergroot de arraylist!")

def main():
    try:
        start_server()
    except:
        print("De server kan niet gestart worden!")


def start_server():
    hostname = socket.gethostname()
    IPAddres = str(socket.gethostbyname(hostname))

    host = IPAddres
    port = 8779
    print(host)

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")

    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    soc.listen(5)       # queue up to 5 requests
    print("Socket now listening")

    # infinite loop- do not reset for every requests
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        lijst(ip, port)
        print("Connected with " + ip + ":" + port)
        connection.sendall("-".encode("utf8"))
        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread is niet opgestart.")
            traceback.print_exc()
    soc.close()



def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True

    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        if "QUIT" in client_input:
            print("Client is requesting to quit")
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            print(client_input)
            connection.sendall("-".encode("utf8"))

        print(max_buffer_size)
        send_output(connection, max_buffer_size)


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        print("Het antwoord van de client is te groot! {}".format(client_input_size))
    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    result = process_input(decoded_input)
    return result

def send_output(connection, max_buffer_size):
    server_output = connection.send(max_buffer_size)
    client_input_size = sys.getsizeof(server_output)

    if client_input_size > max_buffer_size:
        print("Het antwoord van de client is te groot! {}".format(client_input_size))

    decoded_input = server_output.decode("utf8").rstrip()  # decode and strip end of line
    result = process_input(decoded_input)

    message = input(" -> ")  # take input



    return result

def process_input(input_str):
    return str(input_str).upper()

main()