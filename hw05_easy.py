__author__ = 'Матиек Игорь Николаевич'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import re
import sys
import shutil

for i in range(1, 10):
    mk_dir = 'dir_{}'.format(i)
    dir_path = os.path.join(os.getcwd(), mk_dir)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('{} directory already exists'.format(mk_dir))

dir_path = os.path.abspath(os.getcwd())
for i in os.listdir(dir_path):
    if re.findall(r'^dir_\d$', i):
        os.rmdir('{}\{}'.format(dir_path, i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

dir_path = os.path.abspath(os.getcwd())
print(dir_path)
for i in os.listdir(dir_path):
    if os.path.isdir('{}\{}'.format(dir_path, i)):
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

copy_file = sys.argv[0].split('.')
shutil.copy(sys.argv[0], '{}_copy.{}'.format(copy_file[0], copy_file[1]))
