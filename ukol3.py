import tkinter as tk
import random

# Konstanty hry
SIRKA_OKNA = 600
VYSKA_OKNA = 400
VELIKOST_POLE = 20
RYCHLOST = 100 # v milisekundách (nižší = rychlejší)

class HadHra:
    def __init__(self):
        self.okno = tk.Tk()
        self.okno.title("Hra Had - Úkol 3 (Hrušky & Restart)")
        self.okno.resizable(False, False)

        self.platno = tk.Canvas(self.okno, bg="black", width=SIRKA_OKNA, height=VYSKA_OKNA)
        self.platno.pack()

        self.okno.bind("<KeyPress>", self.zpracuj_klavesu)
        self.inicializuj_hru()
        self.okno.mainloop()

    def inicializuj_hru(self):
        # Vyčištění plátna při restartu
        self.platno.delete("all")
        
        self.had = [(100, 100), (80, 100), (60, 100)]
        self.smer = "Right"
        self.jidlo = None
        self.skore = 0
        self.bezi = True

        self.text_skore = self.platno.create_text(
            50, 20, text=f"Skóre: {self.skore}", fill="white", font=("Arial", 14)
        )

        self.vytvor_hrusku()
        self.hlavni_smycka()

    def vytvor_hrusku(self):
        while True:
            x = random.randint(0, (SIRKA_OKNA // VELIKOST_POLE) - 1) * VELIKOST_POLE
            y = random.randint(0, (VYSKA_OKNA // VELIKOST_POLE) - 1) * VELIKOST_POLE
            self.jidlo = (x, y)
            if self.jidlo not in self.had:
                break
        
        self.platno.delete("jidlo")
        # Vykreslení hrušky (zelený ovál + hnědá stopka)
        # Stopka
        self.platno.create_line(
            x + VELIKOST_POLE//2, y, x + VELIKOST_POLE//2, y - 5, 
            fill="brown", width=2, tag="jidlo"
        )
        # Tělo hrušky
        self.platno.create_oval(
            x + 2, y + 2, x + VELIKOST_POLE - 2, y + VELIKOST_POLE, 
            fill="#91ff00", outline="green", tag="jidlo"
        )

    def zpracuj_klavesu(self, event):
        klavesa = event.keysym
        
        # Restart hry
        if not self.bezi and klavesa.lower() == 'r':
            self.inicializuj_hru()
            return

        # Změna směru
        protislovy = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if klavesa in ["Up", "Down", "Left", "Right"]:
            if klavesa != protislovy.get(self.smer):
                self.smer = klavesa

    def hlavni_smycka(self):
        if self.bezi:
            self.pohyb()
            self.kontrola_kolize()
            self.vykresli()
            self.okno.after(RYCHLOST, self.hlavni_smycka)

    def pohyb(self):
        hlava_x, hlava_y = self.had[0]

        if self.smer == "Up":
            hlava_y -= VELIKOST_POLE
        elif self.smer == "Down":
            hlava_y += VELIKOST_POLE
        elif self.smer == "Left":
            hlava_x -= VELIKOST_POLE
        elif self.smer == "Right":
            hlava_x += VELIKOST_POLE

        nova_hlava = (hlava_x, hlava_y)
        self.had.insert(0, nova_hlava)

        if hlava_x == self.jidlo[0] and hlava_y == self.jidlo[1]:
            self.skore += 1
            self.platno.itemconfig(self.text_skore, text=f"Skóre: {self.skore}")
            self.vytvor_hrusku()
        else:
            self.had.pop()

    def kontrola_kolize(self):
        hlava_x, hlava_y = self.had[0]

        if (hlava_x < 0 or hlava_x >= SIRKA_OKNA or 
            hlava_y < 0 or hlava_y >= VYSKA_OKNA):
            self.konec_hry()

        if (hlava_x, hlava_y) in self.had[1:]:
            self.konec_hry()

    def vykresli(self):
        self.platno.delete("had")
        for i, (x, y) in enumerate(self.had):
            barva = "#00FF00" if i == 0 else "#228B22"
            self.platno.create_rectangle(
                x, y, x + VELIKOST_POLE, y + VELIKOST_POLE, fill=barva, tag="had", outline="black"
            )

    def konec_hry(self):
        self.bezi = False
        self.platno.create_rectangle(
            SIRKA_OKNA//4, VYSKA_OKNA//4, 3*SIRKA_OKNA//4, 3*VYSKA_OKNA//4, 
            fill="black", outline="white"
        )
        self.platno.create_text(
            SIRKA_OKNA // 2, VYSKA_OKNA // 2 - 20,
            text="KONEC HRY", fill="red", font=("Arial", 24, "bold")
        )
        self.platno.create_text(
            SIRKA_OKNA // 2, VYSKA_OKNA // 2 + 20,
            text=f"Skóre: {self.skore}", fill="white", font=("Arial", 16)
        )
        self.platno.create_text(
            SIRKA_OKNA // 2, VYSKA_OKNA // 2 + 50,
            text="Stiskni 'R' pro restart", fill="yellow", font=("Arial", 12)
        )

if __name__ == "__main__":
    HadHra()
