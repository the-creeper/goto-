import os

os.chdir(os.path.dirname(__file__))
def Del():
    if not os.path.exists('user.txt'):
        print('Error')
    else:
        os.remove('user.txt')
