import os
import pandas as pd
from tabulate import tabulate

# Optional PDF support
try:
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False

def mostra_anteprima(df):
    print("\n📄 Anteprima:")
    print(tabulate(df.head(5), headers='keys', tablefmt='psql', showindex=False))

def mostra_colonne(df):
    print("\n📑 Elenco colonne:")
    for idx, col in enumerate(df.columns, 1):
        print(f"{idx}: {col}")

def salva_csv(df, file_path):
    nuovo_path = f"{os.path.splitext(file_path)[0]}_modificato.csv"
    df.to_csv(nuovo_path, index=False)
    return nuovo_path

def salva_txt(df, file_path):
    nuovo_path = f"{os.path.splitext(file_path)[0]}_formattato.txt"
    df_pulito = df.copy().astype(str).apply(lambda x: x.str.strip())
    tabella = tabulate(df_pulito, headers='keys', tablefmt='grid', showindex=False)
    with open(nuovo_path, 'w', encoding='utf-8') as f:
        f.write(tabella)
    return nuovo_path

def salva_pdf(df, file_path):
    nuovo_path = f"{os.path.splitext(file_path)[0]}_tabella.pdf"
    doc = SimpleDocTemplate(nuovo_path, pagesize=letter)
    data = [df.columns.tolist()] + df.values.tolist()
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 10),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    doc.build([table])
    return nuovo_path

def salva_finale(df, path_originale):
    print("\n💾 In che formato vuoi salvare il file?")
    print("1. CSV")
    print("2. TXT (formattato)")
    if PDF_SUPPORT:
        print("3. PDF")
    scelta = input("Scegli (1/2/3): ").strip()

    if scelta == '1':
        path = salva_csv(df, path_originale)
    elif scelta == '2':
        path = salva_txt(df, path_originale)
    elif scelta == '3' and PDF_SUPPORT:
        path = salva_pdf(df, path_originale)
    else:
        print("❌ Scelta non valida o supporto PDF non disponibile.")
        return None

    print(f"\n✅ File salvato come: {path}")
    return path

def elimina_colonne(df):
    mostra_colonne(df)
    colonne_input = input("\nInserisci numeri colonne da eliminare (es. 1,3): ").strip()
    try:
        colonne_da_eliminare = [int(x.strip()) - 1 for x in colonne_input.split(',')]
        colonne_non_valide = [i+1 for i in colonne_da_eliminare if i < 0 or i >= len(df.columns)]
        if colonne_non_valide:
            print(f"Colonne non valide: {colonne_non_valide}")
            return df
        df = df[[col for i, col in enumerate(df.columns) if i not in colonne_da_eliminare]]
        print("✅ Colonne eliminate.")
        mostra_anteprima(df)
    except Exception as e:
        print(f"❌ Errore: {e}")
    return df

def ordina_per_colonna_avanzato(df):
    print("\n🛠 Ordina per colonna:")
    scelta_tipo = input("Vuoi ordinare in modo alfabetico (a) o numerico (n)? (a/n): ").lower().strip()
    if scelta_tipo not in ['a', 'n']:
        print("❌ Scelta non valida, uso alfabetico di default.")
        scelta_tipo = 'a'

    mostra_colonne(df)
    colonna = input("Inserisci il nome della colonna da ordinare: ").strip()

    if colonna not in df.columns:
        print("❌ Colonna non trovata.")
        return df

    ascending = True  # Puoi estendere per scegliere asc/desc

    try:
        if scelta_tipo == 'a':
            df = df.sort_values(by=colonna, key=lambda col: col.astype(str).str.lower(), ascending=ascending)
        else:
            df = df.sort_values(by=colonna, key=lambda col: pd.to_numeric(col, errors='coerce'), ascending=ascending)
        print(f"✅ Ordinamento '{colonna}' effettuato in modo {'alfabetico' if scelta_tipo == 'a' else 'numerico'}.")
        mostra_anteprima(df)
    except Exception as e:
        print(f"❌ Errore durante l'ordinamento: {e}")

    return df

def rimuovi_duplicati(df):
    prima = len(df)
    df = df.drop_duplicates()
    dopo = len(df)
    print(f"🧹 Righe duplicate rimosse: {prima - dopo}")
    return df

def naviga_file_csv(start_dir='.'):
    current_path = os.path.abspath(start_dir)
    while True:
        print(f"\n📂 Cartella: {current_path}")
        contenuti = os.listdir(current_path)
        cartelle = sorted([d for d in contenuti if os.path.isdir(os.path.join(current_path, d))])
        file_csv = sorted([f for f in contenuti if f.lower().endswith('.csv')])

        voci = cartelle + file_csv
        if current_path != '/':
            voci.insert(0, '..')

        for i, voce in enumerate(voci, 1):
            tipo = "📁" if voce in cartelle or voce == '..' else "📝"
            print(f"{i}. {tipo} {voce}")

        scelta = input("🔸 Seleziona numero file/cartella (q per uscire): ").strip()
        if scelta.lower() == 'q':
            return None

        try:
            idx = int(scelta) - 1
            voce_scelta = voci[idx]
            percorso = os.path.join(current_path, voce_scelta)

            if voce_scelta == '..':
                current_path = os.path.dirname(current_path)
            elif os.path.isdir(percorso):
                current_path = percorso
            elif os.path.isfile(percorso) and voce_scelta.endswith('.csv'):
                return os.path.abspath(percorso)
        except Exception:
            print("❌ Scelta non valida.")

def main():
    print("📊 CSV Table Formatter Turbo Mode v3.1")
    print("--------------------------------------")

    print("\n📁 Selezione file:")
    print("1. Naviga tra cartelle")
    print("2. Inserisci percorso manualmente")
    scelta = input("Scegli (1/2): ").strip()

    if scelta == '1':
        file_path = naviga_file_csv()
    else:
        file_path = input("📄 Inserisci percorso CSV: ").strip()

    if not file_path or not os.path.exists(file_path):
        print("❌ File non trovato.")
        return

    df = None
    for enc in ['utf-8', 'latin-1', 'cp1252']:
        try:
            df = pd.read_csv(file_path, encoding=enc)
            print(f"✅ File caricato con encoding: {enc}")
            break
        except:
            continue
    if df is None:
        print("❌ Errore apertura file.")
        return

    df_modificato = df.copy()
    mostra_anteprima(df_modificato)

    while True:
        print("\n📋 Menu operazioni:")
        print("1. Elimina colonne")
        print("2. Ordina dati (alfabetico o numerico)")
        print("3. Rimuovi duplicati")
        print("4. Salva ed esci")
        print("5. Esci senza salvare")

        opzione = input("Scegli (1-5): ").strip()
        if opzione == '1':
            df_modificato = elimina_colonne(df_modificato)
        elif opzione == '2':
            df_modificato = ordina_per_colonna_avanzato(df_modificato)
        elif opzione == '3':
            df_modificato = rimuovi_duplicati(df_modificato)
        elif opzione == '4':
            salva_finale(df_modificato, file_path)
            break
        elif opzione == '5':
            print("👋 Uscita senza salvare.")
            break
        else:
            print("❌ Opzione non valida.")

if __name__ == "__main__":
    main()

