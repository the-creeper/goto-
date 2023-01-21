import requests,os,re
from sousuo import sousuo
from moyu import moyu
from kaisou import kaisou
from bilibili import bilibili
from add import add
from open_uf import open_uf
from Del import Del
from cls import cls
from fanyi import fanyi
from goto import goto
from cd import cd
from chdir import chdir
from run import run
from help import help
from count import count
from Cmd import cmd
from csdn import csdn
from date import date
from ddos import ddos
from bing import bing
from pip_install import pip_install
from Happy_Chinese_New_Year import Happy_Chinese_New_Year
from Happy_Christmas import Happy_Christmas
from runoob import runoob
from codepen import codepen
from fsou import fsou
from cg import cg
from Happy_Birthday import Happy_Birthday
from hot import hot
from ping import ping

os.chdir(os.path.dirname(__file__))
print('输入：“help”获取帮助')
while True:
    try:
        enter = input('>>> ')
        if bool(re.match('^[ ]+$',enter)):
            pass
        elif enter == '':
            pass
        elif enter == 'quit':
            break
        elif enter.split(' ')[0] == 'sousuo':
            sousuo(enter)
        elif enter == 'moyu':
            moyu()
        elif enter.split(' ')[0] == 'kaisou':
            kaisou(enter)
        elif enter.split(' ')[0] == 'bilibili':
            bilibili(enter)
        elif enter.split(' ')[0] == 'add':
            add(enter)
        elif enter == 'open_uf':
            open_uf()
        elif enter == 'del':
            Del()
        elif enter == 'cls':
            cls()
        elif enter.split(' ')[0] == 'fanyi':
            fanyi(enter)
        elif enter.split(' ')[0] == 'goto':
            goto(enter)
        elif enter.split(' ')[0] == 'cd':
            cd(enter)
        elif enter == 'chdir':
            chdir()
        elif enter.split(' ')[0] == 'run':
            run(enter)
        elif enter == 'help':
            help()
        elif enter.split(' ')[0] == 'count':
            count(enter)
        elif enter[0:4] == 'cmd ' or enter == 'cmd':
            cmd(enter)
        elif enter.split(' ')[0] == 'csdn':
            csdn(enter)
        elif enter == 'date':
            date()
        elif enter.split(' ')[0] == 'ddos':
            ddos()
        elif enter.split(' ')[0] == 'bing':
            bing(enter)
        elif enter.split(' ')[0] == 'pip_install':
            pip_install(enter)
        elif enter.split(' ')[0] == 'Happy_Chinese_New_Year':
            Happy_Chinese_New_Year(enter)
        elif enter == 'Happy_Christmas':
            Happy_Christmas()
        elif enter.split(' ')[0] == 'runoob':
            runoob(enter)
        elif enter.split(' ')[0] == 'codepen':
            codepen(enter)
        elif enter.split(' ')[0] == 'fsou':
            fsou(enter)
        elif enter.split(' ')[0] == 'cg' or enter == 'cg':
            cg(enter)
        elif enter.split(' ')[0] == 'Happy_Birthday':
            Happy_Birthday(enter)
        elif enter == 'hot':
            hot()
        elif enter.split(' ')[0] == 'ping':
            ping(enter)
        else:
            print('Error')
    except:
        print('Error')

