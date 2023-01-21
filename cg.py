import os

def cg(enter):
    if enter == 'cg /?':
        print('''
输入：cg + 工具
如cg HTML 压缩/解压工具
即可搜索
更多工具请输入：“cg”
''')
    else:
        if enter == 'cg':
            os.system('start https://c.runoob.com')
        else:
            os.system('start https://c.runoob.com/index.php?s=' + enter[3:])
