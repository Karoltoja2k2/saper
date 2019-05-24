from tkinter import *
import random
from tkinter import font
import time

def ekranstartowy():
    """menu glowne"""
    menu = Tk()

    menu.title("Minesweeper")
    backg = "#126748"
    menu.configure(bg=backg)
    tlo = PhotoImage(file='tlo.png')
    latwa = PhotoImage(file='latwa.png')
    srednia = PhotoImage(file='srednia.png')
    expert = PhotoImage(file='expert.png')
    ranking = PhotoImage(file='ranking.png')
    osiagniecia = PhotoImage(file='osiagniecia.png')
    staty = PhotoImage(file='staty1.png')

    class Menu:

        def latwy(self):
            """wybór poziomu i start gry"""
            menu.destroy()
            main(1)

        def sredni(self):
            menu.destroy()
            main(2)

        def trudny(self):
            menu.destroy()
            main(3)

        def rank(self):
            """otwiera okno rankingu"""
            ranks()



        def rysowanie(self):
            """wyglad menu glownego"""
            odstep3 = Label(menu, bg=backg)
            odstep3.grid(row=0, column=0)

            napis = Label(menu, image=tlo, borderwidth=0, activebackground=backg, bg=backg)
            napis.grid(row=0, columnspan=3)

            odstep = Label(menu, bg=backg, text='   ')
            odstep.grid(column=0, row=1)

            R1 = Button(menu, image=latwa, bg=backg, borderwidth=0, activebackground=backg, command=menus.latwy)
            R1.grid(column=1, row=2)

            R2 = Button(menu, image=srednia, bg=backg, borderwidth=0, activebackground=backg, command=menus.sredni)
            R2.grid(column=1, row=3)

            R3 = Button(menu, image=expert, bg=backg,borderwidth=0, activebackground=backg, command=menus.trudny)
            R3.grid(column=1, row=6)

            odstep2 = Label(menu, bg=backg)
            odstep2.grid(column=0, row=7)

            posiagniecia = Button(menu, image=osiagniecia, bg=backg, borderwidth=0, activebackground=backg)
            posiagniecia.grid(row=3, column=2)

            pranking = Button(menu, image=ranking, borderwidth=0, activebackground=backg, bg=backg, command=menus.rank)
            pranking.grid(row=2, column=2)

            odstep4 = Label(menu, bg=backg, text="    ")
            odstep4.grid(row=1, column=1)
            odstep5 = Label(menu, bg=backg, text="     ")
            odstep5.grid(row=0, column=3)

            pstaty = Label(menu, image=staty, borderwidth=0)
            pstaty.grid(row=8, columnspan=3)

            odstep7 = Label(menu, bg=backg)
            odstep7.grid(column=0, row=9)

            menu.mainloop()



    menus=Menu()
    menus.rysowanie()


def staty(czas, wynik):
    """koncowe statystyki"""
    czcionka = font.Font(family='Helvetica', size=24)


    class Statystyki:

        wygrana = Tk()
        wygrana.title("Gratulację!")
        backg = "#126748"
        wygrana.configure(bg=backg)

        def okno(self,czas_gry, w):
            """wyglad okna"""
            label = Label(stats.wygrana, font=czcionka, fg='white', bg=stats.backg,
                          text='Udało ci się rozbroić wszystkie miny w czasie {:.2f} sekund\n'
                                              'Twój wynik to {:.0f}  '.format(czas_gry, w / czas_gry))
            label.grid(row=0, column=0)

        def zamknij(self):
            stats.wygrana.destroy()

    stats=Statystyki()
    stats.okno(czas, wynik)




def main(poziom):
    """ekran gry"""


    class Saper:


        p_click = 0
        czas_startu = 0
        pola0 = []

        if poziom == 1:
            ustawienia = [9, 9, 10]

        if poziom == 2:
            ustawienia = [16, 16, 40]

        if poziom == 3:
            ustawienia = [16, 30, 99]

        rzad = ustawienia[0]
        kolumna = ustawienia[1]
        liczbabomb = ustawienia[2]

        liczbabomb_stala = ustawienia[2]
        wynik = 0

        licznik_widoczny = liczbabomb
        licznik_ukryty = liczbabomb

        def nowa_gra(self):
            """generuje nowa plansze"""
            okno.destroy()
            main(poziom)

        def powrot_do_menu(self):
            """zamyka gre i wraca do menu"""
            okno.destroy()
            ekranstartowy()

        def koniec_gry(self, event=None):
            """odkrywa cala plansze po przegranej lub wszystkie bomby po wygranej"""
            for p in plansza:
                if p[3] == False:
                    bombyprzylegle=p[4]
                    koniecgry = Label(okno, image=liczby[bombyprzylegle],bg=backg, activebackground=backg, borderwidth=0)
                    koniecgry.grid(column=p[2], row=p[1])

                elif p[3] == True:
                    koniecgry = Label(okno, image=ibomb, bg=backg, activebackground=backg, borderwidth=0)
                    koniecgry.grid(column=p[2], row=p[1])



        def click(self):
            """zwraca rzad i kolumne pola ktore zostalo nacisniete"""
            xx = okno.winfo_pointerx() - okno.winfo_x()
            yy = okno.winfo_pointery() - okno.winfo_y()

            return((yy - 31) // 42, (xx - 8) // 42)

        def nflaga(self,event):
            """usuwa flage z pola"""
            pos=saps.click()

            saps.licznik_widoczny += 1
            label_iloscbomb = Label(okno, bg=backg, font=czcionka, text="Ilość bomb: {}".format(saps.licznik_widoczny)).grid(row=5, column=saps.kolumna + 1)

            for i in range(pos[0] * saps.kolumna, (pos[0] + 1) * saps.kolumna):
                if (plansza[i][1], plansza[i][2]) == pos:
                    plansza[i][5] = False
                    szukanepole = i
                    break

            if plansza[i][3] == False:

                przycisk = Button(okno, image=ipole, borderwidth=0, bg=backg, activebackground=backg)
                przycisk.bind("<Button-1>", saps.lpm)
                przycisk.bind("<Button-3>", saps.flaga)
                przycisk.grid(column=plansza[szukanepole][2], row=plansza[szukanepole][1])

            elif plansza[i][3] == True:


                saps.licznik_ukryty += 1

                przycisk = Button(okno, image=ipole, borderwidth=0, bg=backg, activebackground=backg)
                przycisk.bind("<Button-1>", saps.koniec_gry)
                przycisk.bind("<Button-3>", saps.flaga)
                przycisk.grid(column=plansza[szukanepole][2], row=plansza[szukanepole][1])

            if saps.licznik_ukryty == 0 and saps.licznik_ukryty == saps.licznik_widoczny:
                saps.koniec_gry()
                czas_konca = time.time()
                czas_gry = czas_konca - saps.czas_startu
                staty(czas_gry, saps.wynik)


        def flaga(self, event):
            """flaguje pole"""
            pos=saps.click()

            for i in range(pos[0] * saps.kolumna, (pos[0] + 1) * saps.kolumna):
                if plansza[i][2] == pos[1]:
                    plansza[i][5] = True
                    break

            if plansza[i][3] == True:
                saps.licznik_ukryty -= 1

            saps.wynik += saps.liczbabomb_stala/10 * saps.licznik_widoczny
            label_wynik = Label(okno, bg=backg, font=czcionka,
                                text="Twój wynik to: {:.0f}   ".format(saps.wynik/(time.time()-saps.czas_startu)))
            label_wynik.grid(row=6, column=saps.kolumna + 1)

            saps.licznik_widoczny -= 1
            label_iloscbomb = Label(okno, bg=backg, font=czcionka, text="Ilość bomb: {}".format(saps.licznik_widoczny))
            label_iloscbomb.grid(row=5, column=saps.kolumna + 1)

            flaga=Button(okno, image=iflaga,bg=backg, activebackground=backg, borderwidth=0)
            flaga.bind("<Button-3>", saps.nflaga)

            flaga.grid(row=pos[0],column=pos[1])

            if saps.licznik_ukryty == 0 and saps.licznik_ukryty == saps.licznik_widoczny:
                saps.koniec_gry()
                czas_konca = time.time()
                czas_gry = czas_konca - saps.czas_startu
                staty(czas_gry, saps.wynik)

        def lpm_na_pole(self,event, x = ()):
            """po nacisnieciu na odkryte pole odkrywa wszystkie pobliskie pola z liczba 0"""
            if x == ():
                pos = saps.click()
                rz = pos[0]
                kol = pos[1]
            else:
                rz = x[0]
                kol = x[1]

            lista_nieodkrytych_pol=[]

            for i in range(rz * saps.kolumna, (rz + 1) * saps.kolumna):

                if plansza[i][2] == kol:
                    wymagane_pola = plansza[i][4]
                    indeks=i
                    break

            plansza[indeks][6] = True

            pola_dookola = 0
            bezpieczne_pola = 0

            if rz - 1 >= 0:  # góra
                pola_dookola += 1
                if plansza[indeks-saps.kolumna][5] == True:
                    bezpieczne_pola += 1
                if plansza[indeks - saps.kolumna][5] == False:
                    lista_nieodkrytych_pol += [plansza[indeks-saps.kolumna]]



            if rz + 1 <= saps.rzad - 1:  # dół
                pola_dookola += 1
                if plansza[indeks+saps.kolumna][5] == True:
                    bezpieczne_pola += 1
                if plansza[indeks + saps.kolumna][5] == False:
                    lista_nieodkrytych_pol += [plansza[indeks+saps.kolumna]]

            if kol - 1 >= 0:  # lewo
                pola_dookola += 1
                if plansza[indeks - 1][5] == True:
                    bezpieczne_pola += 1
                if plansza[indeks - 1][5] == False:
                    lista_nieodkrytych_pol += [plansza[indeks - 1]]

            if kol + 1 <= saps.kolumna - 1:  # prawo
                pola_dookola += 1
                if plansza[indeks+1][5] == True:
                    bezpieczne_pola += 1
                if plansza[indeks + 1][5] == False:
                    lista_nieodkrytych_pol += [plansza[indeks + 1]]

            if rz - 1 >= 0 and kol - 1 >= 0:  # lewo góra
                pola_dookola += 1
                if plansza[indeks-saps.kolumna-1][5] == True:
                    bezpieczne_pola += 1
                if plansza[indeks - saps.kolumna - 1][5] == False:
                    lista_nieodkrytych_pol += [plansza[indeks - saps.kolumna - 1]]

            if rz + 1 <= saps.rzad - 1 and kol + 1 <= saps.kolumna - 1:  # prawo dół
                pola_dookola += 1
                if plansza[indeks+saps.kolumna+1][5] == True:
                    bezpieczne_pola += 1
                if plansza[indeks + saps.kolumna + 1][5] == False:
                    lista_nieodkrytych_pol += [plansza[indeks + saps.kolumna +1 ]]

            if rz - 1 >= 0 and kol + 1 <= saps.kolumna - 1:  # prawo góra\
                pola_dookola += 1
                if plansza[indeks-saps.kolumna+1][5] == True:
                    bezpieczne_pola += 1
                if plansza[indeks - saps.kolumna + 1][5] == False:
                    lista_nieodkrytych_pol += [plansza[indeks - saps.kolumna + 1]]

            if rz + 1 <= saps.rzad - 1 and kol - 1 >= 0:  # lewo dół
                pola_dookola += 1
                if plansza[indeks+saps.kolumna-1][5] == True:
                    bezpieczne_pola += 1
                if plansza[indeks+saps.kolumna-1][5] == False:
                    lista_nieodkrytych_pol += [plansza[indeks + saps.kolumna - 1]]

            if bezpieczne_pola == wymagane_pola:
                for p in lista_nieodkrytych_pol:
                    if p[3] == True:
                        saps.koniec_gry()
                    elif p[3] == False:

                        plansza[p[0]][5] = None
                        liczba_na_polu = p[4]
                        przycisk = Button(okno, image=liczby[liczba_na_polu], bg=backg, activebackground=backg,borderwidth=0)
                        przycisk.bind("<Button-1>", saps.lpm_na_pole)
                        przycisk.grid(row=p[1], column=p[2])

                if kol - 1 >= 0 and                                                                                    \
                        plansza[indeks - 1][4] == 0 and                                                                \
                        plansza[indeks - 1][6] == None:                                                                 # lewo
                    saps.lpm_na_pole(event, (plansza[indeks - 1][1], plansza[indeks - 1][2]))

                if rz - 1 >= 0 and                                                                                     \
                        plansza[indeks - saps.kolumna][4] == 0 and                                                     \
                        plansza[indeks - saps.kolumna][6] == None:                                                      # gora
                    saps.lpm_na_pole(event, (plansza[indeks - saps.kolumna][1], plansza[indeks - saps.kolumna][2]))

                if kol + 1 <= saps.kolumna - 1 and                                                                     \
                        plansza[indeks + 1][4] == 0 and                                                                \
                        plansza[indeks + 1][6] == None:                                                                 # prawo
                    saps.lpm_na_pole(event, (plansza[indeks + 1][1], plansza[indeks + 1][2]))

                if rz + 1 <= saps.rzad - 1 and                                                                         \
                        plansza[indeks + saps.kolumna][4] == 0 and                                                     \
                        plansza[indeks + saps.kolumna][6] == None:                                                      # dol
                    saps.lpm_na_pole(event, (plansza[indeks + saps.kolumna][1], plansza[indeks + saps.kolumna][2]))

                if rz + 1 <= saps.rzad - 1 and                                                                         \
                        kol - 1 >= 0 and                                                                               \
                        plansza[indeks + saps.kolumna - 1][4] == 0 and                                                 \
                        plansza[indeks + saps.kolumna - 1][6] == None:                                                  # lewo dol
                    saps.lpm_na_pole(event, (plansza[indeks + saps.kolumna - 1][1], plansza[indeks + saps.kolumna - 1][2]))

                if rz + 1 <= saps.rzad - 1 and                                                                         \
                        kol + 1 <= saps.kolumna - 1 and                                                                \
                        plansza[indeks + saps.kolumna + 1][4] == 0 and                                                 \
                        plansza[indeks + saps.kolumna + 1][6] == None:                                                  # prawo dol
                    saps.lpm_na_pole(event, (plansza[indeks + saps.kolumna + 1][1], plansza[indeks + saps.kolumna + 1][2]))

                if rz - 1 >= 0 and                                                                                     \
                        kol + 1 <= saps.kolumna - 1 and                                                                \
                        plansza[indeks - saps.kolumna + 1][4] == 0 and                                                 \
                        plansza[indeks - saps.kolumna + 1][6] == None:                                                  # prawo góra
                    saps.lpm_na_pole(event, (plansza[indeks - saps.kolumna + 1][1], plansza[indeks - saps.kolumna + 1][2]))

                if rz - 1 >= 0 and                                                                                     \
                        kol - 1 >= 0 and                                                                               \
                        plansza[indeks - saps.kolumna - 1][4] == 0 and                                                 \
                        plansza[indeks - saps.kolumna - 1][6] == None:                                                  # góra lewo
                    saps.lpm_na_pole(event, (plansza[indeks - saps.kolumna - 1][1], plansza[indeks - saps.kolumna - 1][2]))

        def lpm(self, event):
            """odkrywa zakryte pole"""
            pos = saps.click()

            if saps.p_click == 0:
                saps.p_click += 1
                saps.czas_startu += time.time()

            for i in range(pos[0] * saps.kolumna, (pos[0] + 1) * saps.kolumna):

                 if plansza[i][2] == pos[1]:
                    bomby_przylegle = plansza[i][4]
                    #plansza[i][5]+=1
                    #print(plansza[i][5])
                    plansza[i][5] = None
                    przycisk = Button(okno, image=liczby[bomby_przylegle],bg=backg, activebackground=backg, borderwidth=0)
                    przycisk.bind("<Button-1>", saps.lpm_na_pole)
                    przycisk.grid(column=pos[1], row=pos[0])
                    if bomby_przylegle == 0:
                        saps.lpm_na_pole(event, (pos[0], pos[1]))


        def bomby(self,rzad, kolumna, liczbabomb):
            """generuje oraz zwraca liste bomb"""

            listabomb0 = []
            while len(set(listabomb0)) < liczbabomb:
                bomba = (random.choice(range(rzad)), random.choice(range(kolumna)))

                listabomb0 += [bomba]
                set(listabomb0)

            return listabomb0


        def plansza(self,rzad,kolumna):
            """"generuje liste definiujaca plansze
                indekspola; rząd; kolumna; bomba t/f; liczba na polu; pole odkryte/oflagowane; blokada rekruencji funkcji lpm_na_pole
            """

            plansza0 = []
            indekspola = -1
            liczba = 0

            for rz in range(rzad):
                for kol in range(kolumna):

                    indekspola = indekspola + 1
                    plansza0 += [[indekspola, rz, kol, False, liczba, False, None]]
                    for b in bomby:
                        if b == (rz, kol):
                            plansza0[indekspola][3] = True
            return plansza0



        def sasiadbomby(self,kolumna,rzad):
            """oblicza ilosc bomb na przyleglych polach i modyfikuje czwarty element w danych pola w liscie plansza"""
            for pole in plansza:
                if pole[3] == True:

                    rz = pole[1]
                    kol = pole[2]
                    ind = pole[0]

                    if rz - 1 >= 0:  # góra
                        plansza[ind - kolumna][4] += 1

                    if rz + 1 <= rzad - 1:  # dół
                        plansza[ind + kolumna][4] += 1

                    if kol - 1 >= 0:  # lewo
                        plansza[ind - 1][4] += 1

                    if kol + 1 <= kolumna - 1:  # prawo
                        plansza[ind + 1][4] += 1

                    if rz - 1 >= 0 and kol - 1 >= 0:  # lewo góra
                        plansza[ind - kolumna - 1][4] += 1

                    if rz + 1 <= rzad - 1 and kol + 1 <= kolumna - 1:  # prawo dół
                        plansza[ind + kolumna + 1][4] += 1

                    if rz - 1 >= 0 and kol + 1 <= kolumna - 1:  # prawo góra
                        plansza[ind - kolumna + 1][4] += 1

                    if rz + 1 <= rzad - 1 and kol - 1 >= 0:  # lewo dół
                        plansza[ind + kolumna - 1][4] += 1

            for pole in plansza:
                if pole[4] == 0 and pole[3] == False:
                    saps.pola0 += [pole]


        def rysowanieplanszy(self):
            """na podstawie listy plansza wyswietla plansze"""

            losowepole=random.choice(saps.pola0)

            for pole in plansza:
                if pole[3] == False:
                    przycisk = Button(okno, image=ipole, borderwidth=0, bg=backg,activebackground=backg)
                    przycisk.bind("<Button-1>", saps.lpm)
                    przycisk.bind("<Button-3>", saps.flaga)

                    przycisk.grid(column=pole[2], row=pole[1])

                elif pole[3] == True:
                    przycisk = Button(okno, image=ipole, borderwidth=0, bg=backg,activebackground=backg)
                    przycisk.bind("<Button-1>",saps.koniec_gry)
                    przycisk.bind("<Button-3>", saps.flaga)

                    przycisk.grid(column=pole[2], row=pole[1])

            przycisk = Button(okno, image=liczby[0], borderwidth=0, bg=backg, activebackground=backg)
            przycisk.bind("<Button-1>", saps.lpm)
            przycisk.bind("<Button-3>", saps.flaga)

            przycisk.grid(column=losowepole[2], row=losowepole[1])


            domenu=Button(okno, bg=backg, text="Powrot do menu", command=saps.powrot_do_menu).grid(row = 3, column = saps.kolumna+1)
            label_rozmiar = Label(okno, bg=backg,font=czcionka, text="Rozmiar planszy: {}x{}".format(saps.rzad, saps.kolumna)).grid(row = 4, column = saps.kolumna+1)
            label_iloscbomb = Label(okno, bg=backg,font=czcionka, text = "Ilość bomb: {}  ".format(saps.liczbabomb)).grid(row = 5, column = saps.kolumna+1)
            label_wynik = Label(okno, bg=backg,font=czcionka, text="Twój wynik to: {}".format(saps.wynik)).grid(row = 6, column = saps.kolumna+1)
            nowagra = Button(okno, text="Zagraj jeszcze raz", font=czcionka, command=saps.nowa_gra).grid(column=saps.kolumna + 1, rowspan=2, row=7)

            okno.mainloop()

    okno=Tk()


    backg="#126748"
    czcionka = font.Font(family='Helvetica', size=24)

    okno.configure(bg=backg,)
    okno.title("Minesweeper")
    liczby=[PhotoImage(file="pole0.png"),PhotoImage(file="pole1.png"),PhotoImage(file="pole2.png"),PhotoImage(file="pole3.png"),PhotoImage(file="pole4.png")
        ,PhotoImage(file="pole5.png"),PhotoImage(file="pole6.png"),PhotoImage(file="pole7.png")]

    ipole = PhotoImage(file="pole.png")
    ibomb = PhotoImage(file="bomba.png")
    iflaga= PhotoImage(file='flaga.png')

    if __name__ == '__main__':

        saps=Saper()

        bomby=saps.bomby(saps.rzad, saps.kolumna, saps.liczbabomb)
        plansza=saps.plansza(saps.rzad, saps.kolumna)
        #listabomb=saps.drugalistabomb()
        saps.sasiadbomby(saps.kolumna, saps.rzad)

        saps.rysowanieplanszy()


def ranks():

    class Ranking:

        backg = "#126748"

        czcionka = font.Font(family='Arial', size=72)
        ranking=Tk()
        ranking.configure(bg=backg )
        ranking.title("Minesweeper")

        def pokaz(self):
            ranking.mainloop()

        naglowek=Label(ranking, text='Ranking', font=czcionka, bg= backg)
        naglowek.pack()

    rank=Ranking()
    rank.pokaz




ekranstartowy()







































