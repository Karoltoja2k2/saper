from tkinter import *
import random
from tkinter import font
import time
from operator import itemgetter

class Menu:
    def __init__(self):
        self.menu=Tk()
        self.backg = "#126748"
        self.menu.configure(bg=self.backg)
        self.tlo, self.latwa, self.srednia, self.expert, self.ranking, self.osiagniecia, self.staty = \
            PhotoImage(file='tlo.png'), PhotoImage(file='latwa.png'), PhotoImage(file='srednia.png'), PhotoImage(file='expert.png'), \
            PhotoImage(file='ranking.png'), PhotoImage(file='osiagniecia.png'), PhotoImage(file='staty1.png')



    def latwy(self):
        self.menu.destroy()
        gra = Gra(10, 9, 9)

    def sredni(self):
        self.menu.destroy()
        gra = Gra(40, 16, 16)

    def trudny(self):
        self.menu.destroy()
        gra = Gra(99, 16, 30)

    def rank(self):
        """otwiera okno rankingu"""
        ranking = Ranking()

    def rysowanie(self):
        """wyglad menu glownego"""
        odstep3 = Label(self.menu, bg=self.backg)
        odstep3.grid(row=0, column=0)

        napis = Label(self.menu, image=self.tlo, borderwidth=0, activebackground=self.backg, bg=self.backg)
        napis.grid(row=0, columnspan=3)

        odstep = Label(self.menu, bg=self.backg, text='   ')
        odstep.grid(column=0, row=1)

        R1 = Button(self.menu, image=self.latwa, bg=self.backg, borderwidth=0, activebackground=self.backg, command=self.latwy)
        R1.grid(column=1, row=2)

        R2 = Button(self.menu, image=self.srednia, bg=self.backg, borderwidth=0, activebackground=self.backg, command=self.sredni)
        R2.grid(column=1, row=3)

        R3 = Button(self.menu, image=self.expert, bg=self.backg, borderwidth=0, activebackground=self.backg, command=self.trudny)
        R3.grid(column=1, row=6)

        odstep2 = Label(self.menu, bg=self.backg)
        odstep2.grid(column=0, row=7)

        posiagniecia = Button(self.menu, image=self.osiagniecia, bg=self.backg, borderwidth=0, activebackground=self.backg)
        posiagniecia.grid(row=3, column=2)

        pranking = Button(self.menu, image=self.ranking, borderwidth=0, activebackground=self.backg, bg=self.backg, command=self.rank)
        pranking.grid(row=2, column=2)

        odstep4 = Label(self.menu, bg=self.backg, text="    ")
        odstep4.grid(row=1, column=1)
        odstep5 = Label(self.menu, bg=self.backg, text="     ")
        odstep5.grid(row=0, column=3)

        pstaty = Label(self.menu, image=self.staty, borderwidth=0)
        pstaty.grid(row=8, columnspan=3)

        odstep7 = Label(self.menu, bg=self.backg)
        odstep7.grid(column=0, row=9)

        self.menu.mainloop()

class Ranking():
    def __init__(self):
        self.ranking=Tk()
        self.backg = "#126748"
        self.ranking.configure(bg=self.backg)
        self.ranking.title('Ranking')
        self.czcionka = font.Font(family='Helvetica', size=16)
        self.best = []
        self.rysowanie()

    def leader(self):
        file = open('wyniki.txt', 'r')
        for linia in file:
            linia = linia.split(';')
            self.best += [linia]

        file.close()

    def rysowanie(self):
        self.leader()
        asd = sorted(self.best, key=itemgetter(1))
        for item in asd:

            label = Label(self.ranking, text='{} - {} - {} - {}'.format(item[0], item[1], item[2], item[3]), bg=self.backg, font=self.czcionka, fg='white')
            label.pack()



class Plansza():

    def __init__(self, liczbabomb, rzad, kolumna):

        # generuje liste bomb
        self.listabomb0 = []
        while len(set(self.listabomb0)) < liczbabomb:
            bomba = (random.choice(range(rzad)), random.choice(range(kolumna)))

            self.listabomb0 += [bomba]
        self.listabomb0 = set(self.listabomb0)

        indekspola = -1
        self.plansza = []

        #generuje plansze
        for rz in range(rzad):
            for kol in range(kolumna):

                indekspola = indekspola + 1
                self.plansza += [[indekspola, rz, kol, False, 0, False, None]]
                for b in self.listabomb0:
                    if b == (rz, kol):
                        self.plansza[indekspola][3] = True

        #dodaje ilosc bomb przyleglych
        self.pole0 = []
        for pole in self.plansza:
            if pole[3] == True:

                rz = pole[1]
                kol = pole[2]
                ind = pole[0]

                if rz - 1 >= 0:  # góra
                    self.plansza[ind - kolumna][4] += 1

                if rz + 1 <= rzad - 1:  # dół
                    self.plansza[ind + kolumna][4] += 1

                if kol - 1 >= 0:  # lewo
                    self.plansza[ind - 1][4] += 1

                if kol + 1 <= kolumna - 1:  # prawo
                    self.plansza[ind + 1][4] += 1

                if rz - 1 >= 0 and kol - 1 >= 0:  # lewo góra
                    self.plansza[ind - kolumna - 1][4] += 1

                if rz + 1 <= rzad - 1 and kol + 1 <= kolumna - 1:  # prawo dół
                    self.plansza[ind + kolumna + 1][4] += 1

                if rz - 1 >= 0 and kol + 1 <= kolumna - 1:  # prawo góra
                    self.plansza[ind - kolumna + 1][4] += 1

                if rz + 1 <= rzad - 1 and kol - 1 >= 0:  # lewo dół
                    self.plansza[ind + kolumna - 1][4] += 1

        for pole in self.plansza:
            if pole[4] == 0 and pole[3] == False:
                self.pole0 += [pole]


class Gra(Plansza):

    def __init__(self, liczbabomb, rzad, kolumna):
        super().__init__(liczbabomb, rzad, kolumna)

        self.okno = Tk()

        self.backg = "#7e7e7e"
        self.czcionka = font.Font(family='Helvetica', size=24)

        self.okno.configure(bg=self.backg)
        self.okno.title("Minesweeper")
        self.okno.resizable(0, 0)

        self.liczby = [PhotoImage(file="pole0.png"), PhotoImage(file="pole1.png"), PhotoImage(file="pole2.png"),
                  PhotoImage(file="pole3.png"), PhotoImage(file="pole4.png")
            , PhotoImage(file="pole5.png"), PhotoImage(file="pole6.png"), PhotoImage(file="pole7.png")]

        self.tlo = PhotoImage(file='tlo.png')
        self.start = PhotoImage(file='start.png')
        self.ipole1 = PhotoImage(file="pole.png")
        self.ipole2 = PhotoImage(file="polee.png")
        self.ibomb = PhotoImage(file="bomba.png")
        self.iflaga = PhotoImage(file='flaga.png')
        self.ipoles = PhotoImage(file='poles.png')

        self.p_click = 0
        self.czas_startu = 0
        self.odkryte_pola = 0
        self.wynik = 0
        self.licznik_widoczny = liczbabomb
        self.licznik_ukryty = liczbabomb


        self.rzad = rzad
        self.kolumna = kolumna
        self.liczbabomb = liczbabomb

        self.rel = SUNKEN

        print(self.rzad)

        self.rysowanieplanszy()

    def rysowanieplanszy(self):
        """na podstawie listy plansza wyswietla plansze"""

        losowepole = random.choice(self.pole0)

        for pole in self.plansza:
            if pole[3] == False:
                print(self.ipole1)
                if pole[1] % 2 == 0 and pole[2] % 2 == 0 or pole[1] % 2 != 0 and pole[2] % 2 != 0:
                    przycisk = Button(self.okno, image=self.ipole1, borderwidth=0, activebackground=self.backg, bg=self.backg, relief=self.rel)
                else:
                    przycisk = Button(self.okno, image=self.ipole2, borderwidth=0, activebackground=self.backg,
                                      bg=self.backg, relief=self.rel)
                przycisk.bind("<Button-1>", self.lpm)
                przycisk.bind("<Button-3>", self.flaga)

                przycisk.grid(column=pole[2], row=pole[1])

            elif pole[3] == True:
                if pole[1] % 2 == 0 and pole[2] % 2 == 0 or pole[1] % 2 != 0 and pole[2] % 2 != 0:
                    przycisk = Button(self.okno, image=self.ipole1, borderwidth=0, activebackground=self.backg,
                                      bg=self.backg, relief=self.rel)
                else:
                    przycisk = Button(self.okno, image=self.ipole2, borderwidth=0, activebackground=self.backg,
                                      bg=self.backg, relief=self.rel)
                przycisk.bind("<Button-1>", self.koniec_gry)
                przycisk.bind("<Button-3>", self.flaga)

                przycisk.grid(column=pole[2], row=pole[1])

        przycisk = Button(self.okno, image=self.ipoles, borderwidth=0, bg=self.backg, activebackground=self.backg, relief=self.rel)
        przycisk.bind("<Button-1>", self.lpm)
        przycisk.bind("<Button-3>", self.flaga)

        przycisk.grid(column=losowepole[2], row=losowepole[1])


        domenu = Button(self.okno, bg=self.backg, text="Powrot do menu", command=self.powrot_do_menu).grid(row=3, column=self.kolumna)
        label_rozmiar = Label(self.okno, bg=self.backg, font=self.czcionka, text="Rozmiar planszy: {}x{}".format(self.rzad, self.kolumna)).grid(row=4, column=self.kolumna)
        label_iloscbomb = Label(self.okno, bg=self.backg, font=self.czcionka, text="Ilość bomb: {}".format(self.liczbabomb)).grid(row=5, column=self.kolumna)
        label_wynik = Label(self.okno, bg=self.backg, font=self.czcionka, text="Twój wynik to: {}".format(self.wynik)).grid(row=6, column=self.kolumna)
        nowagra = Button(self.okno, image=self.start, borderwidth=0, command=self.nowa_gra, bg=self.backg, activebackground=self.backg).grid(column=self.kolumna, rowspan=2, row=7)
        naglowek = Label(self.okno, bg=self.backg, image=self.tlo).grid(row=0, rowspan=2, column=self.kolumna)



    def click(self):
        """zwraca rzad i kolumne pola ktore zostalo nacisniete"""
        xx = self.okno.winfo_pointerx() - self.okno.winfo_x()
        yy = self.okno.winfo_pointery() - self.okno.winfo_y()

        return ((yy - 31) // 42, (xx - 8) // 42)

    def lpm(self, event):
        """odkrywa pole"""
        self.pos = self.click()

        if self.p_click == 0:
            self.p_click += 1
            self.czas_startu += time.time()

        for i in range(self.pos[0] * self.kolumna, (self.pos[0] + 1) * self.kolumna):

            if self.plansza[i][2] == self.pos[1]:
                bomby_przylegle = self.plansza[i][4]

                self.odkryte_pola += 1

                self.plansza[i][5] = None
                przycisk = Button(self.okno, image=self.liczby[bomby_przylegle], bg=self.backg, activebackground=self.backg, borderwidth=0, relief=self.rel)
                przycisk.bind("<Button-1>", self.lpm_na_pole)
                przycisk.grid(column=self.pos[1], row=self.pos[0])
                if bomby_przylegle == 0:
                    self.lpm_na_pole(event, (self.pos[0], self.pos[1]))


        if self.odkryte_pola + self.liczbabomb == self.kolumna * self.rzad:
            self.koniec_gry('wygrana')


    def flaga(self, event):
        """flaguje pole"""
        self.pos = self.click()

        for i in range(self.pos[0] * self.kolumna, (self.pos[0] + 1) * self.kolumna):
            if self.plansza[i][2] == self.pos[1]:
                self.plansza[i][5] = True
                break

        if self.plansza[i][3] == True:
            self.licznik_ukryty -= 1

        self.wynik += self.liczbabomb / 10 * self.licznik_widoczny
        label_wynik = Label(self.okno, bg=self.backg, font=self.czcionka,
                            text="Twój wynik to: {:.0f}".format(self.wynik / (time.time() - self.czas_startu)))
        label_wynik.grid(row=6, column=self.kolumna)

        self.licznik_widoczny -= 1
        label_iloscbomb = Label(self.okno, bg=self.backg, font=self.czcionka, text="Ilość bomb: {}".format(self.licznik_widoczny))
        label_iloscbomb.grid(row=5, column=self.kolumna)

        flaga = Button(self.okno, image=self.iflaga, bg=self.backg, activebackground=self.backg, borderwidth=0)
        flaga.bind("<Button-3>", self.nflaga)

        flaga.grid(row=self.pos[0], column=self.pos[1])


    def nflaga(self, event):
        """usuwa flage z pola"""
        self.pos = self.click()

        self.licznik_widoczny += 1

        label_iloscbomb = Label(self.okno, bg=self.backg, font=self.czcionka,
                                text="  Ilość bomb: {}".format(self.licznik_widoczny)).grid(row=5, column=self.kolumna,
                                                                                            columnspan=2)

        self.wynik -= self.liczbabomb / 10 * self.licznik_widoczny
        label_wynik = Label(self.okno, bg=self.backg, font=self.czcionka,
                            text="Twój wynik to: {:.0f}".format(self.wynik / (time.time() - self.czas_startu)))
        label_wynik.grid(row=6, column=self.kolumna)

        for i in range(self.pos[0] * self.kolumna, (self.pos[0] + 1) * self.kolumna):
            if (self.plansza[i][1], self.plansza[i][2]) == self.pos:
                self.plansza[i][5] = False
                szukanepole = i
                break



        if self.plansza[szukanepole][3] == False:

            przycisk = Button(self.okno, image=self.ipole1, borderwidth=0, bg=self.backg, activebackground=self.backg, relief=self.rel)
            przycisk.bind("<Button-1>", self.lpm)
            przycisk.bind("<Button-3>", self.flaga)
            przycisk.grid(column=self.plansza[szukanepole][2], row=self.plansza[szukanepole][1])

        elif self.plansza[szukanepole][3] == True:

            self.licznik_ukryty += 1

            przycisk = Button(self.okno, image=self.ipole1, borderwidth=0, bg=self.backg, activebackground=self.backg, relief=self.rel)
            przycisk.bind("<Button-1>", self.koniec_gry)
            przycisk.bind("<Button-3>", self.flaga)
            przycisk.grid(column=self.plansza[szukanepole][2], row=self.plansza[szukanepole][1])


    def lpm_na_pole(self, event, x=()):
        """po nacisnieciu na odkryte pole odkrywa wszystkie pobliskie pola które są bezpieczne"""

        if x == ():
            pos = self.click()
            rz = pos[0]
            kol = pos[1]
        else:
            rz = x[0]
            kol = x[1]



        for i in range(rz * self.kolumna, (rz + 1) * self.kolumna):

            if self.plansza[i][2] == kol:
                wymagane_pola = self.plansza[i][4]
                indeks = i
                break


        self.plansza[indeks][6] = True

        pola_dookola = 0
        bezpieczne_pola = 0
        lista_nieodkrytych_pol = []

        if rz - 1 >= 0:  # góra
            g = self.plansza[indeks - self.kolumna]
            pola_dookola += 1
            if g[5] == True:
                bezpieczne_pola += 1
            if g[5] == False:
                lista_nieodkrytych_pol += [g]

        if rz + 1 <= self.rzad - 1:  # dół
            d = self.plansza[indeks + self.kolumna]
            pola_dookola += 1
            if d[5] == True:
                bezpieczne_pola += 1
            if d[5] == False:
                lista_nieodkrytych_pol += [d]

        if kol - 1 >= 0:  # lewo
            l = self.plansza[indeks - 1]
            pola_dookola += 1
            if l[5] == True:
                bezpieczne_pola += 1
            if l[5] == False:
                lista_nieodkrytych_pol += [l]

        if kol + 1 <= self.kolumna - 1:  # prawo
            p = self.plansza[indeks + 1]
            pola_dookola += 1
            if p[5] == True:
                bezpieczne_pola += 1
            if p[5] == False:
                lista_nieodkrytych_pol += [p]

        if rz - 1 >= 0 and kol - 1 >= 0:  # lewo góra
            gl = self.plansza[indeks - self.kolumna - 1]
            pola_dookola += 1
            if gl[5] == True:
                bezpieczne_pola += 1
            if gl[5] == False:
                lista_nieodkrytych_pol += [gl]

        if rz + 1 <= self.rzad - 1 and kol + 1 <= self.kolumna - 1:  # prawo dół
            dp = self.plansza[indeks + self.kolumna + 1]
            pola_dookola += 1
            if dp[5] == True:
                bezpieczne_pola += 1
            if dp[5] == False:
                lista_nieodkrytych_pol += [dp]

        if rz - 1 >= 0 and kol + 1 <= self.kolumna - 1:  # prawo góra\
            gp = self.plansza[indeks - self.kolumna + 1]
            pola_dookola += 1
            if gp[5] == True:
                bezpieczne_pola += 1
            if gp[5] == False:
                lista_nieodkrytych_pol += [gp]

        if rz + 1 <= self.rzad - 1 and kol - 1 >= 0:  # lewo dół
            dl = self.plansza[indeks + self.kolumna - 1]
            pola_dookola += 1
            if dl[5] == True:
                bezpieczne_pola += 1
            if dl[5] == False:
                lista_nieodkrytych_pol += [dl]


        if bezpieczne_pola == wymagane_pola:
            for k in lista_nieodkrytych_pol:
                if k[3] == True:
                    self.koniec_gry()
                elif k[3] == False:
                    self.odkryte_pola += 1
                    self.plansza[k[0]][5] = None
                    liczba_na_polu = k[4]
                    przycisk = Button(self.okno, image=self.liczby[liczba_na_polu], bg=self.backg,
                                      activebackground=self.backg, borderwidth=0, relief=self.rel)
                    przycisk.bind("<Button-1>", self.lpm_na_pole)
                    przycisk.grid(row=k[1], column=k[2])


            if kol - 1 >= 0 and \
                    l[4] == 0 and \
                    l[6] == None:  # lewo
                self.lpm_na_pole(event, (l[1], l[2]))

            if rz - 1 >= 0 and \
                    g[4] == 0 and \
                    g[6] == None:  # gora
                self.lpm_na_pole(event, (g[1], g[2]))

            if kol + 1 <= self.kolumna - 1 and \
                    p[4] == 0 and \
                    p[6] == None:  # prawo
                self.lpm_na_pole(event, (p[1], p[2]))

            if rz + 1 <= self.rzad - 1 and \
                    d[4] == 0 and \
                    d[6] == None:  # dol
                self.lpm_na_pole(event, (d[1], d[2]))

            if rz + 1 <= self.rzad - 1 and \
                    kol - 1 >= 0 and \
                    dl[4] == 0 and \
                    dl[6] == None:  # lewo dol
                self.lpm_na_pole(event, (dl[1], dl[2]))

            if rz + 1 <= self.rzad - 1 and \
                    kol + 1 <= self.kolumna - 1 and \
                    dp[4] == 0 and \
                    dp[6] == None:  # prawo dol
                self.lpm_na_pole(event, (dp[1], dp[2]))

            if rz - 1 >= 0 and \
                    kol + 1 <= self.kolumna - 1 and \
                    gp[4] == 0 and \
                    gp[6] == None:  # prawo góra
                self.lpm_na_pole(event, (gp[1], gp[2]))

            if rz - 1 >= 0 and \
                    kol - 1 >= 0 and \
                    gl[4] == 0 and \
                    gl[6] == None:  # góra lewo
                self.lpm_na_pole(event, (gl[1], gl[2]))

            if self.odkryte_pola + self.liczbabomb == self.kolumna * self.rzad:
                self.odkryte_pola -= 1
                self.koniec_gry('wygrana')

    def koniec_gry(self, status=None, event=None):
        """odkrywa cala plansze po przegranej lub wszystkie bomby po wygranej"""
        for p in self.plansza:
            if p[3] == False:
                bombyprzylegle = p[4]
                koniecgry = Label(self.okno, image=self.liczby[bombyprzylegle], bg=self.backg, activebackground=self.backg, borderwidth=1, relief=self.rel)
                koniecgry.grid(column=p[2], row=p[1])

            elif p[3] == True:
                koniecgry = Label(self.okno, image=self.ibomb, bg=self.backg, activebackground=self.backg, borderwidth=1, relief=self.rel)
                koniecgry.grid(column=p[2], row=p[1])

        czas_konca = time.time()
        czas_gry = czas_konca - self.czas_startu
        self.stats = Stats(czas_gry, self.wynik, status, self.liczbabomb)

    def nowa_gra(self):
        """generuje nowa plansze"""
        self.okno.destroy()
        try:
            self.stats.wygrana.destroy()
            gra = Gra(self.liczbabomb, self.rzad, self.kolumna)
        except:
            gra = Gra(self.liczbabomb, self.rzad, self.kolumna)

    def powrot_do_menu(self):
        """zamyka gre i wraca do menu"""
        try:
            self.stats.wygrana.destroy()
            self.okno.destroy()
            menu = Menu()
            menu.rysowanie()
        except:
            self.okno.destroy()
            menu = Menu()
            menu.rysowanie()

class Stats:
    def __init__(self, czas, wynik, status, level):
        self.wygrana = Tk()
        self.wygrana.resizable(0,0)
        self.wygrana.title("Gratulację!")
        self.backg = "#126748"
        self.wygrana.configure(bg=self.backg)
        self.czcionka = font.Font(family='Helvetica', size=24)

        self.czas, self.wynik, self.status, self.level= (czas, wynik, status, level)


        self.okno(self.czas, self.wynik, self.status, self.level)

    def okno(self,czas_gry, wynik, status, level):
        """wyglad okna"""
        if status == 'wygrana':
            label = Label(self.wygrana, font=self.czcionka, fg='white', bg=self.backg,
                          text='Udało ci się rozbroić wszystkie miny w czasie {:.2f} sekund\n'
                                              'Twój wynik to {:.0f}  '.format(czas_gry, wynik / czas_gry))
            self.zapisz_wynik(self.wynik / self.czas, self.czas, self.level)

        else:
            label = Label(self.wygrana, font=self.czcionka, fg='white', bg=self.backg,
                          text='Nie udało ci się rozbroić wszystkich min, twój czas to {:.2f} sekund\n'
                               'Twój wynik to {:.0f}  '.format(czas_gry, wynik / (czas_gry * 10)))


        label.grid(row=0, column=0)

    def zamknij(self):
        self.wygrana.destroy()

    def zapisz_wynik(self, wynik, czas, liczbabomb, name='anonymous'):
        file = open('wyniki.txt', 'a')
        if liczbabomb == 10:
            level = 'easy'
        elif liczbabomb == 40:
            level = 'medium'
        elif liczbabomb == 99:
            level = 'expert'

        print('{};{:.2f};{};{}'.format(name, czas, str(wynik), level), file=file)

        file.close()





menu = Menu()
menu.rysowanie()