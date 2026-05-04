---
marp: true
theme: default
paginate: true
header: ' '
footer: 'Cvičení 13 · Algoritmizace a programování · Brno 2026'
backgroundColor: #0f172a
style: |
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&family=JetBrains+Mono:wght@500&display=swap');

  section {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background: #0f172a;
    background-image: 
      radial-gradient(at 100% 0%, rgba(30, 64, 175, 0.3) 0px, transparent 50%),
      radial-gradient(at 0% 100%, rgba(15, 23, 42, 1) 0px, transparent 50%);
    color: #f8fafc;
    padding: 60px;
    font-size: 32px;
    line-height: 1.4;
  }

  h1 {
    font-size: 2.8em;
    font-weight: 800;
    letter-spacing: -0.04em;
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
  }

  h2 {
    font-size: 1.4em;
    font-weight: 600;
    color: #94a3b8;
    margin-bottom: 40px;
    border: none;
  }

  h3 {
    font-size: 1.2em;
    color: #38bdf8;
    font-weight: 700;
    margin-bottom: 25px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  /* Čisté karty */
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }

  .card {
    background: rgba(30, 41, 59, 0.7);
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-radius: 24px;
    padding: 35px;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  }

  .card h4 {
    color: #38bdf8;
    margin: 0 0 15px 0;
    font-size: 1.1em;
  }

  .card p {
    margin: 0;
    font-size: 0.85em;
    color: #cbd5e1;
  }

  /* Tabulka s vysokým kontrastem */
  table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin-top: 20px;
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(148, 163, 184, 0.2);
  }

  th {
    background: #1e293b;
    color: #38bdf8;
    padding: 20px;
    font-size: 0.75em;
    text-align: left;
    font-weight: 800;
  }

  td {
    background: rgba(30, 41, 59, 0.5);
    padding: 20px;
    border-top: 1px solid rgba(148, 163, 184, 0.1);
    font-size: 0.9em;
  }

  /* Akcenty */
  .highlight { color: #38bdf8; font-weight: 700; }
  .warning { color: #fbbf24; font-weight: 700; }
  
  blockquote {
    border-left: 8px solid #38bdf8;
    background: rgba(56, 189, 248, 0.1);
    margin: 30px 0;
    padding: 20px 40px;
    border-radius: 0 20px 20px 0;
    font-style: italic;
    font-size: 1.1em;
  }

  footer { font-size: 14px; color: #64748b; }
---

<!-- _class: title -->
# AI AGENTI 2026
## Nový standard vývoje software
### Od asistence k autonomii

---

### 📉 Konec éry "Copy-Paste"
V roce 2023 jsme kód kopírovali. V roce 2026 ho <span class="highlight">delegujeme</span>.

- **Problém:** ChatGPT nevidí váš souborový systém.
- **Důsledek:** Neustálý kontext-switching (přepínání oken).
- **Řešení:** Agenti běžící přímo nad vaším kódem.

---

### 🔄 Agentní cyklus (Reasoning)
Agent není jen generátor textu. Je to <span class="highlight">intelektuální smyčka</span>:

1. **Analýza:** Prohledá codebase a najde souvislosti.
2. **Plán:** Navrhne kroky (např. "Nainstaluj `pandas`, pak uprav `main.py`").
3. **Exekuce:** Zapíše kód, spustí terminál, provede commit.
4. **Validace:** Přečte chyby a <span class="highlight">sám se opraví</span>.

---

### ⚔️ Srovnání: Chatbot vs. Agent

| Funkce | Tradiční Chatbot | Moderní AI Agent |
| :--- | :--- | :--- |
| **Přístup** | Izolovaný prohlížeč | **Terminál, Filesystem, Git** |
| **Kontext** | Jen to, co vložíte | **Celý váš projekt (1M+ tok.)** |
| **Výsledek** | "Tady je kód..." | **"Tady je hotová featura."** |
| **Chyby** | Musíte je řešit vy | **Vyřeší je autonomně** |

---

### 🗺️ Klíčové nástroje dneška

<div class="grid">
<div class="card">
  <h4>GitHub Copilot</h4>
  <p>Standard pro doplňování kódu. Ideální pro <strong>každodenní psaní</strong> řádek po řádku.</p>
</div>
<div class="card">
  <h4>Claude Code / CLI</h4>
  <p>Nejvýkonnější nástroj pro <strong>komplexní refaktoring</strong> a hloubkové opravy chyb.</p>
</div>
<div class="card">
  <h4>Cursor / Windsurf</h4>
  <p>Nová generace IDE. AI <strong>nativně integrovaná</strong> do jádra editoru.</p>
</div>
<div class="card">
  <h4>Gemini CLI</h4>
  <p>Extrémní kontext. Skvělé pro <strong>analýzu obřích projektů</strong> zcela zdarma.</p>
</div>
</div>

---

### ⚠️ Pozor na "Vibe Coding"
Neprodávejte své inženýrské myšlení za pohodlí.

- <span class="warning">Riziko:</span> Kód funguje, ale vy mu nerozumíte.
- <span class="highlight">Správná cesta:</span> AI jako mentor.
  - Nechte si vysvětlit každou netriviální změnu.
  - Validujte architekturu, ne jen funkčnost.

> **"Dobrý inženýr s AI je 10x produktivnější. Špatný inženýr s AI tvoří 10x více technického dluhu."**

---

### 🏁 Shrnutí & Další kroky

1. **GitHub Copilot:** Studentská licence je nutnost.
2. **CLI Agenti:** Zkuste `claude` nebo `gemini` pro velké změny.
3. **Mindset:** Přestaňte psát kód, začněte <span class="highlight">navrhovat řešení</span>.

---

<!-- _class: title -->
# Děkuji za pozornost!
## Budoucnost patří těm, kteří ji umí ovládat. 🚀

---
