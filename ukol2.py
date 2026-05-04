import matplotlib.pyplot as plt
import requests
import sys

def stahni_data(start_date, end_date):
    # Souřadnice Brna
    lat, lon = 49.1951, 16.6068
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max",
        "timezone": "Europe/Berlin"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data['daily']['temperature_2m_max']
    except Exception as e:
        print(f"Chyba při stahování dat ({start_date}): {e}")
        return None

def main():
    print("Stahuji reálná data z Open-Meteo API...")
    
    # Vybrané týdny v roce 2024 (Po-Ne)
    leden_data = stahni_data("2024-01-15", "2024-01-21")
    cervenec_data = stahni_data("2024-07-15", "2024-07-21")
    
    if not leden_data or not cervenec_data:
        print("Nepodařilo se stáhnout data. Ujistěte se, že jste připojeni k internetu.")
        return

    dny = ["Po", "Út", "St", "Čt", "Pá", "So", "Ne"]
    rozdil = [c - l for c, l in zip(cervenec_data, leden_data)]

    # Styl a nastavení
    plt.style.use('ggplot') # Moderní a čistý vzhled
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 11), sharex=True)

    # --- HORNÍ GRAF: Teploty ---
    ax1.plot(dny, leden_data, label="Leden 2024", color="#3498db", marker="o", linewidth=2.5, markersize=8)
    ax1.plot(dny, cervenec_data, label="Červenec 2024", color="#e74c3c", marker="s", linewidth=2.5, markersize=8)

    # Komfortní zóna - jemnější
    ax1.axhspan(18, 24, color='gray', alpha=0.1, label="Komfortní zóna (18–24°C)")

    # Anotace s lepším odsazením a stylem
    max_val, min_val = max(cervenec_data), min(leden_data)
    idx_max, idx_min = cervenec_data.index(max_val), leden_data.index(min_val)

    ax1.annotate(f'MAXIMUM\n{max_val}°C', 
                 xy=(dny[idx_max], max_val), xytext=(0, 25), 
                 textcoords='offset points', ha='center', fontweight='bold',
                 bbox=dict(boxstyle="round4,pad=0.5", fc="#fdf2f2", ec="#e74c3c", alpha=0.9),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", color="#e74c3c", lw=1.5))

    ax1.annotate(f'MINIMUM\n{min_val}°C', 
                 xy=(dny[idx_min], min_val), xytext=(0, -40), 
                 textcoords='offset points', ha='center', fontweight='bold',
                 bbox=dict(boxstyle="round4,pad=0.5", fc="#f2f8fd", ec="#3498db", alpha=0.9),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color="#3498db", lw=1.5))

    ax1.set_title("Srovnání teplot v lednu a červenci", fontsize=15, pad=15)
    ax1.set_ylabel("Teplota (°C)", fontsize=13)
    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=11) # Legenda vně grafu
    ax1.set_ylim(min_val - 15, max_val + 15)

    # --- SPODNÍ GRAF: Rozdíl ---
    bars = ax2.bar(dny, rozdil, color='#9b59b6', alpha=0.7, edgecolor='#8e44ad', linewidth=1.2)
    ax2.set_title("Denní teplotní rozdíl (Léto vs. Zima)", fontsize=13, pad=10)
    ax2.set_ylabel("Rozdíl teplot (Δ°C)", fontsize=13)
    ax2.set_xlabel("Den v týdnu", fontsize=13, labelpad=10)

    # Přidání hodnot nad sloupce s lepším formátováním
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                 f'+{height:.1f}°', ha='center', va='bottom', fontsize=11, fontweight='bold')

    ax2.set_ylim(0, max(rozdil) + 5)

    # Celkový nadpis a doladění mezer
    plt.suptitle("Analýza klimatických dat: Brno 2024", fontsize=20, fontweight='bold', y=0.96)
    plt.tight_layout(rect=[0, 0.03, 0.9, 0.93]) # Necháme místo pro legendu a hlavní nadpis

    print("Zobrazuji vylepšený graf...")
    plt.show()

if __name__ == "__main__":
    main()
