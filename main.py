from itertools import count
from pickle import FALSE, TRUE
from traceback import print_tb


class Ksiazka:
    ksiazki = []
    def __init__(self, tytul, autor, liczba_sztuk = 1):
        self.tytul = tytul
        self.autor = autor
        self.liczba_sztuk = liczba_sztuk

    def __repr__(self):
        return f"('{self.tytul}', '{self.autor}', {self.liczba_sztuk})"
    
    def sprawdz_ksiazke(nazwa, tworca):
            if Ksiazka.ksiazki != []:

                for i in range(len(Ksiazka.ksiazki)):
                    if Ksiazka.ksiazki[i][0] == nazwa:
                        Ksiazka.ksiazki[i][2] += 1
                        break
                    elif Ksiazka.ksiazki[i][0] != nazwa and i+1 == len(Ksiazka.ksiazki):
                        Ksiazka.ksiazki.append([nazwa, tworca, 1])
                        
            else:
                Ksiazka.ksiazki.append([nazwa, tworca, 1])      

class Egzemplarz():
    def __init__(self, tytul, autor, rok):
        self.rok = rok
        self.tytul = tytul
        self.autor = autor
        Ksiazka.sprawdz_ksiazke(self.tytul, self.autor)

        
    def __repr__(self):
        return f"('{self.tytul}', '{self.autor}', {self.rok})"

n = input()
n = int(n)
for i in range(n):
    x = eval(input())
    Egzemplarz(x[0],x[1],x[2])
sorted(Ksiazka.ksiazki, key=lambda x: x[1], reverse=True)
for i in range(len(Ksiazka.ksiazki)):
    print(Ksiazka(Ksiazka.ksiazki[i][0],Ksiazka.ksiazki[i][1],Ksiazka.ksiazki[i][2]))




        

        
