import sys
import os

# Ajouter le répertoire courant au chemin Python
INTERP = os.path.expanduser("/usr/bin/python3.10")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

# Importer l'application Flask
from app import app as application