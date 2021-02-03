import os
import platform

if (platform.system() == 'Windows'):
    os.system('set FLASK_APP=main.py')
    os.system('flask run')
else:
    os.system('export FLASK_APP=main.py')
    os.system('flask run')