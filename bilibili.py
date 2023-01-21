import os

def bilibili(enter):
    url = 'https://search.bilibili.com/all?keyword=' + enter.split(' ')[1]
    os.system('start ' + url)
