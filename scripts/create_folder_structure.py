import os
import sys

BASE_PATH = '../{discipline}'

def _create_folder(discipline, dir_name):
    path = BASE_PATH + '/{dir_name}'
    path = path.format(discipline=discipline, dir_name=dir_name)

    os.makedirs(path)

def _create_file(discipline, filename):
    path = BASE_PATH + '/{filename}'
    path = path.format(discipline=discipline, filename=filename)

    open(path, 'wb').close()

def create_folders(discipline):
    dir_names = ['implementacoes', 'resumos', 'leites']
    for dir_name in dir_names:
        _create_folder(discipline, dir_name)

def create_files(discipline):
    filenames = ['visaoGeralEDicas.md', 'linksUteis.md', 'dificuldadesComuns.md', 'extras.md']
    for filename in filenames:
        _create_file(discipline, filename)

if __name__ == '__main__':
    _, discipline = sys.argv
    create_folders(discipline)
    create_files(discipline)
