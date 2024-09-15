import os
import urllib.request
import urllib.error
import concurrent.futures
import logging

# Configuration des logs
logging.basicConfig(filename='fichiers_trouves.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Liste des extensions de fichiers de sauvegarde
extensions = [
    ".backup", ".bck", ".old", ".save", ".bak", ".sav", "~", ".copy",
    ".orig", ".tmp", ".txt", ".back", ".bkp", ".bac", ".tar", ".gz",
    ".tar.gz", ".zip", ".rar", ".dump", ".sql", ".bak1", ".bak2",
    ".log", ".swp", ".swo", ".data", ".archive", ".bakx", ".snapshot",
    ".map"
]

# Fonction pour créer le dossier 'result' s'il n'existe pas
def create_results_directory():
    if not os.path.exists('result'):
        os.makedirs('result')

def verifier_fichier(url, fichier, extension):
    try:
        reponse = urllib.request.urlopen(url)
        code = reponse.getcode()
        if code == 200:
            result_path = os.path.join('result', f"{extension[1:]}.txt")
            with open(result_path, 'a') as f:
                f.write(f"{url} Code : {code}\n")
            logging.info(f"{url} Code : {code}")
            print(f"{url} Code : {code}")
        elif code == 404:
            print(f"{url} Code : 404 - Non trouvé")
        else:
            print(f"{url} Code : {code}")
    except urllib.error.HTTPError as e:
        logging.error(f"{url} Code : {e.code} - {e.reason}")
        print(f"{url} Code : {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        logging.error(f"{url} Erreur de connexion : {e.reason}")
        print(f"{url} Erreur de connexion : {e.reason}")
    except Exception as e:
        logging.error(f"{url} Erreur inattendue : {str(e)}")
        print(f"{url} Erreur inattendue : {str(e)}")

def verifier_fichiers(hote, fichiers):
    create_results_directory()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for fichier in fichiers:
            for ext in extensions:
                url = f"{hote}{fichier}.php{ext}"
                futures.append(executor.submit(verifier_fichier, url, fichier, ext))
        # Attendre que toutes les tâches soient terminées
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    hote = input("Veuillez entrer l'URL de l'hôte (ex. http://example.com/): ").strip()
    fichiers_input = input("Veuillez entrer la liste des fichiers à vérifier, séparés par des espaces (ex. index file1 file2): ").strip()
    fichiers = fichiers_input.split()

    if not hote or not fichiers:
        print("L'hôte et la liste des fichiers ne peuvent pas être vides.")
    else:
        verifier_fichiers(hote, fichiers)
