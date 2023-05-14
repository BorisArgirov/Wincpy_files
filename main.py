__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import shutil
import os

def clean_cache():
    path = 'files/cache'
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)


import zipfile        

def cache_zip(file_path, cache_dir_path):
    file_path = 'files/data.zip'
    cache_dir_path = 'files/cache'
    
    with zipfile.ZipFile(file_path, 'r' ) as zip_file:
        zip_file.extractall(cache_dir_path)


import os

def cached_files():
    cache = os.path.abspath('files/cache')
    files = os.listdir('files/cache')
    file_paths = [os.path.join(cache, f) for f in files if os.path.isfile(os.path.join(cache, f))]
    return file_paths
#print(cached_files())

import re
def find_password(file_paths):

    password_word = r'password:\s*(\S+)'
    
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            contents = file.read()
            match = re.search(password_word, contents)
            if match:
                return match.group(1)

    return None

file_paths = cached_files()
password = find_password(file_paths)
print(password)

    




    

    