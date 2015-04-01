import urllib.request
import sys
import os
import zipfile
import shutil


def update_runterladen():
    urllib.request.urlretrieve('http://kleintk.tk/tk-file/daten/Twitch-Channel-Checker.zip', 'update.zip')
    with zipfile.ZipFile('update.zip', 'r') as zfile:
        data = zfile.read('Twitch-Channel-Checker/library.zip')
        neue_datei = open('patch.zip', 'wb')
        neue_datei.write(data)
        neue_datei.close()
    os.remove('update.zip')

def library_ersetzen():
    shutil.copy('patch.zip', '../library.zip')
    os.remove('patch.zip')

update_runterladen()
library_ersetzen()