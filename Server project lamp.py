import socket, traceback, sys, psycopg2
from threading import Thread
from tkinter import *
from prettytable import PrettyTable
from time import gmtime, strftime

root = Tk()

root.title('GUI')
root.geometry('670x500')

conn = psycopg2.connect(host="localhost",dbname= "Feedbacklamp_Database" , user="postgres", password="Spetter6")
conn.autocommit = True
cur = conn.cursor()

piEenRood = 75
piEenOranje = 50
piTweeRood = piEenRood
piTweeOranje = piEenOranje



def kleur():
    kleur = Label(master= root, text= '',background = 'red', width= 5)
    kleur.grid(row=1, column= 0,sticky=W)

    kleur1= Label(master= root, text= '', background= 'orange', width=5)
    kleur1.grid(row=2, column=0, sticky=W)

    kleur2 = Label(master= root, text= '', background= 'green', width=5)
    kleur2.grid(row=3, column=0, sticky=W)

    kleur3 = Label(master=root, text='', background='red', width=5)
    kleur3.grid(row=6, column=0, sticky=W)

    kleur4 = Label(master=root, text='', background='orange', width=5)
    kleur4.grid(row=7, column=0, sticky=W)

    kleur5 = Label(master=root, text='', background='green', width=5)
    kleur5.grid(row=8, column=0, sticky=W)

def labelclient1():
    label = Label(master=root, text='Client 1', backgroun='gray', width=10)
    label.grid(row=0, column=0, columnspan=5, sticky='news')

def labelclient2():
    label2= Label(master=root, text= '', width= 10)
    label2.grid(row= 4, column= 0, sticky=W)
    label1=Label(master=root,text= 'Client 2',background= 'gray', width=10)
    label1.grid(row=5, column= 0,columnspan=5,sticky='news')



label3= Label(master=root, text= '', width = 8)
label3.grid(row=9, column= 0,sticky = W)



b1= Label(master = root, text=str(piEenRood)+' db', width =5)
b1.grid(row=1, column= 1, sticky=W)

b2= Label(master= root, text=str(piEenOranje)+' db', width=5)
b2.grid(row=2, column=1, sticky= W)

b3= Label(master= root, text=str(25)+' db', width=5)
b3.grid(row=3, column=1, sticky= W)

b4= Label(master= root, text=str(piTweeRood)+' db', width=5)
b4.grid(row=6, column =1, sticky= W)

b5 = Label(master=root, text=str(piTweeOranje)+' db', width=5)
b5.grid(row=7, column=1, sticky=W)

b6= Label(master=root, text=str(25)+' db', width=5)
b6.grid(row= 8, column=1, sticky=W)

c1= Label(master = root, text= 'Voer waarde in:', width = 20)
c1.grid(row=1, column=2, sticky=W)

c2= Label(master = root, text= 'Voer waarde in:', width = 20)
c2.grid(row=2, column=2, sticky=W)

c3= Label(master = root, text= 'Voer waarde in:', width = 20)
c3.grid(row=3, column=2, sticky=W)

c4= Label(master = root, text= 'Voer waarde in:', width = 20)
c4.grid(row=6, column=2, sticky=W)

c5= Label(master = root, text= 'Voer waarde in:', width = 20)
c5.grid(row=7, column=2, sticky=W)

c6= Label(master = root, text= 'Voer waarde in:', width = 20)
c6.grid(row=8, column=2, sticky=W)


e1 = Entry(master=root, width=8)
e1.grid(row=1, column=3, sticky=W)
e2 = Entry(master=root, width=8)
e2.grid(row=2, column=3, sticky=W)
e3 = Entry(master=root, width=8)
e3.grid(row=3, column=3, sticky=W)
e4 = Entry(master=root, width=8)
e4.grid(row=6, column=3, sticky=W)
e5 = Entry(master=root, width=8)
e5.grid(row=7, column=3, sticky=W)
e6 = Entry(master=root, width=8)
e6.grid(row=8, column=3, sticky=W)

def Rood1():
    global piEenRood
    res= e1.get() + ' db'
    b1.configure(text=res)
    piEenRood = e1.get()

def Oranje1():
    global piEenOranje
    res= e2.get() + ' db'
    b2.configure(text=res)
    piEenOranje = e2.get()

def Geel1():
    res = e3.get() + ' db'
    b3.configure(text=res)

def Rood2():
    global piTweeRood
    res = e4.get() + ' db'
    b4.configure(text=res)
    piTweeRood = e4.get()

def Oranje2():
    global piTweeOranje
    res = e5.get() + ' db'
    b5.configure(text=res)
    piTweeOranje = e5.get()

def Geel2():
    res = e6.get() + ' db'
    b6.configure(text=res)

def labelbutton():
    btn1= Button(master = root,text= 'Verander', width= 11, command= Rood1)
    btn2= Button(master=root, text= 'Verander',width= 11,command= Oranje1)
    btn3= Button(master=root, text= 'Verander',width= 11,command=Geel1)
    btn4= Button(master=root, text= 'Verander',width= 11, command= Rood2)
    btn5= Button(master=root, text= 'Verander',width= 11, command= Oranje2)
    btn6= Button(master=root, text= 'Verander',width= 11, command= Geel2)
    btn1.grid(row=1, column =4, sticky =W)
    btn2.grid(row=2, column =4, sticky =W)
    btn3.grid(row=3, column=4, sticky =W)
    btn4.grid(row=6, column =4, sticky =W)
    btn5.grid(row=7, column =4, sticky =W)
    btn6.grid(row=8, column =4, sticky =W)

    #exit = Button(master= root, text= 'Sluit GUI', width= 11, command= root.destroy)
    #exit.grid(row= 11, column= 3, sticky= W)

def resetclicked():
    b1.configure(text=str(piEenRood)+' db')
    b2.configure(text=str(piEenOranje)+' db')
    b3.configure(text=str(25)+' db')
    b4.configure(text=str(piTweeRood)+' db')
    b5.configure(text=str(piTweeOranje)+' db')
    b6.configure(text=str(25)+' db')

def main():
    start_server()



def start_server():
    hostname = socket.gethostname()
    IPAddres = str(socket.gethostbyname(hostname))
    host = IPAddres
    port = 8759
    print("Host IP adres: ", host)


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
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()

    soc.close()



def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True
    packageClient1 = str(piEenRood) + ' ' + str(piEenOranje) + "Client 1"
    packageClient2 = str(piTweeRood) + ' ' + str(piTweeOranje) + "Client 2"
    connection.sendall(packageClient1.encode("utf8") + packageClient2.encode("utf8"))
    package = str(piEenRood) + ',' + str(piEenOranje)
    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        if "QUIT" in client_input:
            print("Client is requesting to quit")
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            if "Client 1 " in client_input:
                print(client_input)
                package = package + "Client 1"
                connection.sendall(package.encode("utf8"))
            elif "Client 2 " in client_input:
                print(client_input)
                package = package + "Client 2"
                connection.sendall(package.encode("utf8"))
            client_input = client_input.split(" ")
            print(client_input)
            insertValuesTest(client_input[0], client_input[1], int(float(client_input[3])), client_input[4])


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))

    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    print(decoded_input)
    result = process_input(decoded_input)

    return result


def process_input(input_str):
    return str(input_str).upper()

def setup():
    kleur()
    labelclient1()
    labelclient2()
    labelbutton()

################################################################################
#Postgresql#

def sqlWaarschuwing():
    query = "SELECT * FROM Waarschuwing"
    sqlQuery(query)

def sqlAlarm():
    query = "SELECT * FROM Alarm"
    sqlQuery(query)

def maakHTML(results):
    x = PrettyTable([results[0][0]])
    lengthList = len(results)
    for i in range(1, lengthList):
        print(results[i])
        x.add_row([results[i]])
    html_code = x.get_html_string()
    html_file = open("/Users/bruusriezebos/Documents/School/Utrecht HBO ICT/FeedbackHTML.html", 'w')
    html_file = html_file.write(html_code)

def sqlQuery(query):
    cur.execute(query)
    results = cur.fetchall()
    maakHTML(results)

def gemiddelde():
    query = "SELECT * FROM Waarschuwing"
    sqlQuery(query)

def insertValuesTest(PiNaam, PiLocatie, Decibel, Alarm):
    time = strftime("%Y%m%d %H:%M:%S", gmtime())
    timeLijst = time.split(" ")
    dag = timeLijst[0]
    tijd = timeLijst[1]
    if Alarm == "TRUE":
        SQL = "INSERT INTO Alarm (PiNaam, PiLocatie, Decibel, Dag, Tijd) VALUES (%s, %s, %s, %s, %s);"
        print("Inserted into Alarm!")
    else:
        SQL = "INSERT INTO Waarschuwing (PiNaam, PiLocatie, Decibel, Dag, Tijd) VALUES (%s, %s, %s, %s, %s);"
        print("Inserted into Waarschuwing!")
    data = (PiNaam, PiLocatie, Decibel, dag, tijd)
    cur.execute(SQL, data)
    sqlWaarschuwing()
###############################################################################


ereset= Button(master=root,text= 'Reset instellingen', width=14, command= resetclicked)
ereset.grid(row= 11, column= 0, sticky= W)
HTML= Button(master=root,text= "Selecteer alles van Waarschuwing", width=25, command= sqlWaarschuwing)
HTML.grid(row = 12, column= 0, sticky= W)
HTML2= Button(master=root,text= 'Selecteer alles van Alarm', width=25, command= sqlAlarm)
HTML2.grid(row = 13, column= 0, sticky= W)

setup()
root.mainloop()
main()