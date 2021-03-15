import os
from shutil import copytree

root_dir = 'my_project'
dir_name = 'tamplates'

for root, dirs, files in os.walk(root_dir):
    if root.find(dir_name) > 0 and len(files) == 0:
        copytree(os.path.join(root), dir_name, dirs_exist_ok=True)
