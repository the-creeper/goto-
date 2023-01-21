import os

def cmd(enter):
    if len(enter) == 3:
        os.system('cmd')
    else:
        os.system(enter[4:])
