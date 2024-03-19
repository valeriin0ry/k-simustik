from minuomamodul2 import *
kasutajad = ["Valera"]
paroolid = ["Hashiro"]
kus_vas = loe("Ankeet.txt")
while True:
    print("1-soorita test\n2-logi administraatorina sisse\n3-lõpetamine")
    vastus = int(input("Sisestage arv "))
    if vastus == 1:
        print("Soorita test")
        osaleja_nimi = input("Palun sisestage oma nimi: ")
        N = int(input("Mitu küsimust soovite? "))
        punktid, correct_answers = küsimus_vastus(kus_vas, N)
        salvesta(osaleja_nimi, punktid, "Oiged.txt", "Valed.txt")
        print("\nEdukalt läbinud osalejad:")
        with open("Oiged.txt", 'r', encoding='utf-8') as oiged_fail:
            print(oiged_fail.read())
        print("\nEbaõnnestunud osalejad:")
        with open("Valed.txt", 'r', encoding='utf-8') as valed_fail:
            print(valed_fail.read())
        send_email(osaleja_nimi, correct_answers)  # Sending email with correct answers
    elif vastus == 2:
        print("Administraator")
        autoriseerimine(kasutajad, paroolid)
        uued = {}
        uute_arv = int(input("Mitu uut küsimust soovid lisada? "))
        for i in range(uute_arv):
            küsimus = input("Sisestage uus küsimus: ")
            vastus = input("Sisestage vastus uuele küsimusele: ")
            uued[küsimus] = vastus
        lisa(uued, "Ankeet.txt")
    elif vastus == 3:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")