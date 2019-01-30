import psycopg2
from prettytable import PrettyTable
from time import gmtime, strftime
import datetime


conn = psycopg2.connect(host="localhost",dbname= "Feedbacklamp_Database" , user="postgres", password="Spetter6")
cur = conn.cursor()
#Username = Username, Password = Password

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

def insertValuesTest(PiNaam, PiLocatie, Decibel):
    time = strftime("%Y%m%d %H:%M:%S", gmtime())
    timeLijst = time.split(" ")
    dag = timeLijst[0]
    tijd = timeLijst[1]
    SQL = "INSERT INTO Waarschuwing (PiNaam, PiLocatie, Decibel, Dag, Tijd) VALUES (%s, %s, %s, %s, %s);"
    data = (PiNaam, PiLocatie, Decibel, dag, tijd)
    cur.execute(SQL, data)
    gemiddelde()

#insertValuesTest("Client1", "Lokaal1", 70)
#insertValuesTest("Client1", "Lokaal1", 70)

gemiddelde()
