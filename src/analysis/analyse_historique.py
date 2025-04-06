
import pandas as pd

def charger_historique_loto(fichier_csv):
    try:
        df = pd.read_csv(fichier_csv)
        print(f"✅ Fichier chargé : {fichier_csv}")
        print(f"Nombre de tirages : {len(df)}")
        print("Aperçu des 5 derniers tirages :\n")
        print(df.head(5))
        return df
    except Exception as e:
        print(f"❌ Erreur lors du chargement : {e}")
        return None

if __name__ == "__main__":
    # Remplace ce chemin par le chemin vers ton fichier local si besoin
    fichier = "data/historique_loto_format_standard_from_excel.csv"
    charger_historique_loto(fichier)
