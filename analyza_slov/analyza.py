import re
from collections import Counter
import sys
import os

# Pokus o import matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

def analyzuj_text(text):
    if not text:
        print("Nebyl zadán žádný text.")
        return

    # Věty
    vety = [v for v in re.split(r'[.!?]+', text) if v.strip()]
    pocet_vet = len(vety)

    # Slova
    slova = text.lower().split()
    cista_slova = [s.strip(".,!?:;\"'()") for s in slova]
    cista_slova = [s for s in cista_slova if s]
    
    pocet_slov = len(cista_slova)
    pocet_unikatnich = len(set(cista_slova))
    
    if pocet_slov > 0:
        prumerna_delka = sum(len(s) for s in cista_slova) / pocet_slov
    else:
        prumerna_delka = 0

    pocitadlo = Counter(cista_slova)
    nejcastejsi = pocitadlo.most_common(5)

    # Tabulkový výstup
    print("\n" + "="*45)
    print(f"{'Metrika':<30} | {'Hodnota':<10}")
    print("-" * 45)
    print(f"{'Počet slov':<30} | {pocet_slov:<10}")
    print(f"{'Počet vět':<30} | {pocet_vet:<10}")
    print(f"{'Počet unikátních slov':<30} | {pocet_unikatnich:<10}")
    print(f"{'Průměrná délka slova':<30} | {prumerna_delka:<10.2f}")
    print("-" * 45)
    print("\nTop 5 nejčastějších slov:")
    print(f"{'Slovo':<30} | {'Četnost':<10}")
    print("-" * 45)
    for slovo, cetnost in nejcastejsi:
        print(f"{slovo:<30} | {cetnost:<10}")
    print("="*45)

    # Grafické zobrazení
    if plt and nejcastejsi:
        slova_graf, cetnosti_graf = zip(*nejcastejsi)
        plt.figure(figsize=(10, 6))
        plt.bar(slova_graf, cetnosti_graf, color='skyblue')
        plt.xlabel('Slova')
        plt.ylabel('Četnost')
        plt.title('Top 5 nejčastějších slov')
        print("\nZobrazuji graf (zavřete okno grafu pro ukončení skriptu)...")
        plt.show()
    elif not plt:
        print("\nPoznámka: Knihovna matplotlib není nainstalována, graf nebude zobrazen.")

if __name__ == '__main__':
    text = ""
    # Načítání ze souboru, pokud je zadán argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        else:
            print(f"Soubor {file_path} nebyl nalezen.")
            sys.exit(1)
    else:
        # Jinak načítání z klávesnice/standardního vstupu
        if sys.stdin.isatty():
            print("Vložte text pro analýzu (ukončete Ctrl+Z na Windows):")
        text = sys.stdin.read().strip()

    if text:
        analyzuj_text(text)
