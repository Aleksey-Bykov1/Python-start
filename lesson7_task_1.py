import os


def create_dir(master='my_project', slave_1='settings', slave_2='mainapp',
               slave_3='adminapp', slave_4='authapp'):
    dir_path = os.path.join(master, slave_1)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    dir_path = os.path.join(master, slave_2)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    dir_path = os.path.join(master, slave_3)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    dir_path = os.path.join(master, slave_4)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


if __name__ == '__main__':
    create_dir()  # Если функция без значений, создастся по умолчанию. Или вписать свои названия папок
