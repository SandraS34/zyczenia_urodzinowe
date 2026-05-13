import datetime as dt
#year = dt.date.today().year - aktualny rok

imie=input("Podaj imie solenizanta: ")
if imie.endswith("a"): #Sprawdzam czy na końcu imienia występuje litera "a". Jeśli tak to wyświetlam tekst dla rodzaju żeńskiego
    #print(f"W którym roku urodziła się {imie}?")
    rok = int(input(f"W którym roku urodziła się {imie}? "))
else:
    #print(f"W którym roku urodził się {imie}?")
    rok = int(input(f"W którym roku urodził się {imie}? "))
wiek = dt.date.today().year - rok
#print("Napisz wiadomość: ")
wiad = input("Napisz wiadomość: ")
#print("Kto jest nadawcą? ")
nadawca = input("Kto jest nadawcą? ")
full_text = f"{imie}! Wszystkiego najlepszego z okazji {wiek} urodzin!\n{wiad}\n{nadawca}"
print(full_text)






