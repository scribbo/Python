from os import path, walk, listdir
import shutil

project_name = 'my_project'

try:
    for root, dirs, files in walk(project_name):
        print(root, dirs, files)
        if 'templates' in dirs and root != project_name:
            for el in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', el), path.join(project_name, 'templates', el))
except FileExistsError:
    print('Шаболоны уже собраны в папку Templates')
