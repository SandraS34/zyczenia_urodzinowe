#wiadomosc = str(input())
#nadawca = str(input())

print("Podaj imię solenizanta: ")
imie=input()
if imie.endswith("a"): #Sprawdzam czy na końcu imienia występuje litera "a". Jeśli tak to wyświetlam tekst dla rodzaju żeńskiego
    print(f"W którym roku urodziła się {imie}?")
    rok = int(input())
else:
    print(f"W którym roku urodził się {imie}?")
    rok =int(input())
wiek = 2026-rok
print("Napisz wiadomość: ")
wiad = input()
print("Kto jest nadawcą? ")
nadawca=input()
full_text=f"{imie}! Wszystkiego najlepszego z okazji {wiek} urodzin!\n{wiad}\n{nadawca}"
print(full_text)






