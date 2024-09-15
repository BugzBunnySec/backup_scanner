Description
backup_scanner.py est un script Python conçu pour scanner un serveur web à la recherche de fichiers de sauvegarde potentiels. Il teste différentes extensions de fichiers pour voir si des fichiers de sauvegarde existent à un emplacement spécifique. Les fichiers trouvés sont téléchargés et enregistrés dans un dossier nommé result.

Fonctionnalités
Recherche de Fichiers de Sauvegarde : Scanne un serveur web pour des fichiers de sauvegarde communs en testant diverses extensions.
Téléchargement et Enregistrement : Télécharge le contenu des fichiers trouvés et les enregistre dans un dossier local.
Concurrence : Utilise le traitement parallèle pour améliorer les performances du scan.
Journalisation : Enregistre les résultats et les erreurs dans un fichier journal (fichiers_trouves.log).
Liste des Extensions Testées
Le script teste les extensions suivantes pour détecter les fichiers de sauvegarde :

.backup, .bck, .old, .save, .bak, .sav, ~, .copy
.orig, .tmp, .txt, .back, .bkp, .bac, .tar, .gz
.tar.gz, .zip, .rar, .dump, .sql, .bak1, .bak2
.log, .swp, .swo, .data, .archive, .bakx, .snapshot
.map

Prérequis
Python 3.x
Bibliothèques Python standard (urllib, concurrent.futures, os, logging)
Installation
Clonez ou téléchargez le script backup_scanner.py et placez-le dans un répertoire de votre choix.

Utilisation
Exécution du Script : Ouvrez un terminal ou une ligne de commande et exécutez le script avec la commande suivante :

python backup_scanner.py
Entrée des Informations : Le script vous demandera les informations suivantes :

URL de l'hôte : L'URL de base du serveur à scanner (par exemple, http://example.com/).
Liste des fichiers : Les noms des fichiers que vous souhaitez vérifier, séparés par des espaces (par exemple, index file1 file2).
Résultats :

Les fichiers trouvés seront enregistrés dans le dossier result, avec un nom basé sur l'extension trouvée et le nom du fichier testé.
Les résultats de la recherche sont également enregistrés dans un fichier journal nommé fichiers_trouves.log.
Exemple

python backup_scanner.py

Veuillez entrer l'URL de l'hôte (ex. http://example.com/): http://example.com/
Veuillez entrer la liste des fichiers à vérifier, séparés par des espaces (ex. index file1 file2): index file1 file2


Notes
Assurez-vous que le dossier result est accessible en écriture pour que les fichiers puissent être enregistrés.
Les fichiers de sauvegarde sont identifiés en fonction des extensions testées. D'autres extensions peuvent être ajoutées en modifiant la liste dans le script.
