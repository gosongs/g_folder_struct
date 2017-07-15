# coding=utf-8
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

global OUTPUT
OUTPUT = ''

# 被忽略的文件夹
IGNORES = ['.idea', 'node_modules', '.vscode', '.git']


# 文件夹在前, 文件在后
def sort(arr):
    dirs = []
    files = []
    for i in arr:
        if (os.path.isdir(i)):
            dirs.append(i)
        else:
            files.append(i)
    return dirs + files


def each_file(path, time):
    path = path.replace('\n', '')
    global OUTPUT
    path_dir = os.listdir(path)
    time += 1

    for p in path_dir:
        print(p)
        if len(path_dir):
            final = path_dir[-1]
            split = '├──' if p != final else '└──'

            space = ''
            for t in range(time - 1):
                space += '|   '

            line = '{space}{split}{p}\n'.format(p=p, space=space, split=split)
            OUTPUT += line

            new_dir = os.path.join(path, p)
            if os.path.isdir(new_dir) and p not in IGNORES:
                each_file(new_dir, time)


def write_md(output):
    f = open('menu_struct.md', 'w')
    f.write('```\n')
    f.write(output)
    f.write('```\n')
    f.close()


def start():
    # 获取当前路径
    cur_path = os.path.split(os.path.realpath(__file__))[0]
    each_file(cur_path, 0)
    write_md(OUTPUT)


start()