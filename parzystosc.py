def parzystosc(liczba):
    if liczba == 0:
        return 'Nie badamy zera'
    tekst = f'Podana cyfra {liczba} to liczba'
    if liczba % 2 == 0:
        tekst += ' parzysta.'
    else:
        tekst += ' nieparzysta.'
    return tekst

x = int(input('Podaj liczbę:'))
komentarz = parzystosc(x)
print(komentarz)
