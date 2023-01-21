import os

def goto(enter):
    url = enter[5:]
    os.system('start ' + url)
