import os

os.chdir(os.path.dirname(__file__))
def add(enter):
    a = enter[4:]
    if not os.path.exists('user.txt'):
        with open('user.txt','w',encoding='utf-8') as fs:
            fs.write('')
    with open('user.txt','a',encoding='utf-8') as fs:
        fs.write(a + '\n')
