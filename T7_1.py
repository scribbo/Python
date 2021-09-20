import os

project_list = ['settings', 'mainapp', 'adminapp', 'authapp']
for name in project_list:
   dir_path = os.path.join('my_project', name)
   if not os.path.exists(dir_path):
      os.makedirs(dir_path)
   else:
      print(f'Папка с именем {name} уже существует')
