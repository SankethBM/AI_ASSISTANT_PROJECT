import os

import eel

eel.init("frontend")

os.system('microsoft-edge --app="http://localhost:5500/frontend/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)