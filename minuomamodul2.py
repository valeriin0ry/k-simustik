from string import *
from time import sleep
import random
import smtplib, ssl 
from email.message import EmailMessage 
import imghdr
def send_email(receiver_email, correct_answers):
    smtp_server="smtp.gmail.com"
    port=587
    sender_email = "s1ncepr3m@gmail.com"
    password=input("Kirjuta oma salasõna ja vajuta enter: ")
    receiver_email=input("Sisesta email: ")
    context = ssl.create_default_context()
    message = f"Siin on teie testi õiged vastused:\n\n{correct_answers}"
    teema = "Testi õiged vastused"
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = teema
    msg['From'] = "Valera Ashurov"
    msg['To'] = receiver_email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        print("Õiged vastused on saadetud")
    except Exception as e:
        print(e)
    finally:
        server.quit()
def autoriseerimine(kasutajad: list, paroolid: list):
    p = 0
    while True:
        kasutaja = input("Sisestage kasutajanimi: ")
        parool = input("Sisestage parool: ")
        if kasutaja in kasutajad and parool in paroolid:
            print("Sisselogimine õnnestus!")
            return kasutaja
        else:
            p += 1
            print("Vale nimi või salasõna!")
            if p == 5:
                print("Proovi uuesti 10 sekundi pärast")
                for i in range(10):
                    sleep(1)
                    print(f"On jäänud {10-i} sekundit")
            else:
                print("Kasutajat pole")
                break
def loe(Ankeet: str):
    kus = []
    vas = []
    with open(Ankeet, 'r', encoding='utf-8') as fail:
        for line in fail:
            n = line.find(":")
            kus.append(line[0:n].strip())
            vas.append(line[n+1:].strip())
    return kus, vas
def lisa(kus_vas, Ankeet: str):
    with open(Ankeet, 'a', encoding='utf-8') as fail:
        for küsimus, vastus in kus_vas.items():
            fail.write(f"{küsimus}:{vastus}\n")
def küsimus_vastus(kus_vas, n):
    punktid = 0
    küsimused = random.choices(list(kus_vas[0]), k=n)
    correct_answers = ""
    for küsimus in küsimused:
        print(küsimus)
        vastus = input("Vastus: ").strip()
        if vastus.lower() == kus_vas[1][kus_vas[0].index(küsimus)].lower():
            punktid += 1
            correct_answers += f"{küsimus}: {kus_vas[1][kus_vas[0].index(küsimus)]}\n"
    return punktid, correct_answers
def salvesta(osaleja_nimi, punktid, Oiged: str, Valed: str):
    if punktid > len("kus_vas") / 2:
        with open(Oiged, 'a', encoding='utf-8') as oiged:
            oiged.write(f"{osaleja_nimi}\n")
    else:
        with open(Valed, 'a', encoding='utf-8') as valed:
            valed.write(f"{osaleja_nimi}\n")